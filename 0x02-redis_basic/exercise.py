#!/usr/bin/env python3
"""Import required modules"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Method to count calls and execute the original method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Method to track the call history of a method."""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result

    return wrapper


def replay(method: Callable):
    """Method to display the history of inputs and outputs for a method."""
    redis_instance = redis.Redis()

    method_name = method.__qualname__

    input_key = method_name + ":inputs"
    output_key = method_name + ":outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for i, (input_args, output) in enumerate(zip(inputs, outputs), 1):
        print(
            f"{method_name}(*{input_args.decode('utf-8')})
            -> {output.decode('utf-8')}")


class Cache:
    """Cache class"""

    def __init__(self):
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
