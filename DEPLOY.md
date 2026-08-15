# ☁️ Deploy Capstone Flask + PostgreSQL lên Render

> Project đã sẵn sàng: `render.yaml` khai báo cả **web service** lẫn **PostgreSQL**.
> Khi bạn Apply Blueprint, Render tự tạo database và nối `DATABASE_URL` vào app.

## Bước 1 — Đẩy code mới lên GitHub

```bash
git add -A
git commit -m "Chuyen sang PostgreSQL"
git push origin master
```

## Bước 2 — Apply Blueprint trên Render

1. Vào https://dashboard.render.com
2. Vào repo/blueprint của bạn (service đang chạy `capstone-flask-sg9i`)
3. Render phát hiện `render.yaml` có thay đổi → bấm **Apply** (hoặc **Sync Blueprint**)
4. Render sẽ tạo thêm:
   - 🗄️ **PostgreSQL** `capstone-postgres` (free)
   - Đặt biến `DATABASE_URL` cho web service (tự động)
5. Chờ deploy mới hoàn tất (~3–5 phút)

## Bước 3 — Kiểm tra

```powershell
curl https://capstone-flask-sg9i.onrender.com/api/users
curl -X POST https://capstone-flask-sg9i.onrender.com/api/users -H "Content-Type: application/json" -d '{"name":"Alice"}'
curl https://capstone-flask-sg9i.onrender.com/api/users
```

## Bước 4 — Chứng minh dữ liệu không mất khi redeploy 🔥

1. POST vài user (Alice, Binh)
2. Vào Render → bấm **Manual Deploy → Deploy latest commit** (hoặc push 1 commit mới)
3. Sau khi deploy xong, gọi lại `GET /api/users`
4. **Alice và Binh vẫn còn** → PostgreSQL hoạt động đúng!

---

## Cấu trúc `render.yaml` (giải thích)

```yaml
databases:                      # khai báo database
  - name: capstone-postgres
    plan: free
    databaseName: capstone

services:
  - type: web
    ...
    envVarGroups:               # nối DATABASE_URL từ database vừa tạo
      - key: DATABASE_URL
        fromDatabase:
          name: capstone-postgres
          property: connectionString
```

## Lưu ý

- Render Postgres free tier có hạn mức nhỏ (1GB) — đủ cho học tập/demo.
- Nếu deploy cũ (SQLite) vẫn còn, bấm **Deploy** mới để áp dụng thay đổi.
- Mật khẩu database nằm trong `DATABASE_URL` do Render quản lý — **đừng để lộ**.

