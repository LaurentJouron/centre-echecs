"""Management of tournament organization."""
from tinydb import TinyDB


class MatchModel:
    """Manages the results of the chess tournament."""
    db = TinyDB(f"data/players.json", indent=4)

    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def __str__(self):
        return f"The match between {self.player1} and {self.player2} " \
               f"just ended.\n" \
               f"{self.player1} mark {self.score1}, " \
               f" {self.player2} mark {self.score2}"
    
    def player1_win(self):
        """player 1 wins"""
        self.score1 = 1
        self.score2 = 0
    
    def player2_win(self):
        """player 2 wins"""
        self.score1 = 0
        self.score2 = 1
    
    def draw(self):
        self.score1 = 0.5
        self.score2 = 0.5
