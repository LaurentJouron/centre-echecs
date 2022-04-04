"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel

import constants
constants_players = constants.NUMBER_OF_PLAYERS


class TournamentController:

    @staticmethod
    def new_tournament():
        """Imports view data, imports model data and compares accuracy."""
        name, place, start_date, end_date = TournamentView.get_all()
        
        tournament = TournamentModel(name, place, start_date, end_date)
        return tournament
        
    @staticmethod
    def append_player():
        """Returns the players to be added to the tournament list."""
        len_player = TournamentModel.__len__()
        if len_player < constants_players:
            player = TournamentView.append_player()
            first_name = TournamentModel.append_players(player)
            return first_name
        else:
            return f"The number of players is reached for this tournament."


"""round"""
