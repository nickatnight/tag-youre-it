import pytest
from mock import Mock
from sqlalchemy.ext.asyncio import AsyncSession

from tag_youre_it.models.subreddit import SubReddit
from tag_youre_it.repository.subreddit import SubRedditRepository
from tests.unit import test_subreddit


@pytest.mark.asyncio
async def test_get_or_create_when_object_doesnt_exist(async_session: AsyncSession):
    repo = SubRedditRepository(async_session)
    mock_subreddit = Mock()
    mock_subreddit.configure_mock(**test_subreddit)
    instance = await repo.get_or_create(mock_subreddit)

    assert type(instance) == SubReddit
    assert instance.name == test_subreddit["name"]
