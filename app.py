"""Capstone Flask API - demo project for vibe coding (SQLite).

Endpoints:
    GET  /                  -> text homepage
    GET  /api/hello         -> JSON {"message": "hello", "visits": n} + visitor counter
    GET  /api/users         -> list of users (from SQLite)
    POST /api/users         -> create user {"name": "..."} -> 201 or 400
    DELETE /api/users/<id>  -> delete user by id -> 200 or 404
"""

from flask import Flask, jsonify, request

import db

app = Flask(__name__)

# Tao bang users (neu chua co). Neu DATABASE_URL chua san (VD: moi push,
# chua Apply blueprint), chi canh bao, KHONG crash de app van khoi dong.
try:
    db.init_db()
except Exception as exc:
    print(f"WARNING: khong the khoi tao database: {exc}")

visit_count = 0


@app.route("/")
def home():
    return "Hello from Cline Vibe Coding project! Try GET /api/hello"


@app.route("/api/hello")
def hello():
    global visit_count
    visit_count += 1
    return jsonify({"message": "hello", "visits": visit_count})


@app.route("/api/users", methods=["GET"])
def list_users():
    return jsonify(db.list_users())


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return jsonify({"error": "Missing 'name' field"}), 400
    user_id = db.create_user(data["name"])
    return jsonify({"id": user_id, "name": data["name"]}), 201


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    deleted = db.delete_user(user_id)
    if deleted == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": f"Deleted user {user_id}"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)

