import logging
from datetime import datetime, timezone
from typing import AsyncIterator, Optional, Union
from uuid import UUID

from asyncpraw import Reddit
from asyncpraw.models import Message, Redditor
from asyncpraw.models import Subreddit as PrawSubReddit

from tag_youre_it.core.config import settings
from tag_youre_it.core.const import TAG_TIME, ReplyEnum, TagEnum
from tag_youre_it.models.game import Game
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit
from tag_youre_it.services.stream.base import AbstractStream
from tag_youre_it.services.tag import TagService


logger = logging.getLogger(__name__)


class InboxStreamService(AbstractStream[Message]):
    async def pre_flight_check(self, tag_service: TagService, obj: Message) -> bool:
        author = obj.author
        await author.load()  # Re-fetches the object

        author_name = author.name
        logger.info(f"Reading mention from [{author_name}]")

        # direct messages which involve user engagement take precedence
        if obj.was_comment is False:
            logger.info(f"Subject of Message[{obj.subject}")

            # user previously opted out and wants to play again
            enable_check = TagEnum.ENABLE_PHRASE == obj.subject.title().lower()
            opted_out_check1 = author_name in await tag_service.player_list_opted_out()

            if all([enable_check, opted_out_check1]):
                await tag_service.player_set_opted_out(author.id, False)
                await obj.reply(ReplyEnum.welcome_back(author=author_name))

            # user wants to opt of playing
            disable_check = TagEnum.DISABLE_PHRASE == obj.subject.title().lower()
            opted_out_check2 = author_name not in await tag_service.player_list_opted_out()

            if all([disable_check, opted_out_check2]):
                await tag_service.player_set_opted_out(author.id, True)
                await obj.reply(ReplyEnum.user_opts_out_info(author=author_name))

            await obj.mark_read()
            return False

        # check if mention is not from the streams subreddit
        mention_subreddit = obj.subreddit
        await mention_subreddit.load()

        if mention_subreddit.display_name != self.subreddit_name:
            logger.info(
                f"SubReddit[r/{self.subreddit_name}] does not match mention "
                f"Subreddit: r/{mention_subreddit.display_name}...skipping"
            )
            return False

        return True

    async def process(
        self, tag_service: TagService, obj: Message, game_id: Optional[Union[UUID, str]] = None
    ) -> Optional[Union[UUID, str]]:

        if TagEnum.KEY in obj.body.lower():
            mention_subreddit: PrawSubReddit = obj.subreddit
            await mention_subreddit.load()

            subreddit: SubReddit = await tag_service.subreddit_get_or_create(mention_subreddit)
            game: Optional[Game] = await tag_service.current_game(subreddit)

            mention_author: Redditor = obj.author  # the person tagging
            await mention_author.load()

            parent = await obj.parent()
            await parent.load()
            author: Redditor = parent.author  # the person who got tagged
            await author.load()

            # prevent tagger from tagging bot
            if author.name == settings.USERNAME:
                logger.info(f"Player [{mention_author.name}] tried tagging bot")
                await obj.reply(ReplyEnum.unable_to_tag_bot())
                return game_id

            # prevent tagger from tagging self
            if author.id == mention_author.id:
                logger.info(f"Player [{mention_author.name}] tried tagging themself")
                await obj.reply(ReplyEnum.unable_to_tag_self())
                return game_id

            # prevent an opted out user from participating in game
            if author.name in await tag_service.player_list_opted_out():
                logger.info(f"Player [{author.username}] has opted out.")
                await obj.reply(ReplyEnum.user_opts_out(author=author.username))
                return game_id

            # TODO: change this, active game means tagger is already created
            tagger: Player = await tag_service.player_get_or_create(mention_author)
            tagee: Player = await tag_service.player_get_or_create(author)

            # a game is currently being played
            if game is not None:  # add check for game.modified_at

                # is the tagger actually it?
                if tagger.tag_time:
                    tag_over_time: int = int(
                        (datetime.now(timezone.utc) - tagger.tag_time).total_seconds()
                    )

                    # player didn't tag anyone in allotted time, so end current game
                    if tag_over_time > TAG_TIME:
                        await tag_service.reset_game(game.ref_id, tagger)
                        await obj.reply(ReplyEnum.game_over(tag_over_time=tag_over_time))
                        return None

                    # the 'it' person tagged another player
                    await tag_service.add_player_to_game(game.ref_id, tagee)
                    await parent.reply(ReplyEnum.comment_reply_tag(tagger.username))

                    return game_id

                logger.info(f"Current active Game[{game_id}] Player(s)[{game.players}].")

                await obj.reply(ReplyEnum.active_game())
                return game_id

            # there is no active game, so start a new one
            await tag_service.player_untag(mention_author)
            await tag_service.player_tag(author)
            game = await tag_service.game.create(subreddit, tagger, tagee)

            logger.info(f"New Game[{game}] created")
            await parent.reply(ReplyEnum.comment_reply_tag(mention_author.name))

            return game.ref_id

        return game_id

    def stream(self, reddit: Reddit) -> AsyncIterator[Message]:
        s: AsyncIterator[Message] = reddit.inbox.stream()

        return s
