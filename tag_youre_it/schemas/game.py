from typing import List, Optional
from uuid import UUID

from sqlmodel import SQLModel

from tag_youre_it.models.player import Player


class IGameBase(SQLModel):
    players: Optional[List[Player]] = []
    is_active: Optional[bool] = None
    subreddit_id: Optional[int] = None


class IGameCreate(IGameBase):
    pass


class IGameRead(IGameBase):
    ref_id: UUID


class IGameUpdate(IGameBase):
    pass
