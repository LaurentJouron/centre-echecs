"""Management of chess player results."""

from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games, scores and ranking in real time."""

    @staticmethod
    def score(player1=None, player2=None):
        if MatchView.player1_win():
            return player1, player2
        elif MatchView.player2_win():
            return player1, player2
        else:
            MatchView.draw()
            return player1, player2
        
    match_view = MatchView()
    match_data = match_view.results()
    match = MatchModel(match_data[0],   # player 1
                       match_data[1])   # player 2
    match_view.display_match(match)
