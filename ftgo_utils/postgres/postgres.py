import contextlib
from typing import Optional, Dict, Type
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from .exceptions import PostgresConnectionError, PostgresSessionCreationError

class AsyncPostgres:
    _instances = {}
    _locks = {}

    def __new__(cls, url: str):
        if url not in cls._locks:
            cls._locks[url] = asyncio.Lock()
        return cls._instances.setdefault(url, super(AsyncPostgres, cls).__new__(cls))

    def __init__(self, url: str):
        if not hasattr(self, 'initialized'):
            self.url = url
            self.session = None
            self.initialized = True

    def __init__(self, url: str, echo: bool = False, expire_on_commit: bool = False):
        self.url = url
        self.echo = echo
        self.expire_on_commit = expire_on_commit
        
        self._async_engine: AsyncEngine = self._create_async_engine()
        self._async_session_maker = self._create_async_session_maker()

    
    def _create_async_engine(self) -> AsyncEngine:
        return create_async_engine(
            url=self.url,
            echo=self.echo,
        )

    def _create_async_session_maker(self) -> async_sessionmaker:
        return async_sessionmaker(
            bind=self._async_engine,
            expire_on_commit=self.expire_on_commit,
            class_=AsyncSession,
        )

    @contextlib.asynccontextmanager
    async def get_or_create_session(self):
        session = self._async_session_maker()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise PostgresSessionCreationError(url=self.url, message=str(e.args[0]))
        finally:
            await session.close()

    async def connect(self) -> None:
        try:
            async with self._async_engine.begin() as connection:
                await connection.run_sync(lambda conn: None)
        except Exception as e:
            raise PostgresConnectionError(url=self.url, message=str(e.args[0]))

    async def disconnect(self) -> None:
        await self._async_engine.dispose()
