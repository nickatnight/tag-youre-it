import logging
from typing import AsyncIterator, Optional

from asyncpraw import Reddit
from asyncpraw.models import Message

from tag_youre_it.core.clients import DbClient
from tag_youre_it.core.const import ReplyEnum, TagEnum
from tag_youre_it.services import AbstractStream


logger = logging.getLogger(__name__)


class InboxStreamService(AbstractStream[Message]):
    async def pre_flight_check(self, db_client: DbClient, obj: Message) -> bool:
        author = obj.author
        await author.load()  # Re-fetches the object

        author_name = author.name
        logger.info(f"Reading mention from [{author_name}]")

        if obj.was_comment is False:
            # user previously opted out and wants to play again
            enable_check = TagEnum.ENABLE_PHRASE == obj.subject.title().lower()
            opted_out_check1 = author_name in await db_client.player.list_opted_out()

            if all([enable_check, opted_out_check1]):
                await db_client.player.set_opted_out(author.id, False)
                await obj.reply(ReplyEnum.welcome_back(author=author_name))

            # user wants to opt of playing
            disable_check = TagEnum.DISABLE_PHRASE == obj.subject.title().lower()
            opted_out_check2 = author_name not in db_client.player.list_opted_out()

            if all([disable_check, opted_out_check2]):
                await db_client.player.set_opted_out(author.id, True)
                await obj.reply(ReplyEnum.user_opts_out_info(author=author_name))

            await obj.mark_read()
            return False

        mention_subreddit = obj.subreddit
        await mention_subreddit.load()

        # check if mention is not from the streams subreddit
        if mention_subreddit.display_name != self.subreddit_name:
            logger.warning(
                f"SubReddit[{self.subreddit_name}] does not match mention "
                f"SubReddit: {mention_subreddit.display_name}...skipping"
            )
            return False

        return True

    async def process(
        self, db_client: DbClient, obj: Message, game_id: Optional[str]
    ) -> Optional[str]:

        if TagEnum.KEY in obj.body.lower():
            mention_author = obj.author  # the person tagging
            await mention_author.load()

            parent = await obj.parent()
            await parent.load()

            author = parent.author  # the person who got tagged
            await author.load()

            # prevent user from tagging self
            if author.id == mention_author.id:
                logger.info(f"Player [{mention_author}] tried tagging themself")
                await obj.reply(ReplyEnum.unable_to_tag_self())
                return game_id

            if author.name in await db_client.player.list_opted_out():
                logger.info(f"Player [{author.name}] has opted out.")
                await obj.reply(ReplyEnum.user_opts_out(author=author.name))
                return

            # a game is currently being played
            # if game_id is not None:
            #     player = db_client.player.by_reddit_id(mention_author.id)

            # if not player.is_it:

            #     # TODO: get user who is currently it
            #     await obj.reply(CURRENT_ACTIVE_GAME.format(author=author.name))
            #     return inserted_game

            # game = self.db_client.game.create()
            # game_data = GameSchema()
            # inserted_game = await db["game_collection"].insert_one(game_data.dict())
            # g = await db["game_collection"].find_one({"_id": ObjectId(inserted_game.inserted_id)})
            # players = g.get("players").copy()

            # await parent.reply(COMMENT_REPLY_YOURE_IT.format(author=obj.author.name))

            # # upsert
            # await self.db_client.player.insert(author)

            # await self.db_client.game.add_player()

    def stream(self, reddit: Reddit) -> AsyncIterator[Message]:
        return reddit.inbox.stream()
