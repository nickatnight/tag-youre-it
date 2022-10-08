from tag_youre_it.repository import AbstractRepository, PlayerRepository


class DbClient:
    def __init__(self, player: PlayerRepository, game: AbstractRepository):
        self.player = player
        self.game = game
