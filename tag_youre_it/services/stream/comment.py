from asyncpraw.models import Comment

from tag_youre_it.services.stream.base import AbstractStream


class CommentStreamService(AbstractStream[Comment]):
    pass
