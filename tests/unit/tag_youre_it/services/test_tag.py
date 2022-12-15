import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from tag_youre_it.repository.game import GameRepository
from tag_youre_it.repository.player import PlayerRepository
from tag_youre_it.repository.subreddit import SubRedditRepository
from tag_youre_it.services.tag import TagService


class TestTagService:
    async def setUp(self, s, p1, p2, sub):
        s.add(sub)
        s.add(p1)
        s.add(p2)
        await s.commit()

    @pytest.mark.asyncio
    async def test_reset_game(self, async_session: AsyncSession, player, it_player, subreddit):
        await self.setUp(async_session, player, it_player, subreddit)
        p = PlayerRepository(async_session)
        g = GameRepository(async_session)
        s = SubRedditRepository(async_session)
        t = TagService(p, g, s)  # noqa
