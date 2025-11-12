from __future__ import annotations
from dataclasses import dataclass

from core.animal import Animal
from core.player_info import PlayerInfo


@dataclass(frozen=True)
class CellView:
    x: int
    y: int
    animals: set[Animal]
    helpers: set[PlayerInfo]
