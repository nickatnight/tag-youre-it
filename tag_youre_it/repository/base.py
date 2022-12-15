import logging
from abc import ABCMeta
from typing import Generic, Optional, Type, TypeVar, Union
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select


DbType = TypeVar("DbType")

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


logger: logging.Logger = logging.getLogger(__name__)


class AbstractRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """interface for database operations"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    async def insert(
        self,
        obj_in: CreateSchemaType,
        add: Optional[bool] = True,
        flush: Optional[bool] = True,
        commit: Optional[bool] = True,
    ) -> ModelType:
        db_obj = self.model.from_orm(obj_in)

        logger.info(f"Inserting new object[{db_obj}]")

        # You'll usually want to add to the self.db
        if add:
            self.db.add(db_obj)

        # Navigate these with caution
        if add and commit:
            try:
                await self.db.commit()
                await self.db.refresh(db_obj)
            except Exception as exc:
                logger.error(exc)
                await self.db.rollback()

        elif add and flush:
            await self.db.flush()

        return db_obj

    async def get(self, ref_id: Union[UUID, str]) -> ModelType:
        logger.info(f"Fetching [{str(self.model.__class__)}] object by [{ref_id}]")

        query = select(self.model).where(getattr(self.model, "ref_id") == ref_id)
        response = await self.db.execute(query)
        scalar: Optional[ModelType] = response.scalar_one_or_none()

        if not scalar:
            raise Exception("no object")
        return scalar

    async def update(
        self,
        obj_current: ModelType,
        obj_in: Union[UpdateSchemaType, ModelType],
    ) -> ModelType:
        update_data = obj_in.dict(
            exclude_unset=True
        )  # This tells Pydantic to not include the values that were not sent

        logger.info(f"Updating [{self.model.__class__}] object with [{update_data}]")

        for k, v in update_data.items():
            setattr(obj_current, k, v)

        self.db.add(obj_current)
        await self.db.commit()
        await self.db.refresh(obj_current)

        return obj_current
