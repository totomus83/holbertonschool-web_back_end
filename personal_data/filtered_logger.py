#!/usr/bin/env python3
"""
Module for filtering sensitive fields from log messages
and connecting to a secure MySQL database.
"""


import logging
import os
import mysql.connector
from typing import List
from filtered_logger import RedactingFormatter, get_logger, PII_FIELDS, get_db


def main() -> None:
    """Retrieve all rows in users table and display filtered log messages."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    formatter = RedactingFormatter(PII_FIELDS)

    for row in cursor:
        # Construct a log message in key=value; key2=value2; ... format
        message = "; ".join(f"{key}={value}" for key, value in row.items()) + ";"
        log_record = logging.LogRecord(
            name=logger.name,
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg=message,
            args=None,
            exc_info=None,
        )
        print(formatter.format(log_record))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
