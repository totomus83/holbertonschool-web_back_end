#!/usr/bin/env python3
"""
This module provides a Cache class that uses Redis to store
data, count method calls, and keep history of inputs/outputs.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called
    and stores the count in Redis using the method's qualified name.
    Args: The method to decorate.
    Returns: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count before
        executing the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs
    for a function in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(input_key, str(args))

        # Execute the original function
        result = method(self, *args, **kwargs)

        # Store output
        self._redis.rpush(output_key, result)

        return result

    return wrapper


class Cache:
    """
    Cache class that interacts with Redis to store data and
    track method usage history.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance by creating a Redis client
        and flushing the database to start with a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

        if fn:
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
