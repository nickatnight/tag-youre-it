import logging
from datetime import datetime, timezone
from typing import List, Optional

from asyncpraw.models import Redditor
from sqlmodel import select

from tag_youre_it.models.player import Player
from tag_youre_it.repository.base import AbstractRepository
from tag_youre_it.schemas.player import IPlayerCreate, IPlayerUpdate


logger: logging.Logger = logging.getLogger(__name__)


class PlayerRepository(AbstractRepository[Player, IPlayerCreate, IPlayerUpdate]):
    model = Player

    async def list_opted_out(self) -> List[str]:
        statement = select(self.model).where(self.model.opted_out == True)  # noqa
        results = await self.db.execute(statement)
        players: List[Player] = results.scalars().all()

        return [p.username for p in players]

    async def set_opted_out(self, reddit_id: str, value: bool) -> None:
        statement = select(self.model).where(self.model.reddit_id == reddit_id)
        results = await self.db.execute(statement)
        player: Player = results.scalar_one()

        player.opted_out = value
        self.db.add(player)
        await self.db.commit()
        await self.db.refresh(player)

        logger.info(f"[{player.username}] opted out of playing.")

    async def get_or_create(self, reddit_obj: Redditor) -> Player:
        statement = select(self.model).where(self.model.username == reddit_obj.name)
        result = await self.db.execute(statement)
        instance: Optional[Player] = result.scalar_one_or_none()

        if instance:
            return instance

        player_obj = IPlayerCreate(
            username=reddit_obj.name,
            reddit_id=reddit_obj.id,
            icon_img=reddit_obj.icon_img,
            is_employee=reddit_obj.is_employee,
            created_utc=reddit_obj.created_utc,
            verified=reddit_obj.verified,
            is_suspended=reddit_obj.is_suspended if hasattr(reddit_obj, "is_suspended") else False,
            has_verified_email=reddit_obj.has_verified_email,
        )
        instance = await self.insert(player_obj)

        return instance

    async def untag(self, reddit_obj: Redditor) -> None:
        instance = await self.get_or_create(reddit_obj)

        player_obj = IPlayerUpdate(tag_time=None)
        _ = await self.update(instance, player_obj)

    async def tag(self, reddit_obj: Redditor) -> None:
        instance = await self.get_or_create(reddit_obj)

        player_obj = IPlayerUpdate(tag_time=datetime.now(timezone.utc))
        _ = await self.update(instance, player_obj)
