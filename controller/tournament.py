"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel

import constants
number_of_player = constants.NUMBER_OF_PLAYERS


class TournamentController:
    @staticmethod
    def new_tournament():
        """Imports view data, imports model data and compares accuracy."""
        name, place, start_date, end_date = TournamentView.get_all()
        
        tournament = TournamentModel(name, place, start_date, end_date)
        return tournament

    @staticmethod
    def append_player():
        players = []
        number_player = TournamentView.append_player()
        player = TournamentModel.get_all()
        while len(players) < number_player:
            players.append(player)
            return players

"""players, rounds"""
