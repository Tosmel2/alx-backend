#!/usr/bin/env python3
"""basic chache"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    """

    def put(self, key, item):
        """
        put
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get
        """
        if key:
            return self.cache_data.get(key, None)
