#!/usr/bin/env python3
"""
Route module for the API.

This module initializes the Flask application, registers API routes,
configures CORS, and handles authentication setup depending on the
AUTH_TYPE environment variable.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handle 404 Not Found errors.

    This function is triggered when a client tries to access a route
    that does not exist in the API.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handle 401 Unauthorized errors.

    This function is called when authentication credentials are missing
    or invalid for a request that requires authentication.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handle 403 Forbidden errors.

    This error occurs when the user is authenticated but does not
    have permission to access the requested resource.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """
    Validate incoming requests before they reach the route handlers.

    This function runs before every request and ensures that
    authentication requirements are respected depending on the
    configured authentication type.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)
    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)
    request.current_user = current_user


if __name__ == "__main__":
    """
    Application entry point.

    This block starts the Flask development server using
    environment variables to configure the host and port.
    Default values are used if the variables are not set.
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
