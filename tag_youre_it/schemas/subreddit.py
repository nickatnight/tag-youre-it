from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.subreddit import SubRedditBase


class ISubRedditBase(SubRedditBase):
    pass


class ISubRedditCreate(ISubRedditBase):
    pass


class ISubRedditRead(ISubRedditBase):
    ref_id: UUID


@optional
class ISubRedditUpdate(ISubRedditBase):
    pass
