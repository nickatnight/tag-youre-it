from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel


class ISubRedditBase(SQLModel):
    name: Optional[str] = None
    sub_id: Optional[str] = None
    display_name: Optional[str] = None


class ISubRedditCreate(ISubRedditBase):
    pass


class ISubRedditRead(ISubRedditBase):
    ref_id: UUID


class ISubRedditUpdate(SQLModel):
    pass
