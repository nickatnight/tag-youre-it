from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.subreddit import SubRedditBase


class ISubRedditCreate(SubRedditBase):
    pass


class ISubRedditRead(SubRedditBase):
    ref_id: UUID


@optional
class ISubRedditUpdate(SubRedditBase):
    pass
