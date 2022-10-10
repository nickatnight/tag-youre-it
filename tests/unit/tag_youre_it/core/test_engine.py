# import asyncio
# from unittest import TestCase, mock

# import pytest
# import asyncpraw

# from tag_youre_it.core.engine import Engine
# # from ...conftest import FAKE_SETTINGS

# def test_engine_simple():
#     assert "hi" == "hi"


# class EnginTestCase(TestCase):
#     @pytest.fixture(autouse=True)
#     def _mocker(self, mocker):
#         self._mocker = mocker

#     def setUp(self):
#         super().setUp()
#         self._mocker.patch("asyncpraw.models.inbox", "stream", [])
#         # self._mocker.patch.object(asyncpraw.Reddit.inbox, "stream", [])

#     def test_engine(self):
#         e = Engine(mock.MagicMock(), mock.MagicMock(), FAKE_SETTINGS)
#         asyncio.run(e.run())
