from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseConfig, validator
from sqlmodel import Column, DateTime, Field, SQLModel

from tag_youre_it.models.base import BaseModel


class PlayerBase(SQLModel):
    reddit_id: str = Field(..., description="The ID of the Redditor.")
    reddit_username: str = Field(..., description="The Redditor’s username.")
    icon_img: str = Field(..., description="The url of the Redditors’ avatar.")
    opted_out: bool = Field(...)
    is_it: bool = Field(...)
    is_employee: bool = Field(..., description="Whether or not the Redditor is a Reddit employee.")
    created_utc: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        ),
        description="Time the account was created, represented in Unix Time.",
    )

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


class Player(BaseModel, PlayerBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, _: Optional[datetime] = None) -> datetime:
        return datetime.now(timezone.utc)
