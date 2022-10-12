import logging
from abc import ABCMeta
from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


logger: logging.Logger = logging.getLogger(__name__)


class AbstractRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """interface for interacting with database"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    async def insert(
        self,
        obj_in: CreateSchemaType,
        add: bool = True,
        flush: bool = True,
        commit: bool = False,
    ) -> ModelType:
        db_obj = self.model.from_orm(obj_in)

        # You'll usually want to add to the self.db
        if add:
            self.db.add(db_obj)

        # Navigate these with caution
        if add and commit:
            try:
                await self.db.commit()
            except Exception as exc:
                logger.error(exc)
                await self.db.rollback()

        elif add and flush:
            await self.db.flush()

        return db_obj
