#!/usr/bin/env python3
"""Import required modules"""
import redis
from uuid import uuid4
from typing import Union, Callable
import functools


class Cache:
    """Cache class"""

    def __init__(self):
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()
        self._counts = {}

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store data with certain key"""
        return super().store(data)

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from Redis storage."""
        return super().get(key, fn)

    def get_str(self, key: str) -> Union[str, bytes]:
        """Method to retrieve a value as a string"""
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Method to retrieve a value as an integer"""
        return self.get(key, lambda x: int(x))


def count_calls(func: Callable) -> Callable:
    """Decorator that increments the call count for a method."""

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        key = f"{self.__class__.__name__}.{func.__qualname__}"

        if key not in self._counts:
            self._counts[key] = 0

        old_value = func(self, *args, **kwargs)
        new_count = self._counts[key] + 1
        self._counts[key] = new_count

        return old_value

    wrapper.__doc__ = f"Counting calls for {func.__qualname__}"
    return wrapper


Cache.store = count_calls(Cache.store)
