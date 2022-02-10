"""Management of tournament organization."""


class MatchModel:
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_score(self):
        """Get the information of a participant."""
        return self.player1 + " " + \
            self.player2
