from abc import ABC, abstractmethod
from typing import AsyncIterator, Generic, List, Optional, Type, TypeVar, Union

import asyncpraw
from asyncpraw.models.base import AsyncPRAWBase


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")


class AbstractStream(ABC):
    """interface to stream different Reddit objects Comments, Messaging, etc"""

    @abstractmethod
    async def pre_flight_check(self, db_client: Type[DbType], obj: AsyncPRAWBase) -> bool:
        ...

    @abstractmethod
    async def process(
        self, db_client: Type[DbType], obj: AsyncPRAWBase, game_id: Optional[str]
    ) -> Optional[str]:
        ...

    @abstractmethod
    def stream(
        self, reddit: asyncpraw.Reddit
    ) -> AsyncIterator[Union["asyncpraw.models.Comment", "asyncpraw.models.Message"]]:
        ...


class AbstractRepository(Generic[ModelType, SchemaType], ABC):
    """interface for interacting with database"""

    model: Type[ModelType]

    @abstractmethod
    async def insert(self, obj_in: SchemaType) -> ModelType:
        ...

    @abstractmethod
    async def all(self) -> List[Type[ModelType]]:
        ...

    @abstractmethod
    async def one(self, field: str, value: str) -> Type[ModelType]:
        ...

    @abstractmethod
    async def update(self, *args, **kwargs) -> ModelType:
        ...
