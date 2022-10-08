import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def get_db_url():
    return f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"  # noqa


DB_POOL_SIZE = 83
WEB_CONCURRENCY = 9
POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)
POSTGRES_URL = get_db_url()

engine = create_async_engine(
    POSTGRES_URL, echo=True, future=True, pool_size=POOL_SIZE, max_overflow=64
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
