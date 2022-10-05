from typing import List, Optional
from uuid import UUID

from tag_youre_it.models.game import GameBase


class IGameCreate(GameBase):
    pass


class IGameRead(GameBase):
    id: UUID


class IGameUpdate(GameBase):
    players: Optional[List] = None
    is_active: Optional[bool] = None
