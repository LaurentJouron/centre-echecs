"""Information for the organisation of chass tournaments."""
from tinydb import TinyDB


class MatchModel:
    """Generates tournament elements."""
    db = TinyDB(f"data/tour.json", indent=4)

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


