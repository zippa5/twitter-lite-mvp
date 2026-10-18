from app import User, Post, db
from tests.conftest import post_form


def test_registration_and_hash(client):
    result = post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    assert result.status_code == 200
    assert b"@alice" in result.data
    with client.application.app_context():
        user = db.session.query(User).filter_by(username="alice").one()
        assert user.password_hash != "strongpass123"
        assert user.password_hash.startswith("scrypt:")


def test_duplicate_username_rejected(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/logout", {})
    response = post_form(client, "/register", {"username": "alice", "password": "differentpass"})
    assert b"Username already taken" in response.data
    with client.application.app_context():
        assert db.session.query(User).count() == 1


def test_invalid_registration_rejected(client):
    response = post_form(client, "/register", {"username": "ab", "password": "strongpass123"})
    assert b"3" in response.data
    response = post_form(client, "/register", {"username": "validuser", "password": "short"})
    assert b"at least 8 characters" in response.data
    with client.application.app_context():
        assert db.session.query(User).count() == 0


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


def test_incorrect_password_rejected(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/logout", {})
    response = post_form(client, "/login", {"username": "alice", "password": "wrongpassword"})
    assert b"Invalid username or password" in response.data
    assert b"@alice" not in response.data


def test_feed_is_public(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/posts", {"body": "Public announcement"})
    post_form(client, "/logout", {})
    page = client.get("/").data
    assert b"Public announcement" in page
    assert b"alice" in page


def test_posts_newest_first(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/posts", {"body": "First post"})
    post_form(client, "/posts", {"body": "Second post"})
    page = client.get("/").data
    assert page.index(b"Second post") < page.index(b"First post")


def test_invalid_post_and_csrf(client):
    post_form(client, "/register", {"username": "alice", "password": "strongpass123"})
    post_form(client, "/posts", {"body": "x" * 281})
    post_form(client, "/posts", {"body": "   "})
    with client.application.app_context():
        assert db.session.query(Post).count() == 0
    assert client.post("/posts", data={"body": "no token"}).status_code == 400
