import asyncio
from typing import Generator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from tag_youre_it.core.db import test_engine
from tag_youre_it.models import Player
from tests.unit import test_redditor_one


FAKE_SETTINGS = dict(
    client_id="dummy",
    client_secret="dummy",
    user_agent="dummy",
)


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # noqa: indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def async_session() -> AsyncSession:
    async_test_session = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_test_session() as s:
        async with test_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s

    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await test_engine.dispose()


@pytest.fixture
def player():
    return Player(
        username=test_redditor_one["name"],
        reddit_id=test_redditor_one["id"],
        icon_img=test_redditor_one["icon_img"],
        is_employee=test_redditor_one["is_employee"],
        created_utc=test_redditor_one["created_utc"],
    )
