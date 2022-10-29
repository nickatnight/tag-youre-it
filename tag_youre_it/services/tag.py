import logging
from typing import List, Optional, Union
from uuid import UUID

from asyncpraw.models import Redditor
from asyncpraw.models import Subreddit as PrawSubReddit

from tag_youre_it.models import Game, Player, SubReddit
from tag_youre_it.repository import (
    GameRepository,
    PlayerRepository,
    SubRedditRepository,
)
from tag_youre_it.schemas.game import IGameUpdate
from tag_youre_it.schemas.player import IPlayerUpdate


logger: logging.Logger = logging.getLogger(__name__)


class TagService:
    """main service for all tag operations"""

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

    async def game_create(self, subreddit: SubReddit, tagger: Player, tagee: Player) -> Game:
        g: Game = await self.game.create(subreddit, tagger, tagee)
        return g

    async def player_get_or_create(self, reddit_obj: Redditor) -> Player:
        p: Player = await self.player.get_or_create(reddit_obj)
        return p

    async def player_tag(self, reddit_obj: Redditor) -> None:
        await self.player.tag(reddit_obj)

    async def player_untag(self, reddit_obj: Redditor) -> None:
        await self.player.untag(reddit_obj)

    async def player_list_opted_out(self) -> List[str]:
        opt_list: List[str] = await self.player.list_opted_out()
        return opt_list

    async def player_set_opted_out(self, reddit_id: str, value: bool) -> None:
        await self.player.set_opted_out(reddit_id, value)

    async def subreddit_get_or_create(self, reddit_obj: PrawSubReddit) -> SubReddit:
        sub: SubReddit = await self.subreddit.get_or_create(reddit_obj)
        return sub
