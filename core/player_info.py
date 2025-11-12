from core.animal import Animal
from core.views.player_view import Kind


class PlayerInfo:
    def __init__(
        self, id: int, x: float, y: float, kind: Kind, flock: set[Animal]
    ) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.kind = kind
        self.flock = flock
