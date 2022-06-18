#!/usr/bin/python3
""" 5. LFU Caching
"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching


class HeapItemStatus(Enum):
    """ HeapItemStatus
    """
    ACTIVE = 1
    INACTIVE = 2


class LFUCache(BaseCaching):
    """ LFUCache """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.heap = []
        self.map = {}
        self.counter = count()

    def put(self, key, item):
        """ put """
        if key and item:
            if key in self.cache_data:
                self.rehydrate(key)
            else:
                if self.is_full():
                    self.evict()
                self.add_to_heap(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get """
        if key in self.cache_data:
            self.rehydrate(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ check number of items  """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ evict """
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.ACTIVE:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

    def rehydrate(self, key):
        """ Marks current item as inactive and reinserts updated count back
        into heap.
        """
        entry = self.map[key]
        entry[-1] = HeapItemStatus.INACTIVE
        self.add_to_heap(key, entry[0])

    def add_to_heap(self, key, count=0):
        """ Adds a new entry into heap.
        """
        entry = [1 + count, next(self.counter), key, HeapItemStatus.ACTIVE]
        self.map[key] = entry
        heappush(self.heap, entry)
