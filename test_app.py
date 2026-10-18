from app import User, Post, db
from tests.conftest import csrf

def register(client, username='alice', password='securepass123'):
    client.get('/register')
    return client.post('/register', data={'username':username, 'password':password, '_csrf':csrf(client)}, follow_redirects=True)

def test_registration_and_hash(client):
    response = register(client)
    assert response.status_code == 200
    with client.application.app_context():
        user = db.session.query(User).filter_by(username='alice').one()
        assert user.password_hash != 'securepass123'
        assert user.password_hash.startswith('scrypt:')

def test_login_logout(client):
    register(client)
    client.post('/logout', data={'_csrf':csrf(client)})
    response = client.post('/login', data={'username':'alice','password':'wrong', '_csrf':csrf(client)}, follow_redirects=True)
    assert b'Invalid username' in response.data
    response = client.post('/login', data={'username':'alice','password':'securepass123','_csrf':csrf(client)}, follow_redirects=True)
    assert b'@alice' in response.data
    client.post('/logout', data={'_csrf':csrf(client)})
    assert client.post('/posts', data={'body':'No','_csrf':csrf(client)}).status_code == 302

def test_posts_feed_order_and_validation(client):
    register(client)
    for body in ('First', 'Second'):
        client.post('/posts', data={'body':body,'_csrf':csrf(client)})
    response = client.get('/')
    assert response.data.index(b'Second') < response.data.index(b'First')
    assert b'@alice' in response.data
    assert b'UTC' in response.data
    client.post('/posts', data={'body':'x'*281,'_csrf':csrf(client)})
    with client.application.app_context():
        assert db.session.query(Post).count() == 2

def test_csrf_protection(client):
    assert client.post('/register', data={'username':'bob','password':'password123'}).status_code == 400

def test_duplicate_and_invalid_registration(client):
    register(client)
    client.post('/logout', data={'_csrf':csrf(client)})
    response = register(client)
    assert b'already taken' in response.data
    response = register(client, 'bad name', 'short')
    assert b'Username must' in response.data

def test_xss_is_escaped(client):
    register(client)
    response = client.post('/posts', data={'body':'<script>alert(1)</script>','_csrf':csrf(client)}, follow_redirects=True)
    assert b'&lt;script&gt;' in response.data
    assert b'<script>' not in response.data

def test_persistence_between_app_instances(tmp_path):
    from app import create_app
    url = f'sqlite:///{tmp_path / "persist.db"}'
    app1 = create_app({'TESTING':True,'SECRET_KEY':'test','SQLALCHEMY_DATABASE_URI':url})
    with app1.test_client() as c:
        register(c)
        c.post('/posts', data={'body':'Still here','_csrf':csrf(c)})
    app2 = create_app({'TESTING':True,'SECRET_KEY':'test','SQLALCHEMY_DATABASE_URI':url})
    with app2.test_client() as c:
        assert b'Still here' in c.get('/').data
