"""Management of the tournament organization"""

from view.tournament import TournamentView
from model.tournament import TournamentModel


class TournamentController:
    
    @staticmethod
    def new_tournament():
        tournament_view = TournamentView()
        tournament_data = tournament_view.organize_new_tournament()
        tournament = TournamentModel(tournament_data[0],    # name
                                     tournament_data[1],    # place
                                     tournament_data[2],    # start date
                                     tournament_data[3])    # end date

        tournament_view.display_tournament_organization(tournament)
