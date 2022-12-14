from typing import List, Optional
from uuid import UUID

from tag_youre_it.core.utils import optional
from tag_youre_it.models.game import GameBase
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit


class IGameCreate(GameBase):
    pass


class IGameRead(GameBase):
    ref_id: UUID
    subreddit: Optional[SubReddit] = None
    players: Optional[List[Player]] = []


@optional
class IGameUpdate(GameBase):
    pass
