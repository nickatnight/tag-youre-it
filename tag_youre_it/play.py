import asyncio
import logging
import os


# NOTE: this file should only be used for testing and local development

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

if __name__ == "__main__":
    from tag_youre_it.core.config import settings
    from tag_youre_it.core.const import SupportedSubs
    from tag_youre_it.core.db import async_session
    from tag_youre_it.core.engine import GameEngine
    from tag_youre_it.core.typed import RedditClientConfigTyped
    from tag_youre_it.repository.game import GameRepository
    from tag_youre_it.repository.player import PlayerRepository
    from tag_youre_it.repository.subreddit import SubRedditRepository
    from tag_youre_it.services.stream.inbox import InboxStreamService
    from tag_youre_it.services.tag import TagService

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
        tag_service=TagService(player, game, subreddit),
        stream_service=InboxStreamService(SupportedSubs.DOGECOIN),
        reddit_config=config,
    )

    asyncio.run(e.run())
