import logging

from sqlmodel import select

from tag_youre_it.models import SubReddit
from tag_youre_it.repository import AbstractRepository
from tag_youre_it.schemas.subreddit import ISubRedditCreate, ISubRedditUpdate


logger: logging.Logger = logging.getLogger(__name__)


class SubRedditRepository(AbstractRepository[SubReddit, ISubRedditCreate, ISubRedditUpdate]):
    model = SubReddit

    async def get_or_create(
        self, obj: ISubRedditCreate, add: bool = True, flush: bool = True, commit: bool = False
    ) -> SubReddit:
        statement = select(self.model).where(self.model.name == obj.name)
        result = await self.db.execute(statement)
        instance = result.scalar_one_or_none()

        if instance:
            return instance

        else:
            instance = self.model.from_orm(obj)

        # You'll usually want to add to the self.db
        if add:
            self.db.add(instance)

        # Navigate these with caution
        if add and commit:
            try:
                await self.db.commit()
            except Exception as exc:
                logger.error(exc)
                self.db.rollback()

        elif add and flush:
            await self.db.flush()

        return instance
