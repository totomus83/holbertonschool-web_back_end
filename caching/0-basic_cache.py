#!/usr/bin/env python3
"""
This module defines a simple dictionary-based cache.
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, return nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache, return nothing.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
