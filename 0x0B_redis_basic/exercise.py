#!/usr/bin/env python3
"""
This module provides a Cache class that uses Redis to store data
with randomly generated keys.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class that interacts with a Redis database to store
    and retrieve data using randomly generated keys.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance by creating a Redis client
        and flushing the database to start with a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store input data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
