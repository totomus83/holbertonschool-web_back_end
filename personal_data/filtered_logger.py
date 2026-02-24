#!/usr/bin/env python3
"""
Module for filtering sensitive fields from log messages.
"""

from dataclasses import fields
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Return the log message with specified fields obfuscated.
    """
    pattern = rf"({'|'.join(fields)})=([^{separator}]+)"
    return re.sub(pattern, r"\1=" + redaction, message)
