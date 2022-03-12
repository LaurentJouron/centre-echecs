"""Management of the tournament organization"""

from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController
from model.player import PlayerModel
import constants

number_of_player = constants.NUMBER_OF_PLAYERS


class TournamentController:

    def __init__(self):
        self.tournament_view = TournamentView()

    def new_tournament(self):
        """Imports view data, imports model data and compares accuracy."""
        tournament_data = self.tournament_view.organize_new_tournament()
        tournament = TournamentModel(name=tournament_data[0],
                                     place=tournament_data[1],
                                     start_date=tournament_data[2],
                                     end_date=tournament_data[3])

        return self.tournament_view.display_tournament_organization(tournament)
    
    def add_player(self):
        """Add players to the current tournament"""
    if new_tournament is True:
        get_player = PlayerController.create_player(new_tournament())
    players = PlayerController.create_player()

    for players in range[number_of_player]:
        PlayerController.create_player()
        players += 1
        
        

"""Si j'ai un tournoi ajouter un player et boucler 8 fois"""
