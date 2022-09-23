from dataclasses import dataclass
from typing import List

from tag_youre_it.domain.base import BaseDomain
from tag_youre_it.domain.player import PlayerDomain


@dataclass
class GameDomain(BaseDomain):
    players: List[PlayerDomain]
    is_active: bool
