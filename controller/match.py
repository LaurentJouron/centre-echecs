"""Management of chess player results."""
from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games, scores and ranking in real time."""

    @staticmethod
    def game_match():
        match_view = MatchView()
        match_data = match_view.results()
        match = MatchModel(match_data[0][0],  # player 1
                           match_data[0][1],  # score 1
                           match_data[1][0],  # player 2
                           match_data[1][1])  # score 2
        match_view.display_winner(match)
