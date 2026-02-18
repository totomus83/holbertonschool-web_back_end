#!/usr/bin/env python3
"""
0-basic_cache module: basic caching system without limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache system that stores key-value.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.

        If key or item is None, does nothing.
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value associated with the key, or None if key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
