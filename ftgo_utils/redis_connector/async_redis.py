import contextlib
from typing import Optional
import asyncio
import redis.asyncio as redis

from .exceptions import RedisConnectionError, RedisSessionCreationError

class AsyncRedis():
    _instances = {}
    _locks = {}

    def __new__(cls, url: str):
        if url not in cls._locks:
            cls._locks[url] = asyncio.Lock()
        return cls._instances.setdefault(url, super(AsyncRedis, cls).__new__(cls))

    def __init__(self, url: str):
        if not hasattr(self, 'initialized'):
            self.url = url
            self.session = None
            self.initialized = True

    @contextlib.asynccontextmanager
    async def get_or_create_session(self) -> redis.Redis:
        try:
            if self.session is None:
                await self.connect()
            yield self.session
        except Exception as e:
            raise RedisSessionCreationError(url=self.url) from e

    async def connect(self) -> None:
        async with self._locks[self.url]:
            if self.session is None:
                try:
                    self.session = redis.Redis.from_url(self.url, decode_responses=True)
                    await self.session.ping()
                except Exception as e:
                    raise RedisConnectionError(utl=self.url, message=str(e.args[0]))

    async def disconnect(self) -> None:
        async with self._locks[self.url]:
            if self.session:
                await self.session.close()
                self.session = None

