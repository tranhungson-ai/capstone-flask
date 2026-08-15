# AGENTS.md — Quy ước dự án capstone Flask

## Bối cảnh
- Đây là project **học vibe coding**: API Flask nhỏ.
- Chạy bằng: `python app.py` (server ở `http://localhost:5000`)
- Test bằng: `python -m pytest -v`
- Cài thư viện: `python -m pip install -r requirements.txt`

## Ngôn ngữ
- Code, comment, tên biến dùng **tiếng Anh**.
- Câu trả lời cho tôi có thể dùng **tiếng Việt**.

## Luật cho AI (Cline)
- Trước khi sửa code: giải thích ngắn gọn sẽ đổi gì (2–3 dòng).
- Sau khi sửa: chạy thử test rồi báo kết quả — KHÔNG báo "xong" khi chưa chạy.
- Không cài thêm thư viện mới khi chưa được phép.
- Không xóa/sửa file ngoài phạm vi được yêu cầu.
- Nếu phát hiện vấn đề bảo mật (secret, injection...) → cảnh báo tôi ngay.

## Cấu trúc dự án
- `app.py` — ứng dụng Flask chính
- `test_app.py` — test bằng pytest
- `requirements.txt` — danh sách thư viện
- `AGENTS.md` — file này (quy ước cho AI)
