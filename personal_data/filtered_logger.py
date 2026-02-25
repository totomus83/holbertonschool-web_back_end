#!/usr/bin/env python3

"""Module for filtering sensitive fields from log messages
and connecting to a secure MySQL database."""

import os
import re



PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                separator: str) -> str:
    """Return the log message with specified fields obfuscated."""
    pattern = rf"({'|'.join(fields)})=([^{separator}]+)"
    return re.sub(pattern, r"\1=" + redaction, message)
