"""Management of tournament organization."""


class ScoreModel:
    """Manages the results of the chess tournament."""
    
    players_and_score = ["player1", 0, "player2", 0]
    
    player1 = " = ".join(players_and_score[0:1])
    player2 = " = ".join(players_and_score[2:3])

    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

    def player1_win(self):
        """player 1 wins"""
        self.player1 = "player1"
        self.score1 += 1
    
    def player2_win(self):
        """player 2 wins"""
        self.player2 = "player2"
        self.score2 += 1
    
    def draw(self):
        self.player1 = "player1"
        self.score1 += 0.5
        self.player2 = "player2"
        self.score2 += 0.5

    def get_score(self):
        """Get the information of a participant."""
        # self.player1 + " " + self.score1 + " " + self.player2 + " " + \
        #       self.score2
