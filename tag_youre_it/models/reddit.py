from datetime import datetime, timezone

from pydantic import validator
from sqlmodel import Field, SQLModel

from tag_youre_it.models import BaseModel


# from tag_youre_it.models.player import Player


class SubRedditBase(SQLModel):
    name: str = Field(default=None)
    sub_id: str = Field(default=None)


class SubReddit(BaseModel, SubRedditBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v):
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, v):
        return v or datetime.now(timezone.utc)
