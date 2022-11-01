from typing import List, Optional
from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.game import Game
from tag_youre_it.models.player import PlayerBase


class IPlayerBase(PlayerBase):
    pass


class IPlayerCreate(IPlayerBase):
    pass


class IPlayerRead(IPlayerBase):
    ref_id: UUID
    games: Optional[List[Game]] = []


@optional
class IPlayerUpdate(IPlayerBase):
    pass
