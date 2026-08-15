"""Capstone Flask API - demo project for vibe coding.

Endpoints:
    GET  /                  -> text homepage
    GET  /api/hello         -> JSON {"message": "hello", "visits": n} + visitor counter
    GET  /api/users         -> list of users (in-memory)
    POST /api/users         -> create user {"name": "..."} -> 201 or 400
    DELETE /api/users/<id>  -> delete user by id -> 200 or 404
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data (no database - simple on purpose for learning)
users = []
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
    return jsonify(users)


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not data or not data.get("name"):
        return jsonify({"error": "Missing 'name' field"}), 400
    user = {"id": len(users) + 1, "name": data["name"]}
    users.append(user)
    return jsonify(user), 201


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return jsonify({"message": f"Deleted user {user_id}"}), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
