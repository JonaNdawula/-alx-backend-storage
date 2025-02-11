#!/usr/bin/env python3
"""
This moddule contains the count_callls function
the cache_result and get_page functions
"""
import functools
import redis
import requests
from typing import Callable

_redis = redis.Redis()


def count_calls(method: Callable) -> callable:
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        key = f"count:{url}"
        _redis.incr(key)
        return method(url)
    return wrapper


def cache_result(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        key = f"cache:{url}"
        cached_result = _redis.get(key)
        if cached_result is not None:
            return cached_result.decode('utf-8')
        result = method(url)
        _redis.setex(key, 10, result)
        return result
    return wrapper


@count_calls
@cache_result
def get_page(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"HTTP request failed with status"
            f"code {response.status_code}")
    return response.text
