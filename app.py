# app.py
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory "database"
users = {}
next_id = 1

def get_next_id():
    global next_id
    nid = next_id
    next_id += 1
    return nid

@app.route("/users", methods=["GET"])
def list_users():
    # returns list of users
    return jsonify(list(users.values())), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    user_id = get_next_id()
    user = {"id": user_id, "name": data["name"], "email": data.get("email")}
    users[user_id] = user
    return jsonify(user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    user = users[user_id]
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user.get("email"))
    users[user_id] = user
    return jsonify(user), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"deleted": deleted}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
