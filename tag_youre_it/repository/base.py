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
    """interface for interacting with database"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    async def insert(
        self,
        obj_in: CreateSchemaType,
        add: Optional[bool] = True,
        flush: Optional[bool] = True,
        commit: Optional[bool] = True,
        from_orm: Optional[bool] = True,
    ) -> ModelType:
        # TODO: remove "from_orm" flag and remove below condition
        db_obj = obj_in
        if from_orm:
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

    async def get(self, ref_id: Union[UUID, str]) -> Optional[ModelType]:
        query = select(self.model).where(self.model.ref_id == ref_id)
        response = await self.db.execute(query)

        return response.scalar_one_or_none()

    async def update(
        self,
        obj_current: ModelType,
        obj_in: Union[UpdateSchemaType, ModelType],
    ):
        update_data = obj_in.dict(
            exclude_unset=True
        )  # This tells Pydantic to not include the values that were not sent

        logger.info(f"Updating====data: {update_data}")
        logger.info(f"Updating====obj_current-pre: {obj_current}")
        for field in update_data:
            setattr(obj_current, field, update_data[field])

        self.db.add(obj_current)
        await self.db.commit()
        await self.db.refresh(obj_current)

        logger.info(f"Updating====obj_current-post: {obj_current}")
        return obj_current
