#!/usr/bin/python3

from flask import Flask, jsonify, request, abort  # type: ignore

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Returns the list of usernames.

    Returns:
        Response: JSON response containing list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns status 'OK'.

    Returns:
        str: Status message.
    """
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieves user details by username.

    Args:
        username (str): The username to retrieve.

    Returns:
        Response: JSON response containing user details.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username]
    user["username"] = username

    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user.

    Returns:
        Response: JSON response confirming user addition.
    """
    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    output = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
