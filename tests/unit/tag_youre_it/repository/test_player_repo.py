from datetime import datetime, timezone

import pytest
from mock import Mock
from sqlalchemy.ext.asyncio import AsyncSession

from tag_youre_it.models import Player
from tag_youre_it.repository import PlayerRepository
from tests.unit import test_redditor_one


@pytest.mark.asyncio
async def test_get_or_create_when_object_doesnt_exist(async_session: AsyncSession):
    repo = PlayerRepository(async_session)
    mock_redditor = Mock()
    mock_redditor.configure_mock(**test_redditor_one)
    instance = await repo.get_or_create(mock_redditor)

    assert type(instance) == Player
    assert instance.username == test_redditor_one["name"]


@pytest.mark.asyncio
async def test_get_or_create_when_object_exists(async_session: AsyncSession, player: Player):
    async_session.add(player)
    await async_session.commit()
    await async_session.refresh(player)

    repo = PlayerRepository(async_session)
    mock_redditor = Mock()
    mock_redditor.configure_mock(**test_redditor_one)
    instance = await repo.get_or_create(mock_redditor)

    assert instance.ref_id == player.ref_id


@pytest.mark.asyncio
async def test_tag(async_session: AsyncSession, player: Player):
    async_session.add(player)
    await async_session.commit()
    await async_session.refresh(player)

    assert player.tag_time is None

    repo = PlayerRepository(async_session)
    mock_redditor = Mock()
    mock_redditor.configure_mock(**test_redditor_one)

    await repo.tag(mock_redditor)

    assert player.tag_time is not None


@pytest.mark.asyncio
async def test_untag(async_session: AsyncSession, player: Player):
    tag_time = datetime.now(timezone.utc)
    player.tag_time = tag_time

    async_session.add(player)
    await async_session.commit()
    await async_session.refresh(player)

    assert player.tag_time == tag_time

    repo = PlayerRepository(async_session)
    mock_redditor = Mock()
    mock_redditor.configure_mock(**test_redditor_one)

    await repo.untag(mock_redditor)

    assert player.tag_time is None
