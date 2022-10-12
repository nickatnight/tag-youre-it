import logging
from typing import AsyncIterator, Optional

from asyncpraw import Reddit
from asyncpraw.models import Message, Redditor
from asyncpraw.models import Subreddit as PrawSubReddit

from tag_youre_it.core.clients import DbClient
from tag_youre_it.core.config import settings
from tag_youre_it.core.const import ReplyEnum, TagEnum
from tag_youre_it.models import Game, Player, SubReddit
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
            opted_out_check2 = author_name not in await db_client.player.list_opted_out()

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
            mention_author: Redditor = obj.author  # the person tagging
            await mention_author.load()
            tagger: Player = await db_client.player.get_or_create(mention_author)

            parent = await obj.parent()
            await parent.load()
            author: Redditor = parent.author  # the person who got tagged
            await author.load()
            tagee: Player = await db_client.player.get_or_create(author)

            # prevent tagger from tagging bot
            if tagee.username == settings.USERNAME:
                logger.info(f"Player [{tagger.username}] tried tagging bot")
                await obj.reply(ReplyEnum.unable_to_tag_bot())
                return game_id

            # prevent tagger from tagging self
            if tagee.reddit_id == tagger.reddit_id:
                logger.info(f"Player [{tagger.username}] tried tagging themself")
                await obj.reply(ReplyEnum.unable_to_tag_self())
                return game_id

            # prevent an opted out user from participating in game
            if tagee.username in await db_client.player.list_opted_out():
                logger.info(f"Player [{tagee.username}] has opted out.")
                await obj.reply(ReplyEnum.user_opts_out(author=tagee.username))
                return game_id

            # a game is currently being played
            # if game_id is not None:
            #     player = db_client.player.by_reddit_id(mention_author.id)

            # if not player.is_it:

            #     # TODO: get user who is currently it
            #     await obj.reply(CURRENT_ACTIVE_GAME.format(author=author.name))
            #     return inserted_game

            # there is no active game, so start a new one
            mention_subreddit: PrawSubReddit = obj.subreddit
            await mention_subreddit.load()

            subreddit: SubReddit = await db_client.subreddit.get_or_create(mention_subreddit)
            game: Game = await db_client.game.create(subreddit, tagger, tagee)
            await parent.reply(ReplyEnum.comment_reply_tag(tagger.username))

            return str(game.id)

        return game_id

    def stream(self, reddit: Reddit) -> AsyncIterator[Message]:
        s: AsyncIterator[Message] = reddit.inbox.stream()

        return s
