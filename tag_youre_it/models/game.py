from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.link import GamePlayerLink
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit


class GameBase(SQLModel):
    subreddit_id: int = Field(
        default=None, foreign_key="subreddit.id", description="The database id of the subreddit"
    )
    is_active: Optional[bool] = Field(default=True, description="Is the Game active or not.")


class Game(BaseModel, GameBase, table=True):
    subreddit: Optional[SubReddit] = Relationship(
        back_populates="games", sa_relationship_kwargs={"lazy": "selectin"}
    )
    players: List[Player] = Relationship(
        back_populates="games",
        link_model=GamePlayerLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
