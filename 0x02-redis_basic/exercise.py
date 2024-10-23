#!/usr/bin/env python3
"""Import required modules"""
import redis
from uuid import uuid4
import json


class Cache:
    """Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """Method to store data with certain key"""
        key = str(uuid4())
        json_data = json.dumps(data)
        self.redis.set(key, json_data)
        return key
