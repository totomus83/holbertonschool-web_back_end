#!/usr/bin/env python3
""" Auth module """
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class """


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if authentication is required
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


    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now
        """
        return None


    def session_cookie(self, request=None) -> str:
        """
        Returns the cookie value from a request
        The cookie name is defined by environment variable SESSION_NAME
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
