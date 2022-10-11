from typing import List, Optional
from uuid import UUID

from tag_youre_it.models.game import GameBase
from tag_youre_it.models.player import Player


class IGameCreate(GameBase):
    pass


class IGameRead(GameBase):
    id: UUID


class IGameUpdate(GameBase):
    players: Optional[List[Player]]
    is_active: Optional[bool]
