from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tag_youre_it.core.config import settings


engine = create_async_engine(
    settings.POSTGRES_URL, echo=True, future=True, pool_size=settings.POOL_SIZE, max_overflow=64
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
