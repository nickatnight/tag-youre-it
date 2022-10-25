import logging
from typing import List

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
        # TODO: consider new 'add_player' method instead
        game_obj = Game(subreddit_id=subreddit.id, players=[tagger, tagee])
        instance = await self.insert(game_obj, from_orm=False)
        # logger.info(f"New r/{subreddit.display_name} Game[{instance}]")

        # await self.add_player(tagger, instance.ref_id)
        # await self.add_player(tagee, instance.ref_id)
        logger.info(
            f"New Game[{instance}] created with Players[{tagger.username}, {tagee.username}]"
        )

        return instance

    async def active(self) -> List[Game]:
        statement = (
            select(self.model)
            .where(self.model.is_active == True)  # noqa
            .order_by(self.model.__table__.columns["created_at"].desc())
        )
        results = await self.db.execute(statement)
        games: List[Game] = results.scalars().all()

        return games
