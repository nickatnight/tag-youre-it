from uuid import UUID

from tag_youre_it.models.subreddit import SubRedditBase


class ISubRedditCreate(SubRedditBase):
    pass


class ISubRedditRead(SubRedditBase):
    id: UUID


class ISubRedditUpdate(SubRedditBase):
    pass
