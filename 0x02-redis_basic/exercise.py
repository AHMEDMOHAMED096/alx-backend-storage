#!/usr/bin/env python3
"""Import required modules"""
import redis
from uuid import uuid4


class Cache:
    """Cache class"""

    def __init__(self):
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """Method to store data with certain key"""
        key = str(uuid4())
        self.redis.set(key, data)
        return key
