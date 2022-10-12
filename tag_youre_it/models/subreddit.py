from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseConfig, validator
from sqlmodel import Field, SQLModel

from tag_youre_it.models import BaseModel


class SubRedditBase(SQLModel):
    name: str = Field(default=None, description="The database name of the subreddit")
    sub_id: str = Field(default=None, description="The Reddit Id of the subreddit")
    display_name: str = Field(default=None, description="The human friendly name of the subreddit")

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "name": "t4_csdf9",
                "sub_id": "nej7au",
                "display_name": "TagYoureItBot",
            }
        }


class SubReddit(BaseModel, SubRedditBase, table=True):
    @validator("created_at", pre=True, always=True)
    def set_created_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(cls, v: Optional[datetime] = None) -> datetime:
        return v or datetime.now(timezone.utc)
