#!/usr/bin/python3
"""LIFOCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """
        put
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                del self.cache_data[self.last_key]
                print(f'DISCARD: {self.last_key}')
            self.last_key = key

    def get(self, key):
        """
        get
        """
        if key:
            return self.cache_data.get(key, None)
