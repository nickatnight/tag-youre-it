from tag_youre_it.core.abstract import AbstractRepository


class DbClient:
    def __init__(self, player: AbstractRepository, game: AbstractRepository):
        self.player = player
        self.game = game
