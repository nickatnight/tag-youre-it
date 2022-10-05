from datetime import datetime, timezone
from typing import List

from pydantic import BaseConfig, validator
from sqlmodel import Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.player import Player


class GameBase(SQLModel):
    players: List["Player"] = Relationship(
        back_populates="game", sa_relationship_kwargs={"lazy": "selectin"}
    )
    is_active: bool = Field(...)

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "reddit_id": "1234-43143-3134-13423",
                "reddit_username": "nny218",
                "icon_img": "reddit.com",
                "opted_out": False,
                "is_it": True,
                "is_employee": False,
                "created_utc": "2004-09-16T23:59:58.75",
            }
        }


class Game(BaseModel, GameBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v):
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, v):
        return v or datetime.now(timezone.utc)
