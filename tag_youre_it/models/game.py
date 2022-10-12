from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseConfig, validator
from sqlmodel import Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.player import Player


class GameBase(SQLModel):
    players: List["Player"] = Relationship(
        back_populates="game", sa_relationship_kwargs={"lazy": "selectin"}
    )
    is_active: bool = Field(..., description="Is the Game active or not.")
    # TODO: add subreddit

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "players": [{"reddit_id": "nny27"}],
                "is_active": True,
            }
        }


class Game(BaseModel, GameBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, _: Optional[datetime] = None) -> datetime:
        return datetime.now(timezone.utc)
