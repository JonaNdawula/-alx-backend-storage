#!/usr/bin/env python3
"""
This module contains redis db
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif isinstance(data, int) or isinstance(data, float):
            data = str(data).encode('utf-8')
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, func: Optional[Callable] = None):
        data = self._redis.get(key)
        if data is not None:
            data = data.decode('utf-8')
            if func:
                data = func(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, func=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, func=int)
