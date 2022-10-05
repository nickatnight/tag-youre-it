from datetime import datetime
from typing import Optional
from uuid import UUID

from tag_youre_it.models.player import PlayerBase


class IPlayerCreate(PlayerBase):
    pass


class IPlayerRead(PlayerBase):
    id: UUID


class IPlayerUpdate(PlayerBase):
    is_it: Optional[bool] = None
    opted_out: Optional[bool] = None
    updated_at: Optional[datetime] = None
