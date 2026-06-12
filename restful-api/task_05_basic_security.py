#!/usr/bin/python3
"""Module that implements API security with Basic Auth and JWT."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from werkzeug.security import generate_password_hash, check_password_hash


# Create the Flask application.
app = Flask(__name__)

# Secret key used to sign and verify JWT tokens.
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"

# Create Basic Auth and JWT managers.
auth = HTTPBasicAuth()
jwt = JWTManager(app)


# In-memory users database.
# Passwords are hashed, not stored in plain text.
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication."""
    user = users.get(username)

    # Check that the user exists and that the password is correct.
    if user and check_password_hash(user["password"], password):
        return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message if Basic Authentication succeeds."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT access token."""
    data = request.get_json(silent=True)

    # If the body is missing or is not valid JSON.
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    # Check if the user exists and if the password is correct.
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create a JWT token containing the username as identity.
    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message if JWT authentication succeeds."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Allow access only to users with the admin role."""
    current_user = get_jwt_identity()
    user = users.get(current_user)

    # The user must exist and must have the admin role.
    if user and user["role"] == "admin":
        return "Admin Access: Granted"

    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # Run the Flask development server.
    app.run()
