#!/usr/bin/env python3
"""Module that defines a FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching system using FIFO algorithm."""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache using FIFO."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache, return nothing."""
        if key is None:
            return None
        return self.cache_data.get(key)
