import logging
from typing import Optional

from asyncpraw.models import Subreddit as PrawSubReddit
from sqlmodel import select

from tag_youre_it.models import SubReddit
from tag_youre_it.repository import AbstractRepository
from tag_youre_it.schemas.subreddit import ISubRedditCreate, ISubRedditUpdate


logger: logging.Logger = logging.getLogger(__name__)


class SubRedditRepository(AbstractRepository[SubReddit, ISubRedditCreate, ISubRedditUpdate]):
    model = SubReddit

    async def get_or_create(self, reddit_obj: PrawSubReddit) -> SubReddit:
        statement = select(self.model).where(self.model.name == reddit_obj.name)
        result = await self.db.execute(statement)
        instance: Optional[SubReddit] = result.scalar_one_or_none()

        if instance:
            return instance

        subreddit_obj = ISubRedditCreate(
            name=reddit_obj.name,
            sub_id=reddit_obj.id,
            display_name=reddit_obj.display_name,
        )

        instance = await self.insert(subreddit_obj)
        return instance
