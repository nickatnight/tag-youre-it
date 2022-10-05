import logging
from typing import List

from sqlmodel import select

from tag_youre_it.models.player import Player
from tag_youre_it.repository.base import AbstractRepository
from tag_youre_it.schemas.player import IPlayerCreate, IPlayerUpdate


logger: logging.Logger = logging.getLogger(__name__)


class PlayerRepository(AbstractRepository[Player, IPlayerCreate, IPlayerUpdate]):
    model = Player

    async def list_opted_out(self) -> List[Player]:
        statement = select(self.model).where(self.model.opted_out is True)
        results = self.db.execute(statement)
        return results.scalars().all()

    async def set_opted_out(self, reddit_id: str) -> List[Player]:
        statement = select(self.model).where(self.model.reddit_id == reddit_id)
        results = self.db.execute(statement)
        player: Player = results.one()

        player.opted_out = True
        self.db.add(player)
        await self.db.commit()
        await self.db.refresh(player)

        logger.info(f"{player.reddit_username} opted out of playing.")
