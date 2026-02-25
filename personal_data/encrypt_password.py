#!/usr/bin/env python3
"""
Module to hash passwords using bcrypt
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password with a random salt using bcrypt."""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
