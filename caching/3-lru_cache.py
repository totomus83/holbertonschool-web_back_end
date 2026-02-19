#!/usr/bin/env python3
"""
This module implements an LRU caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and implements
    a caching system using the Least Recently Used policy.
    """

    def __init__(self):
        """
        Initialize the LRU cache and track usage order.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU caching system.
        If cache exceeds MAX_ITEMS, discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            self.cache_data[key] = item
            self.usage_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """
        Retrieve an item by key and update its usage.
        Returns None if key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
