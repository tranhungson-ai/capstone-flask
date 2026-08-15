"""db.py — lop du lieu PostgreSQL cho capstone Flask.

Ket noi qua bien moi truong DATABASE_URL.
- Tren Render: render.yaml (database blueprint) tu dong set bien nay.
- Chay local: set DATABASE_URL truoc khi chay, VD:
      $env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/capstone"

Khac biet voi SQLite:
- Placeholder la %s (khong phai ?)
- id tu dong tang bang SERIAL
- Insert tra id qua RETURNING
"""

import os
from contextlib import closing

import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/capstone",
)


def get_connection():
    """Mo ket noi PostgreSQL (truy cap cot theo ten qua RealDictCursor)."""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    """Tao bang users neu chua co (goi 1 lan luc khoi dong)."""
    with closing(get_connection()) as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
            """
        )
        conn.commit()


def list_users():
    """Tra ve danh sach users tu database."""
    with closing(get_connection()) as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name FROM users ORDER BY id")
        rows = cur.fetchall()
    return [dict(r) for r in rows]


def create_user(name):
    """Them user moi, tra ve id vua tao."""
    with closing(get_connection()) as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", (name,))
        user_id = cur.fetchone()["id"]
        conn.commit()
        return user_id


def update_user(user_id, name):
    """Cap nhat ten user. Tra ve dict user neu tim thay, else None."""
    with closing(get_connection()) as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE users SET name = %s WHERE id = %s RETURNING id, name",
            (name, user_id),
        )
        row = cur.fetchone()
        conn.commit()
    return dict(row) if row else None


def delete_user(user_id):
    """Xoa user theo id. Tra ve so dong da xoa (0 = khong tim thay)."""
    with closing(get_connection()) as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        deleted = cur.rowcount
        conn.commit()
        return deleted

