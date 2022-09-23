import asyncio
import logging
import os


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

if __name__ == "__main__":
    from tag_youre_it.core.abstract import AbstractRepository
    from tag_youre_it.core.clients import DbClient
    from tag_youre_it.core.config import settings
    from tag_youre_it.core.engine import Engine
    from tag_youre_it.services.stream import InboxStreamService

    e = Engine(
        db_client=DbClient(AbstractRepository, AbstractRepository),
        stream_service=InboxStreamService(),
        reddit_config={
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "username": settings.USERNAME,
            "password": settings.PASSWORD,
            "user_agent": f"{settings.BOT_NAME}/{settings.VERSION}/{settings.DEVELOPER}",
        },
    )

    asyncio.run(e.run())
