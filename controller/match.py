"""Management of chess player results."""

from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games, scores and ranking in real time."""

    @staticmethod
    def score_match():
        match_view = MatchView()
        match_results = match_view.results()
        match_data = match_results.get_player_information()
        match = MatchModel(match_data[0],  # player 1
                           match_data[1],  # score 1
                           match_data[2],  # player 2
                           match_data[3])  # score 2