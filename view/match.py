"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Manages the results of the chess tournament."""

    player_1 = ["Laurent", "Virginie", "Louis", "Antoine"]
    player_2 = ["Thierno", "Marc", "Julia", "Felix"]
    
    def __init__(self, player1, player2, match_nul):
        self.player_1 = player1
        self.player_2 = player2
        self.match_nul = match_nul
        
    def player1_win(self):
        """player 1 wins"""
        self.player_1 = 1
        self.player_2 = 0
        
    def player2_win(self):
        """player 2 wins"""
        self.player_1 = 0
        self.player_2 = 1
        
    def draw(self):
        self.player_1 = 0.5
        self.player_2 = 0.5
        
        

