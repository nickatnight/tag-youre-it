from typing import List, Optional

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
