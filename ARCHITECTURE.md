# 🏗️ Kiến trúc Capstone Flask — sơ đồ trực quan

> File này dùng **Mermaid** — mở trong VS Code có extension *Markdown Preview Mermaid Support*
> rồi bấm Preview (hoặc xem trực tiếp trên GitHub) để thấy sơ đồ vẽ ra.

---

## 1. Sơ đồ tổng thể (endpoints → functions → database)

```mermaid
graph TD
    U[User / curl] -->|GET /| H[app.py: home]
    U -->|GET /api/hello| HE[app.py: hello]
    U -->|POST /api/users| CR[app.py: create_user]
    U -->|GET /api/users| LI[app.py: list_users]
    U -->|PUT /api/users/:id| UP[app.py: update_user]
    U -->|DELETE /api/users/:id| DE[app.py: delete_user]

    CR --> DB1[db.py: create_user]
    LI --> DB2[db.py: list_users]
    UP --> DB3[db.py: update_user]
    DE --> DB4[db.py: delete_user]

    DB1 --> PG[(PostgreSQL)]
    DB2 --> PG
    DB3 --> PG
    DB4 --> PG
```

## 2. Luồng 1 request POST (sequence diagram)

```mermaid
sequenceDiagram
    participant C as Client / curl
    participant F as Flask app.py
    participant D as db.py
    participant P as PostgreSQL

    C->>F: POST /api/users {"name":"Alice"}
    F->>F: validate JSON + name
    alt thiếu "name"
        F-->>C: 400 {"error":"Missing 'name' field"}
    else hợp lệ
        F->>D: create_user("Alice")
        D->>P: INSERT INTO users (name) VALUES (%s) RETURNING id
        P-->>D: id = 1
        D-->>F: 1
        F-->>C: 201 {"id":1,"name":"Alice"}
    end
```

## 3. Dependency graph (module nào phụ thuộc module nào)

```mermaid
graph LR
    APP[app.py] --> DB[db.py]
    APP --> FL[flask]
    DB --> PG2[psycopg2]
    DB --> OS[os]
    TEST[test_app.py] --> APP
    TEST --> DB
    TEST --> PT[pytest]
```

## 4. Bảng endpoints chi tiết

| Method | Route | Hàm trong app.py | Gọi db.py | Thành công | Lỗi |
|---|---|---|---|---|---|
| GET | `/` | `home` | — | 200 text | — |
| GET | `/api/hello` | `hello` | — | 200 JSON | — |
| GET | `/api/users` | `list_users` | `list_users` | 200 list | — |
| POST | `/api/users` | `create_user` | `create_user` | 201 | 400 |
| PUT | `/api/users/:id` | `update_user` | `update_user` | 200 | 400, 404 |
| DELETE | `/api/users/:id` | `delete_user` | `delete_user` | 200 | 404 |

## 5. Cấu trúc project

```
capstone-flask/
├── app.py          # routes (tầng HTTP)
├── db.py           # tầng database (PostgreSQL)
├── test_app.py     # pytest tests
├── render.yaml     # blueprint deploy (web + Postgres)
├── Procfile        # gunicorn app:app
├── requirements.txt
├── AGENTS.md
└── README.md / DEPLOY.md / ARCHITECTURE.md (file này)
```

---

## 💡 Mẹo: tự sinh sơ đồ bằng AI (Cline/DSH)

Chỉ cần hỏi AI:
> "Đọc project capstone-flask, vẽ sơ đồ kiến trúc bằng Mermaid:
> - flowchart endpoints → functions → database
> - sequence diagram cho POST /api/users"

AI sẽ tự phân tích code và tạo Mermaid như trên — bạn chỉ cần paste vào file `.md` và preview!
