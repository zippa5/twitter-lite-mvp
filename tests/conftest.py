import pytest
from app import create_app, db

@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True, "SECRET_KEY": "test-secret", "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(tmp_path / "test.db")})
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

def post_form(client, url, data):
    client.get("/")
    with client.session_transaction() as session:
        token = session["_csrf"]
    return client.post(url, data={**data, "_csrf": token}, follow_redirects=True)
