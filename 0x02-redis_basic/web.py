#!/usr/bin/env python3
"""Import required modules"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_instance = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decorator to cache the result of a function in Redis."""

    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper to cache page content and count URL access."""
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        cached_page = redis_instance.get(cache_key)
        if cached_page:
            return cached_page.decode("utf-8")

        redis_instance.incr(count_key)
        page_content = method(url)
        redis_instance.setex(cache_key, 10, page_content)

        return page_content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and returns it."""
    response = requests.get(url)
    return response.text
