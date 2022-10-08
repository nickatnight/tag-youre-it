import logging

from tag_youre_it.models.game import Game
from tag_youre_it.repository import AbstractRepository
from tag_youre_it.schemas.game import IGameCreate, IGameUpdate


logger: logging.Logger = logging.getLogger(__name__)


class GameRepository(AbstractRepository[Game, IGameCreate, IGameUpdate]):
    pass
