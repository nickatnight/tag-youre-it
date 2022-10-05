from datetime import datetime, timezone

from pydantic import BaseConfig, validator
from sqlmodel import Column, DateTime, Field, SQLModel

from tag_youre_it.models.base import BaseModel


class PlayerBase(SQLModel):
    reddit_id: str = Field(...)
    reddit_username: str = Field(...)
    icon_img: str = Field(...)
    opted_out: bool = Field(...)
    is_it: bool = Field(...)
    is_employee: bool = Field(...)
    created_utc: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        )
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
    def set_created_at_now(cls, v):
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, v):
        return v or datetime.now(timezone.utc)
