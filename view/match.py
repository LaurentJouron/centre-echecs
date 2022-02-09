"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Manages the results of the chess tournament."""
    
    # def __init__(self, player1=None, player2=None):
    #     self.player1 = player1
    #     self.player2 = player2

    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
    
    def player1_win(self):
        """player 1 wins"""
        self.player1 = 1
        self.player2 = 0
        return self.player1, self.player2
    
    def player2_win(self):
        """player 2 wins"""
        self.player1 = 0
        self.player2 = 1
        return self.player1, self.player2
    
    def draw(self):
        players = self.player1 = self.player2 = 0.5
        return players
    
    def results(self):
        if self.player1_win():
            return self.player1_win()
        elif self.player2_win():
            return self.player2_win()
        else:
            self.draw()
            return self.draw()
    
    def display_match(self, match):
        if self.player1_win():
            print(f"le gagnant marque {match.player1} point.")
        elif self.player2_win():
            print(f"le gagnant marque {match.player2} point.")
        else:
            print(f"Les joueurs sont à égalité et marque {match.draw()}"
                  f"points chacun.")
