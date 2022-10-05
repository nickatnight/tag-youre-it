from abc import ABCMeta, abstractmethod
from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class AbstractRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """interface for interacting with database"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod
    async def insert(self, obj_in: Type[CreateSchemaType]) -> Type[ModelType]:
        db_obj = self.model.from_orm(obj_in)  # type: ignore

        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj
