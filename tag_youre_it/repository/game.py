import logging

from tag_youre_it.models.game import Game
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit
from tag_youre_it.repository import AbstractRepository
from tag_youre_it.schemas.game import IGameCreate, IGameUpdate


logger: logging.Logger = logging.getLogger(__name__)


class GameRepository(AbstractRepository[Game, IGameCreate, IGameUpdate]):
    async def create(self, subreddit: SubReddit, tagger: Player, tagee: Player) -> Game:
        pass
