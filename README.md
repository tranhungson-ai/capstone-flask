# 🚀 Capstone Flask — project mẫu cho vibe coding (PostgreSQL)

Project nhỏ dành cho **Tuần 6** trong kế hoạch vibe coding — nay dùng
**PostgreSQL** (database thật trên cloud, dữ liệu KHÔNG mất khi redeploy).

## Cài đặt & chạy local

```powershell
cd capstone-flask
python -m pip install -r requirements.txt

# Cần 1 PostgreSQL đang chạy, rồi set biến môi trường:
$env:DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/capstone"

python app.py                      # chạy server -> http://localhost:5000
```

## Test (cần DB test riêng)

```powershell
$env:TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/capstone_test"
python -m pytest -v                # 6 test xanh
```

## Các endpoint

| Method | Đường dẫn | Kết quả |
|---|---|---|
| GET | `/` | Trang chủ dạng text |
| GET | `/api/hello` | `{"message": "hello", "visits": n}` — bộ đếm |
| GET | `/api/users` | Danh sách users từ **PostgreSQL** |
| POST | `/api/users` | Body `{"name": "Alice"}` → `201`; thiếu `name` → `400` |
| DELETE | `/api/users/<id>` | Xóa user → `200`; không có → `404` |

## Tại sao PostgreSQL (thay vì SQLite)?

| | SQLite (trước) | PostgreSQL (bây giờ) |
|---|---|---|
| Dữ liệu | File `capstone.db` trong thư mục tạm | **Database riêng trên cloud** |
| Redeploy lên Render | ❌ Dữ liệu bị mất | ✅ **Dữ liệu giữ nguyên** |
| Kết nối | `sqlite3.connect(DB_PATH)` | `psycopg2.connect(DATABASE_URL)` |
| Placeholder SQL | `?` | `%s` |
| Auto-increment | `AUTOINCREMENT` | `SERIAL` |
| Lấy id sau INSERT | `cur.lastrowid` | `INSERT ... RETURNING id` |

## Deploy lên cloud ☁️

`render.yaml` đã khai báo sẵn **PostgreSQL blueprint** — khi bạn Apply Blueprint
trên Render, nó tự tạo database + set `DATABASE_URL` cho app. Xem `DEPLOY.md`.

## Cấu trúc dự án
```
capstone-flask/
├── AGENTS.md       # quy ước cho AI
├── app.py          # ứng dụng Flask
├── db.py           # tầng database PostgreSQL
├── test_app.py     # pytest (dùng TEST_DATABASE_URL)
├── Procfile        # cho cloud: gunicorn app:app
├── render.yaml     # Blueprint: web + Postgres
├── requirements.txt
├── DEPLOY.md
└── .gitignore
```

## 🔥 Kiểm chứng persistence (2026-08-15)

Đây là commit trigger để **redeploy**. Nếu Alice & Binh vẫn còn trong database
sau lần redeploy này → PostgreSQL đã chứng minh dữ liệu **không mất khi redeploy**.


