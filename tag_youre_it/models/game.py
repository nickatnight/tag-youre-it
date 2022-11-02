from datetime import datetime, timezone
from typing import List, Optional

from pydantic import validator
from sqlmodel import Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.link import GamePlayerLink
from tag_youre_it.models.player import Player


class GameBase(SQLModel):
    subreddit_id: int = Field(
        default=None, foreign_key="subreddit.id", description="The database uuid of the subreddit"
    )
    is_active: Optional[bool] = Field(default=True, description="Is the Game active or not.")


class Game(BaseModel, GameBase, table=True):
    players: List[Player] = Relationship(
        back_populates="games",
        link_model=GamePlayerLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, _: Optional[datetime] = None) -> datetime:
        return datetime.now(timezone.utc)
