#!/usr/bin/python3
"""Module that implements a simple RESTful API using Flask."""

from flask import Flask, jsonify, request


# Create the Flask application instance.
app = Flask(__name__)

# Store users in memory.
# The username is the key, and the full user dictionary is the value.
users = {}


@app.route("/")
def home():
    """Return a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return the list of usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return a simple status message."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return a user object if the username exists."""
    if username in users:
        return jsonify(users[username])

    # Return a JSON error with a 404 status code if user is not found.
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON data."""
    # Read JSON data from the request body.
    # silent=True prevents Flask from raising an error on invalid JSON.
    data = request.get_json(silent=True)

    # If the body is not valid JSON, return a 400 error.
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # A username is required to store the user in the dictionary.
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Prevent replacing an existing user.
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the complete user object, not only the username.
    users[username] = data

    # Return a confirmation message and the added user with status 201.
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    # Run the Flask development server.
    app.run()
