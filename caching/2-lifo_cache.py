#!/usr/bin/env python3
"""
Module that defines a LIFO caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache caching system using LIFO algorithm.
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO replacement policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
