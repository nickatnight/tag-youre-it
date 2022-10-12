from tag_youre_it.repository import (
    GameRepository,
    PlayerRepository,
    SubRedditRepository,
)


# TODO: move abstract repository methods here and remove dependency
class DbClient:
    def __init__(
        self, player: PlayerRepository, game: GameRepository, subreddit: SubRedditRepository
    ):
        self.player = player
        self.game = game
        self.subreddit = subreddit
