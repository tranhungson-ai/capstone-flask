import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_hello_endpoint(client):
    r = client.get("/api/hello")
    assert r.status_code == 200
    data = r.get_json()
    assert data["message"] == "hello"
    assert data["visits"] == 1


def test_create_user_ok(client):
    r = client.post("/api/users", json={"name": "Alice"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["name"] == "Alice"
    assert data["id"] == 1


def test_create_user_missing_name(client):
    r = client.post("/api/users", json={})
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_create_user_invalid_json(client):
    r = client.post("/api/users", data="not json", content_type="application/json")
    assert r.status_code == 400
