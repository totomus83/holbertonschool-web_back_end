#!/usr/bin/env python3
"""
This module provides a Cache class that uses Redis to store
and retrieve data with type conversion support.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any


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
        Args: The data to store.
        Returns: The generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Any]] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it.
        Args:The key to retrieve.
        Returns:The retrieved and optionally converted data,
        or None if key does not exist.
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.
        Args: The key to retrieve.
        Returns: The decoded string value or None.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.
        Args: key (str): The key to retrieve.
        Returns: Optional[int]: The integer value or None.
        """
        return self.get(key, fn=int)
