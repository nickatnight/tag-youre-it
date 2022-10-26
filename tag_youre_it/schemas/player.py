from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.player import PlayerBase


class IPlayerBase(PlayerBase):
    pass


class IPlayerCreate(IPlayerBase):
    pass


class IPlayerRead(IPlayerBase):
    ref_id: UUID


@optional
class IPlayerUpdate(IPlayerBase):
    pass
