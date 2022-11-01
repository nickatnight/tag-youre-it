from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseConfig, validator
from sqlmodel import Field, SQLModel

from tag_youre_it.models.base import BaseModel


class SubRedditBase(SQLModel):
    # aPRAW fields
    name: str = Field(description="The database name of the subreddit")
    sub_id: str = Field(description="The Reddit Id of the subreddit")
    display_name: str = Field(description="The human friendly name of the subreddit")
    created_utc: int = Field(
        description="Time the subreddit was created, represented in Unix Time."
    )
    description: str = Field(description="Subreddit description, in Markdown.")
    description_html: str = Field(description="Subreddit description, in HTML.")
    over18: bool = Field(description="Whether the subreddit is NSFW.")
    subscribers: int = Field(description="Count of subscribers.")

    # custom
    is_banned: Optional[bool] = Field(
        default=False, description="Is the bot banned from the Subreddit."
    )

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
