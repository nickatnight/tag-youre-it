from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID

from pydantic import BaseConfig, validator
from sqlmodel import Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit


class GameBase(SQLModel):
    players: List["Player"] = Relationship(
        back_populates="game", sa_relationship_kwargs={"lazy": "selection"}
    )
    is_active: bool = Field(default=True, description="Is the Game active or not.")
    subreddit_id: UUID = Field(
        default=None, foreign_key="subreddit.id", description="The database uuid of the subreddit"
    )
    subreddit: SubReddit = Relationship(back_populates="games")

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "players": [{"reddit_id": "nny27"}],
                "is_active": True,
                "subreddit_id": "2c4993a6-fac8-4467-a579-ffaeb41fb105",
                "subreddit": {
                    "name": "t4_csdf9",
                    "sub_id": "nej7au",
                    "display_name": "TagYoureItBot",
                },
            }
        }


class Game(BaseModel, GameBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, _: Optional[datetime] = None) -> datetime:
        return datetime.now(timezone.utc)
