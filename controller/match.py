"""Management of chess player results."""

from view.match import MatchView
from model.match import MatchModel


class MatchController:
    """Controls the organization of games, scores and ranking in real time."""

    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        if MatchView.player1_win():
            print(
                f"Le joueur {self.player1} gagne la partie et marque 1 point.")
            return self.player1, self.player2
        elif MatchView.player2_win():
            print(
                f"Le joueur {self.player2} gagne la partie et marque 1 point.")
            return self.player1, self.player2
        else:
            MatchView.draw()
            print(
                f"Les joueurs sont à égalité "
                f"sur cette partie et marque 0.5 point chacun.")
            return self.player1, self.player2

    match_view = MatchView()
    match_data = score()
    match = MatchModel(match_data[0],   # player 1
                       match_data[1])   # player 2
