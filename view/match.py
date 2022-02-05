"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Manages the results of the chess tournament."""

    player_1 = ["Laurent", "Virginie", "Louis", "Antoine"]
    player_2 = ["Thierno", "Marc", "Julia", "Felix"]
    
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
        self.player_1 = 0.5
        self.player_2 = 0.5
        return self.player_1, self.player_2
    
    def results(self):
        player1_win = self.player1_win()
        player2_win = self.player2_win()
        draw = self.draw()
        return[player1_win, player2_win, draw]

    def display_match(self, match):
        player1_win = self.player1_win()
        player2_win = self.player2_win()
        if player1_win:
            print(f"{match.player1_win} gagne le match et marque 1 point.")
        if player2_win:
            print(f"{match.player2_win} gagne le match et marque 1 point.")
        else:
            print(f"Les joueurs sont à égalité et marque 0.5 points chacun.")
