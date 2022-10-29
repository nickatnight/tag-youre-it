import logging
from typing import List, Optional, Union
from uuid import UUID

from tag_youre_it.models.game import Game
from tag_youre_it.models.player import Player
from tag_youre_it.models.subreddit import SubReddit
from tag_youre_it.repository import (
    GameRepository,
    PlayerRepository,
    SubRedditRepository,
)
from tag_youre_it.schemas.game import IGameUpdate
from tag_youre_it.schemas.player import IPlayerUpdate


logger: logging.Logger = logging.getLogger(__name__)


# TODO: move abstract repository methods here and remove dependency
class TagService:
    def __init__(
        self, player: PlayerRepository, game: GameRepository, subreddit: SubRedditRepository
    ):
        self.player = player
        self.game = game
        self.subreddit = subreddit

    async def reset_game(self, game_ref_id: Union[UUID, str], tagger: Player) -> None:
        logger.info(f"Player [{tagger.username}] tag time expired. Ending game.")
        game_obj = IGameUpdate(is_active=False)
        db_obj = await self.game.get(ref_id=game_ref_id)

        if not db_obj:
            raise Exception("no game found")

        await self.game.update(db_obj, game_obj)

        player_obj = IPlayerUpdate(tag_time=None)
        await self.player.update(tagger, player_obj)

    async def current_game(self, subreddit: SubReddit) -> Optional[Game]:
        active_games: List[Game] = await self.game.active()

        for game in active_games:
            if game.subreddit_id == subreddit.id:
                return game

        return None

    async def add_player_to_game(self, game_ref_id: Union[UUID, str], tagee: Player) -> None:
        game_ref_ids: List[str] = [str(g.ref_id) for g in tagee.games]

        if str(game_ref_id) in game_ref_ids:
            logger.info(f"Player[{tagee.username}] already exists in Game[{game_ref_id}]")
            return

        await self.game.add_player(tagee, game_ref_id)
