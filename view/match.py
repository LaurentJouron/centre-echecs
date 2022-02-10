"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Manages the results of the chess tournament."""
    
    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
    
    def player1_win(self):
        """player 1 wins"""
        self.player1 = 1
        self.player2 = 0
    
    def player2_win(self):
        """player 2 wins"""
        self.player1 = 0
        self.player2 = 1
    
    def draw(self):
        self.player1 = self.player2 = 0.5

