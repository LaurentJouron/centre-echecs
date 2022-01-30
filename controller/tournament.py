"""Management of the tournament organization"""

from view.tournament import TournamentView
from model.tournament import TournamentModel


class TournamentController:

    @staticmethod
    def new_tournament():
        tournament_data = TournamentView.display_tournament_organization()
        new_tournament = TournamentModel(tournament_data[0],    # name
                                         tournament_data[1],    # place
                                         tournament_data[2],    # start date
                                         tournament_data[3],    # end date
                                         tournament_data[4])    # rounds
        return TournamentView.display_tournament_organization(new_tournament)
