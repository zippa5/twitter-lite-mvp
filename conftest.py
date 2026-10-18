import pytest
from app import create_app, db

@pytest.fixture
def client(tmp_path):
    app = create_app({'TESTING': True, 'SECRET_KEY': 'test-only-secret', 'SQLALCHEMY_DATABASE_URI': f'sqlite:///{tmp_path / "test.db"}'})
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.session.remove()

def csrf(client):
    with client.session_transaction() as session:
        return session['_csrf']
