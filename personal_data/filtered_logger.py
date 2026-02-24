#!/usr/bin/env python3
"""
This module defines the filter_datum function that will obfuscate
the content of a string
"""

import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Return the log message with specified fields obfuscated.
    """
    
    pattern = rf"({'|'.join(fields)})=([^{separator}]+)"
    return re.sub(pattern, r"\1=" + redaction, message)

class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class that obfuscates specified fields.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the record and redact sensitive fields.
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)

def get_logger() -> logging.Logger:
    """Return a logger that redacts PII fields."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger
