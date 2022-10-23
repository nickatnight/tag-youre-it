from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel


class IPlayerBase(SQLModel):
    reddit_id: Optional[str] = None
    username: Optional[str] = None
    icon_img: Optional[str] = None
    opted_out: Optional[bool] = False
    tag_time: Optional[datetime] = None
    is_employee: Optional[bool] = False
    created_utc: Optional[datetime] = None


class IPlayerCreate(IPlayerBase):
    pass


class IPlayerRead(IPlayerBase):
    ref_id: UUID


class IPlayerUpdate(IPlayerBase):
    created_utc: Optional[datetime] = None
