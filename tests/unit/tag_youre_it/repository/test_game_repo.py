import pytest
from mock import Mock
from sqlalchemy.ext.asyncio import AsyncSession

from tag_youre_it.models.game import Game
from tag_youre_it.models.player import Player
from tag_youre_it.repository.game import GameRepository
from tag_youre_it.repository.player import PlayerRepository
from tag_youre_it.repository.subreddit import SubRedditRepository
from tests.unit import test_subreddit


PLAYER_TWO = dict(
    name="test", is_employee=False, id="fs89dfd", icon_img="test.com", created_utc=1626226832.0
)


@pytest.mark.asyncio
async def test_create_game(async_session: AsyncSession, player: Player):
    player_repo = PlayerRepository(async_session)
    sub_repo = SubRedditRepository(async_session)

    mock_sub = Mock()
    mock_sub.configure_mock(**test_subreddit)

    mock_player = Mock()
    mock_player.configure_mock(**PLAYER_TWO)

    sub = await sub_repo.get_or_create(mock_sub)
    p2 = await player_repo.get_or_create(mock_player)

    repo = GameRepository(async_session)
    instance = await repo.create(sub, player, p2)

    assert type(instance) == Game

    player_names = [p.username for p in instance.players]
    assert player.username in player_names
    assert p2.username in player_names
