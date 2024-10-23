#!/usr/bin/env python3
"""Import required modules"""
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    """Cache class"""

    def __init__(self):
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store data with certain key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from Redis storage."""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Union[str, bytes]:
        """Method to retrieve a value as a string"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Method to retrieve a value as an integer"""
        return self.get(key, lambda x: int(x))
