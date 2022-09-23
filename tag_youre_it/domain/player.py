from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from tag_youre_it.domain.base import BaseDomain


@dataclass
class PlayerDomain(BaseDomain):
    reddit_id: str
    reddit_username: str
    icon_img: str
    is_boring: bool
    is_it: bool
    is_employee: bool
    tag_time: Optional[datetime]
