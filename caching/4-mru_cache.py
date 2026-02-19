#!/usr/bin/env python3
"""Module that defines a MRUCache caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that implements Most Recently Used caching."""

    def __init__(self):
        """Initialize the cache and tracking structure."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache using MRU algorithm.

        Does nothing if key or item is None.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache.

        Returns None if key is None or does not exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
