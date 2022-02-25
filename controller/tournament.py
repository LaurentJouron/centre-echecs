"""Management of the tournament organization"""

from view.tournament import TournamentView
from model.tournament import TournamentModel


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()

    def new_tournament(self):
        """Imports view data, imports model data and compares accuracy."""
        tournament_data = self.tournament_view.organize_new_tournament()
        tournament = TournamentModel(tournament_data[0],  # name
                                     tournament_data[1],  # place
                                     tournament_data[2],  # start date
                                     tournament_data[3])  # end date

        return self.tournament_view.display_tournament_organization(tournament)

"""Si j'ai un trounoi ajouter un player et boucler 8 fois"""