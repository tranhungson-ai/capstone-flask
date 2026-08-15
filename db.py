"""db.py — lop du lieu SQLite cho capstone Flask.

Dung module sqlite3 co san trong Python (khong can cai them gi).
File database: capstone.db (tu dong tao lan dau chay).
"""

import sqlite3
from contextlib import closing

DB_PATH = "capstone.db"


def get_connection():
    """Mo ket noi SQLite. row_factory = truy cap cot theo ten."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Tao bang users neu chua co (goi 1 lan luc khoi dong)."""
    with closing(get_connection()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """
        )
        conn.commit()


def list_users():
    """Tra ve danh sach users tu database."""
    with closing(get_connection()) as conn:
        rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
    return [{"id": r["id"], "name": r["name"]} for r in rows]


def create_user(name):
    """Them user moi, tra ve id vua tao."""
    with closing(get_connection()) as conn:
        cur = conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        return cur.lastrowid


def delete_user(user_id):
    """Xoa user theo id. Tra ve so dong da xoa (0 = khong tim thay)."""
    with closing(get_connection()) as conn:
        cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return cur.rowcount
