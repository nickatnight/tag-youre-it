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
class DbClient:
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
        logger.info(f"Adding [{tagee.username}] to Game.red_id[{game_ref_id}]")

        db_obj = await self.game.get(ref_id=game_ref_id)
        player_ref_ids: List[UUID] = [str(p.ref_id) for p in db_obj.players]

        if str(game_ref_id) in player_ref_ids:
            logger.info(f"Player[{tagee.username}] already exists in Game[{game_ref_id}]")
            return

        db_obj.players.append(tagee)

        await self.game.db.commit()
        await self.game.db.refresh(db_obj)
