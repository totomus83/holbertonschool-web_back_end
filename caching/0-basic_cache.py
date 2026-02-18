#!/usr/bin/env python3
"""Module that defines a BasicCache caching system."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that stores key-value pairs without eviction policy."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Does nothing if key or item is None.
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Returns None if the key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
