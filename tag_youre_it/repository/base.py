from abc import ABCMeta
from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class AbstractRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """interface for interacting with database"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    async def insert(self, obj_in: Type[CreateSchemaType]) -> ModelType:
        db_obj = self.model.from_orm(obj_in)

        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj
