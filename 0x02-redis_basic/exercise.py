#!/usr/bin/env python3
"""
This module contains redis db
"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    function counts calls
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    function displays call history
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """
    function replays
    """
    inputs_key = f"{method.__qualname__}:inputs}"
    outputs_key = f"{method.__qualname__}:outputs"
    count_key = method.__qualname__
    count = method.__self__._redis.get(count_key)
    print(f"{method.__qualname} was called {count.decode('utf-8')} times:")
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = methods.__self__._redis.lrange(outputs_key, 0, -1)
    for inp, out in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{inp.decode('utf-8'}) -> "
            f"{out.decode('utf-8')}")


class Cache:
    def __init__(self):
        """
        Is an instance of Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Function takes data arg and returns String
        """
        random_key = str(uuid.uuid4())
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif isinstance(data, int) or isinstance(data, float):
            data = str(data).encode('utf-8')
        elif isinstance(data, bytes):
            pass
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, func: Optional[Callable] = None):
        """
        Gets data stored in redis
        """
        data = self._redis.get(key)
        if data is not None and func:
            if func != int:
                data = func(data.decode('utf-8'))
            else:
                data = func(int(data))
        return data

    def get_str(self, key: str) -> str:
        """
        Gets a string
        """
        return self.get(key, func=lambda x: x)

    def get_int(self, key: str) -> int:
        """
        Gets an int
        """
        return self.get(key, func=int)
