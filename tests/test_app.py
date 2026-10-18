from app import User, Post, db
from tests.conftest import post_form

def test_registration_and_hash(client):
    result = post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    assert result.status_code == 200
    with client.application.app_context():
        user = db.session.query(User).filter_by(username="alice").one()
        assert user.password_hash != "strongpass123"
        assert user.password_hash.startswith("scrypt:")

def test_login_logout_and_protected_post(client):
    assert client.post("/posts", data={"body": "Hello"}).status_code == 400
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/logout", {})
    response = post_form(client, "/posts", {"body": "Not allowed"})
    assert b"Log in" in response.data
    response = post_form(client, "/login", {"username": "alice", "password": "strongpass123"})
    assert b"@alice" in response.data
    response = post_form(client, "/posts", {"body": "Hello world"})
    assert b"Hello world" in response.data

def test_posts_newest_first(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/posts", {"body": "First post"})
    post_form(client, "/posts", {"body": "Second post"})
    page = client.get("/").data
    assert page.index(b"Second post") < page.index(b"First post")

def test_invalid_post_and_csrf(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/posts", {"body": "x" * 281})
    with client.application.app_context():
        assert db.session.query(Post).count() == 0
    assert client.post("/posts", data={"body": "no token"}).status_code == 400
