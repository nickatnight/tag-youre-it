from unittest.mock import patch

import pytest
import pytest_asyncio
from sqlmodel import SQLModel
from sqlmodel.main import default_registry


FAKE_SETTINGS = dict(
    client_id="dummy",
    client_secret="dummy",
    user_agent="dummy",
)


@pytest.fixture()
def clear_sqlmodel():
    # Clear the tables in the metadata for the default base model
    SQLModel.metadata.clear()
    # Clear the Models associated with the registry, to avoid warnings
    default_registry.dispose()
    yield
    SQLModel.metadata.clear()
    default_registry.dispose()


@pytest_asyncio.fixture
async def db_conn():
    with patch("tag_youre_it.core.clients.async_session") as mock_pool:
        mock_pool.configure_mock(
            **{
                "async_session.return_value": mock_pool,
            }
        )

        yield mock_pool
