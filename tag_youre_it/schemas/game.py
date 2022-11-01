from typing import List, Optional
from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.game import GameBase
from tag_youre_it.models.player import Player


class IGameBase(GameBase):
    pass


class IGameCreate(IGameBase):
    pass


class IGameRead(IGameBase):
    ref_id: UUID
    players: Optional[List[Player]] = []


@optional
class IGameUpdate(IGameBase):
    pass
