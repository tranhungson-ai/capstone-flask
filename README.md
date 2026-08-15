# 🚀 Capstone Flask — project mẫu cho vibe coding

Project nhỏ dành cho **Tuần 6** trong kế hoạch vibe coding, hoặc để luyện tập
ngay từ **Tuần 1–2**. Được tạo sẵn để bạn thấy một dự án hoàn chỉnh trông thế nào.

## Cài đặt & chạy

```powershell
cd capstone-flask
python -m pip install -r requirements.txt
python app.py                      # chạy server -> http://localhost:5000
```

## Test

```powershell
python -m pytest -v                # chạy tất cả test
```

## Các endpoint

| Method | Đường dẫn | Kết quả |
|---|---|---|
| GET | `/` | Trang chủ dạng text |
| GET | `/api/hello` | `{"message": "hello", "visits": n}` — mỗi lần gọi tăng biến đếm |
| GET | `/api/users` | Danh sách users đã tạo (trong bộ nhớ) |
| POST | `/api/users` | Body `{"name": "Alice"}` → `201` kèm user; thiếu `name` → `400` |

## Thử bằng curl (terminal khác)

```powershell
curl http://localhost:5000/api/hello
curl -X POST http://localhost:5000/api/users -H "Content-Type: application/json" -d '{"name":"Alice"}'
curl http://localhost:5000/api/users
```

## Bài tập vibe coding trên project này

1. Nhờ Cline **thêm endpoint** `DELETE /api/users/<id>` (đừng để AI tự ý xóa data khác).
2. Nhờ Cline **viết test** cho endpoint mới, chạy `pytest` xác minh.
3. Commit từng bước vào git.

## File trong project
- `AGENTS.md` — quy ước dành cho AI (mẫu để bạn học viết)
- `app.py` — ứng dụng chính
- `test_app.py` — pytest tests
- `requirements.txt` — thư viện
