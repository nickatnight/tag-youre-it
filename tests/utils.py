from sqlalchemy.ext.asyncio import create_async_engine

from tag_youre_it.core.config import settings


def get_db_url() -> str:
    POSTGRES_USER = settings.POSTGRES_USER
    POSTGRES_PASSWORD = settings.POSTGRES_PASSWORD
    POSTGRES_HOST = "db-test"
    POSTGRES_PORT = settings.POSTGRES_PORT
    POSTGRES_DB = settings.POSTGRES_DB

    return f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa


POSTGRES_TEST_URL = get_db_url()

test_engine = create_async_engine(
    POSTGRES_TEST_URL, echo=False, future=True, pool_size=settings.POOL_SIZE, max_overflow=64
)
