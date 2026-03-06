#!/usr/bin/env python3
"""Authentication module for handling API request authorization."""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class used to manage authentication logic for the API."""

    # Méthode __init__
    def __init__(self):
        """
        Méthode d'initialisation de l'objet Auth
        """
        pass

    # Méthode require_path
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if a given path requires authentication.
        This method checks if the requested path is part of the list
        of excluded paths that do not require authentication.
        """

        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True


        if not path.endswith("/"):
            path += "/"

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    # Méthode authorization_header
    def authorization_header(self, request=None) -> str:
        """
        Retrieve the Authorization header from the request object.

        This method extracts the Authorization header if it exists
        in the incoming HTTP request.
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    # Méthode current_user
    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method is intended to identify and return the user
        based on the authentication information contained in the request.
        Currently, this method is not implemented.
        """
        pass
    
    # Méthode session_cookie
    def session_cookie(self, request=None) -> str:
        """
        Retrieve the session cookie value from the request.

        The cookie name is defined by the environment variable
        SESSION_NAME. This method extracts the corresponding
        cookie value from the incoming request.
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
