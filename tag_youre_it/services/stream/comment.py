from asyncpraw.models import Comment

from tag_youre_it.services import AbstractStream


class CommentStreamService(AbstractStream[Comment]):
    pass
