import os

import pytest

import db
from app import app

# DB test rieng (can PostgreSQL dang chay local):
#   $env:TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/capstone_test"
TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/capstone_test",
)


@pytest.fixture
def client():
    """Moi test dung DB test rieng va lam sach bang users truoc khi chay."""
    db.DATABASE_URL = TEST_DATABASE_URL
    db.init_db()
    with db.get_connection() as conn, conn.cursor() as cur:
        cur.execute("TRUNCATE users RESTART IDENTITY")
        conn.commit()
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


def test_delete_user_ok(client):
    client.post("/api/users", json={"name": "Alice"})
    r = client.delete("/api/users/1")
    assert r.status_code == 200
    assert client.get("/api/users").get_json() == []


def test_delete_user_not_found(client):
    r = client.delete("/api/users/999")
    assert r.status_code == 404
    assert "error" in r.get_json()


