from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel


class IPlayerBase(SQLModel):
    reddit_id: Optional[str] = None
    reddit_username: Optional[str] = None
    icon_img: Optional[str] = None
    opted_out: Optional[bool] = False
    is_it: Optional[bool] = False
    is_employee: Optional[bool] = False


class IPlayerCreate(IPlayerBase):
    pass


class IPlayerRead(IPlayerBase):
    id: UUID


class IPlayerUpdate(IPlayerBase):
    created_utc: Optional[datetime] = None
