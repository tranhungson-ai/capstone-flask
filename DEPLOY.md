# ☁️ Deploy Capstone Flask lên Cloud

> Project đã sẵn sàng deploy: có `Procfile`, `requirements.txt` (kèm gunicorn), git repo sạch.

## Cách nhanh nhất: Render (miễn phí) 🚀

### Bước 1 — Đẩy code lên GitHub
1. Tạo repo công khai trên GitHub (không cần README).
2. Trong terminal, tại thư mục `capstone-flask`:
   ```bash
   git remote add origin https://github.com/<ten-ban>/capstone-flask.git
   git push -u origin master
   ```

### Bước 2 — Tạo Web Service trên Render
1. Vào https://render.com → **Sign up** (Google/GitHub) → **New +** → **Web Service**
2. **Connect** repo GitHub `capstone-flask` (lần đầu cần cấp quyền cho Render)
3. Render tự nhận `Procfile` và điền sẵn các cấu hình. Kiểm tra:
   | Trường | Giá trị |
   |---|---|
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn app:app` |
   | **Python version** | chọn bản gần nhất có sẵn |
4. Bấm **Create Web Service** → chờ ~3 phút build
5. Xong! Nhận URL dạng `https://capstone-flask-xxxx.onrender.com`

### Bước 3 — Kiểm tra
```powershell
curl https://capstone-flask-xxxx.onrender.com/api/users
curl -X POST https://capstone-flask-xxxx.onrender.com/api/users -H "Content-Type: application/json" -d '{"name":"Alice"}'
```

---

## Các nền tảng khác

| Nền tảng | Ưu điểm | Ghi chú |
|---|---|---|
| **Railway** | Đơn giản, auto-deploy từ GitHub | railway.app |
| **PythonAnywhere** | Dễ dùng, có panel web | pythonanywhere.com (cần tạo web app + WSGI `app:app`) |
| **HuggingFace Spaces** | Miễn phí, tốt cho demo | hf.co → Space type: **Docker** |
| **Fly.io / AWS / GCP** | Mạnh, chuyên nghiệp | nâng cao hơn, tốn thời gian học |

---

## ⚠️ Lưu ý quan trọng về SQLite trên cloud

- **SQLite là file** (`capstone.db`) nằm trong thư mục server. Trên Render free tier, thư mục này **bị reset mỗi khi deploy lại** → dữ liệu có thể mất.
- **Phù hợp:** demo, học tập, app cá nhân ít người dùng.
- **Khi làm sản phẩm thật:** chuyển sang **PostgreSQL** (Render có free Postgres) — cấu trúc code gần như giữ nguyên, chỉ đổi tầng `db.py`.

## 🧠 Tóm tắt quy trình deploy
```
pip install -r requirements.txt (build)  →  gunicorn app:app (start)  →  https URL
```
Chỉ 2 lệnh — đó là lý do `Procfile` + `requirements.txt` tồn tại.
