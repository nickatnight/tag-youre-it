# from datetime import datetime, timezone
# from mock import Mock

# import pytest
# from sqlalchemy.ext.asyncio import AsyncSession

# from tag_youre_it.models import Game
# from tag_youre_it.repository import GameRepository
# from tests.unit import test_redditor_one


# @pytest.mark.asyncio
# async def test_get_or_create_when_object_doesnt_exist(async_session: AsyncSession, game: Game):
#     repo = GameRepository(async_session)
#     mock_redditor = Mock()
#     mock_redditor.configure_mock(**test_redditor_one)
#     instance = await repo.get_or_create(mock_redditor)

#     assert type(instance) == Player
#     assert instance.username == test_redditor_one["name"]
