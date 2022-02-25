"""Management of chess player results."""
from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games and scores in real time."""
    def __init__(self):
        self.match_view = MatchView()

    def game_match(self):
        """Imports view data, imports model data and compares accuracy."""
        match_data = self.match_view.results()
        match = MatchModel(match_data[0][0],  # player 1
                           match_data[0][1],  # score 1
                           match_data[1][0],  # player 2
                           match_data[1][1])  # score 2
        return match
