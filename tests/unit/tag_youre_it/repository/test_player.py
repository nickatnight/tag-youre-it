# from typing import Optional

# import pytest
# from sqlmodel import Field, Session, SQLModel, create_engine

# from tag_youre_it.models import Player
# from tag_youre_it.repository import PlayerRepository


# @pytest.mark.asyncio
# async def test_query(clear_sqlmodel, db_conn):
#     repo = PlayerRepository(db_conn)
#     player_1 = (
#         Player(
#             reddit_id="nny218",
#             username="harry",
#             icon_img="reddit.com",
#             opted_out=False,
#             is_it=True,
#             is_employee=False,
#             created_utc="2004-09-16T23:59:58.75",
#         ),
#     )
#     expected = 1
#     engine = create_engine("sqlite://")

#     SQLModel.metadata.create_all(engine)

#     async def fetch():
#         return expected

#     # async function calls need to return an awaitable
#     db_conn.fetch.return_value = fetch()

#     # with Session(engine) as session:
#     #     session.add(player_1)
#     #     session.commit()
#     #     session.refresh(player_1)

#     # with Session(engine) as session:
#     #     query_hero = session.query(Hero).first()
#     #     assert query_hero
#     #     assert query_hero.name == hero_1.name

#     feeds = await repo.list_opted_out()

#     assert feeds == expected
#     # assert function was called with the query we expect
#     db_conn.fetch.assert_called_once_with(expected)
