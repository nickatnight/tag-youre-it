import logging

from emoji import emojize


# from tag_youre_it.core.clients import DbClient
# from tag_youre_it.schemas.subreddit import ISubRedditCreate


logger = logging.getLogger(__name__)


def _emojize(s: str) -> str:
    return emojize(s, variant="emoji_type", language="alias")


# async def check_valid_subreddit(db_client: DbClient, obj: Message, subreddit_name: str):
#     mention_subreddit = obj.subreddit
#     await mention_subreddit.load()

#     subreddit_obj = ISubRedditCreate(
#         name=mention_subreddit.name,
#         sub_id=mention_subreddit.id,
#         display_name=mention_subreddit.display_name,
#     )
#     _ = await db_client.subreddit.get_or_create(subreddit_obj)

#     # check if mention is not from streams defined subreddit
#     if mention_subreddit.display_name != subreddit_name:
#         logger.warning(
#             f"SubReddit[{subreddit_name}] does not match mention "
#             f"SubReddit: {mention_subreddit.display_name}"
#         )
#         return False
