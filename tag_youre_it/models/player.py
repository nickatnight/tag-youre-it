from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseConfig, validator
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel

from tag_youre_it.models.base import BaseModel
from tag_youre_it.models.link import GamePlayerLink


class PlayerBase(SQLModel):
    # PRAW fields
    reddit_id: str = Field(..., description="The ID of the Redditor.")
    username: str = Field(..., description="The Redditor’s username.")
    icon_img: str = Field(..., description="The url of the Redditors’ avatar.")
    is_employee: bool = Field(..., description="Whether or not the Redditor is a Reddit employee.")
    created_utc: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        ),
        description="Time the account was created, represented in Unix Time.",
    )
    # game fields
    opted_out: bool = Field(default=False)
    tag_time: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=True,
        )
    )


class Player(BaseModel, PlayerBase, table=True):
    games: List["Game"] = Relationship(back_populates="players", link_model=GamePlayerLink)  # noqa

    @validator("ref_id", pre=True, always=True)
    def set_ref_id(cls, v: Optional[UUID] = None) -> UUID:
        return v or uuid4()

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, _: Optional[datetime] = None) -> datetime:
        return datetime.now(timezone.utc)

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "reddit_id": "dlb7rtu",
                "username": "nny218",
                "icon_img": "reddit.com",
                "opted_out": False,
                "tag_time": "2004-09-16T23:59:58.75",
                "is_employee": False,
                "created_utc": "2004-09-16T23:59:58.75",
            }
        }
