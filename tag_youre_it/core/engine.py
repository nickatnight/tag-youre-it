import logging

import asyncpraw
from aiohttp import ClientSession

from tag_youre_it.core.clients import DbClient
from tag_youre_it.core.config import settings
from tag_youre_it.core.typed import RedditClientConfigTyped
from tag_youre_it.services import AbstractStream


logger = logging.getLogger(__name__)


#   _______              __     __         _               _____ _
#  |__   __|             \ \   / /        ( )             |_   _| |
#     | | __ _  __ _ _____\ \_/ /__  _   _|/ _ __ ___ ______| | | |_
#     | |/ _` |/ _` |______\   / _ \| | | | | '__/ _ \______| | | __|
#     | | (_| | (_| |       | | (_) | |_| | | | |  __/     _| |_| |_
#     |_|\__,_|\__, |       |_|\___/ \__,_| |_|  \___|    |_____|\__|
#               __/ |
#              |___/
class Engine:
    def __init__(
        self,
        db_client: DbClient,
        stream_service: AbstractStream,
        reddit_config: RedditClientConfigTyped,
    ):
        self.db_client: DbClient = db_client
        self.stream_service: AbstractStream = stream_service
        self.reddit_config: RedditClientConfigTyped = reddit_config

    async def run(self):
        logger.info(
            f"Starting session with [{self.stream_service.__class__.__name__}] stream class..."
        )
        async with ClientSession(trust_env=True) as session:
            self.reddit_config.update(
                {
                    "requestor_kwargs": {
                        "session": session
                    },  # must successfully close the session when finished
                }
            )
            game_id: str = None
            db: DbClient = self.db_client

            async with asyncpraw.Reddit(**self.reddit_config) as reddit:
                logger.info(f"Streaming mentions for u/{settings.USERNAME}")

                async for mention in self.stream_service.stream(reddit):

                    pre_flight_check: bool = await self.stream_service.pre_flight_check(db, mention)
                    if pre_flight_check:
                        game_id: str = await self.stream_service.process(db, mention, game_id)

                        await mention.mark_read()
