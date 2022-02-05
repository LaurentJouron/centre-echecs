"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Manages the results of the chess tournament."""
    
    def __init__(self, player1, player2, draw):
        self.player_1 = player1
        self.player_2 = player2
        self.draw = draw
    
    def player1_win(self):
        """player 1 wins"""
        self.player_1 = 1
        self.player_2 = 0
        return self.player_1, self.player_2
    
    def player2_win(self):
        """player 2 wins"""
        self.player_1 = 0
        self.player_2 = 1
        return self.player_1, self.player_2
    
    def draw(self):
        players = self.player_1 = self.player_2 = 0.5
        return players
    
    def results(self):
        if self.player1_win():
            return self.player1_win()
        elif self.player2_win():
            return self.player2_win()
        else:
            self.draw()
            return self.draw
    
    def display_match(self, match):
        player1_win = self.player1_win()
        player2_win = self.player2_win()
        if player1_win:
            print(f"le gagnant marque {match.player1_win} point.")
        elif player2_win:
            print(f"le gagnant marque {match.player2_win} point.")
        else:
            print(f"Les joueurs sont à égalité et marque 0.5 points chacun.")
