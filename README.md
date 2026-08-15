# 🚀 Capstone Flask — project mẫu cho vibe coding (SQLite)

Project nhỏ dành cho **Tuần 6** trong kế hoạch vibe coding, nay đã nâng cấp lên
**SQLite** (database thật) và sẵn sàng **deploy lên cloud**.

## Cài đặt & chạy

```powershell
cd capstone-flask
python -m pip install -r requirements.txt
python app.py                      # chạy server -> http://localhost:5000
```

## Test

```powershell
python -m pytest -v                # 6 test xanh
```

## Các endpoint

| Method | Đường dẫn | Kết quả |
|---|---|---|
| GET | `/` | Trang chủ dạng text |
| GET | `/api/hello` | `{"message": "hello", "visits": n}` — bộ đếm |
| GET | `/api/users` | Danh sách users **từ SQLite** |
| POST | `/api/users` | Body `{"name": "Alice"}` → `201`; thiếu `name` → `400` |
| DELETE | `/api/users/<id>` | Xóa user → `200`; không có → `404` |

## SQLite — điều gì đã đổi?

- Trước: danh sách `users` nằm **trong bộ nhớ** → restart server là mất hết.
- Bây giờ: dữ liệu nằm trong file **`capstone.db`** → **restart vẫn còn**.
- File `db.py` = tầng database: `init_db()`, `list_users()`, `create_user()`, `delete_user()`.
- Dùng module `sqlite3` có sẵn trong Python — **không cần cài thêm gì**.

## Deploy lên cloud ☁️

Xem hướng dẫn đầy đủ trong **`DEPLOY.md`** — nhanh nhất là Render free tier:
`gunicorn app:app` (đã có sẵn trong `Procfile`).

## Cấu trúc dự án
```
capstone-flask/
├── AGENTS.md       # quy ước cho AI
├── app.py          # ứng dụng Flask
├── db.py           # tầng database SQLite (mới!)
├── test_app.py     # pytest (mỗi test 1 DB tạm riêng)
├── Procfile        # cho cloud: gunicorn app:app
├── requirements.txt
├── DEPLOY.md       # hướng dẫn deploy (mới!)
└── .gitignore
```
