import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tag_youre_it.core.exceptions import ImproperlyConfigured


def get_db_url(test: bool = False) -> str:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST_TEST") if test else os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB]):
        raise ImproperlyConfigured(
            "Could not build Postgres URL string. Check environment variables."
        )

    return f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa


DB_POOL_SIZE = 83
WEB_CONCURRENCY = 9
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
POSTGRES_URL = get_db_url()
POSTGRES_TEST_URL = get_db_url(test=True)

engine = create_async_engine(
    POSTGRES_URL, echo=True, future=True, pool_size=POOL_SIZE, max_overflow=64
)
test_engine = create_async_engine(
    POSTGRES_TEST_URL, echo=False, future=True, pool_size=POOL_SIZE, max_overflow=64
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
