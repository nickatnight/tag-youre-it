import logging
from typing import List, Union
from uuid import UUID

from sqlmodel import select

from tag_youre_it.models.game import Game
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit
from tag_youre_it.repository import AbstractRepository
from tag_youre_it.schemas.game import IGameCreate, IGameUpdate


logger: logging.Logger = logging.getLogger(__name__)


class GameRepository(AbstractRepository[Game, IGameCreate, IGameUpdate]):
    model = Game

    async def create(self, subreddit: SubReddit, tagger: Player, tagee: Player) -> Game:
        game_obj = IGameCreate(subreddit_id=subreddit.id)
        instance = await self.insert(game_obj)
        logger.info(f"New r/{subreddit.display_name} Game[{instance}]")

        await self.add_player(tagger, instance.ref_id)
        await self.add_player(tagee, instance.ref_id)

        return instance

    async def add_player(self, player: Player, game_ref_id: Union[UUID, str]) -> None:
        game = await self.get(game_ref_id)
        game.players.append(player)

        await self.db.commit()
        await self.db.refresh(game)

        logger.info(f"Adding Players[{player.username}] to Game[{game.ref_id}]")

    async def active(self) -> List[Game]:
        statement = (
            select(self.model)
            .where(self.model.is_active == True)  # noqa
            .order_by(self.model.__table__.columns["created_at"].desc())  # type: ignore
        )
        results = await self.db.execute(statement)
        games: List[Game] = results.scalars().all()

        return games
