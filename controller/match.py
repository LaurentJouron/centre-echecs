"""Management of chess player results."""

from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games, scores and ranking in real time."""
    
    @staticmethod
    def game_management():
        game_management = MatchView()
        game_data = game_management.create_a_match()
        match = MatchModel(game_data[0])


