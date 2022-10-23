import asyncio
import logging
import os


# NOTE: this file should only be used for testing and local development

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

if __name__ == "__main__":
    from tag_youre_it.core import (
        DbClient,
        GameEngine,
        RedditClientConfigTyped,
        settings,
    )
    from tag_youre_it.core.const import SupportedSubs
    from tag_youre_it.core.db import async_session
    from tag_youre_it.repository import (
        GameRepository,
        PlayerRepository,
        SubRedditRepository,
    )
    from tag_youre_it.services import InboxStreamService

    sesh = async_session()
    player: PlayerRepository = PlayerRepository(sesh)
    game: GameRepository = GameRepository(sesh)
    subreddit: SubRedditRepository = SubRedditRepository(sesh)
    config: RedditClientConfigTyped = {  # type: ignore
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "username": settings.USERNAME,
        "password": settings.PASSWORD,
        "user_agent": f"{settings.BOT_NAME}/{settings.VERSION}/{settings.DEVELOPER}",
    }

    e = GameEngine(
        db_client=DbClient(player, game, subreddit),
        stream_service=InboxStreamService(SupportedSubs.TAG_YOURE_IT_BOT),
        reddit_config=config,
    )

    asyncio.run(e.run())
