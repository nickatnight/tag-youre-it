from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.game import GameBase


class IGameBase(GameBase):
    pass


class IGameCreate(IGameBase):
    pass


class IGameRead(IGameBase):
    ref_id: UUID


@optional
class IGameUpdate(IGameBase):
    pass
