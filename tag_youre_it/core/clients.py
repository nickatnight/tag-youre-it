from tag_youre_it.repository.base import AbstractRepository
from tag_youre_it.repository.player import PlayerRepository


class DbClient:
    def __init__(self, player: PlayerRepository, game: AbstractRepository):
        self.player = player
        self.game = game
