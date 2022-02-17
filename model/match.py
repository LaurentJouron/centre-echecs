"""Management of tournament organization."""


class MatchModel:
    """Manages the results of the chess tournament."""
    
    players = ([], [])
    
    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def player1_win(self):
        """player 1 wins"""
        self.player1 = "player1"
        self.score1 += 1
        self.player2 = "player2"
        self.score2 += 0
    
    def player2_win(self):
        """player 2 wins"""
        self.player1 = "player1"
        self.score1 += 0
        self.player2 = "player2"
        self.score2 += 1
    
    def draw(self):
        self.player1 = "player1"
        self.score1 += 0.5
        self.player2 = "player2"
        self.score2 += 0.5

    def get_score(self):
        """Get a results."""
        "player1: " + self.score1 + " " + "player2: " + self.score2
