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
        player: str = TournamentView.append_player()
        len_player: int = TournamentModel.__len__()
        if len_player < constants_players:
            first_name = TournamentModel.append_players(player)
            return first_name
        else:
            return f"The number of players is reached for this tournament."

    @staticmethod
    def remove_player():
        """Remove player un tournament list"""
        player = TournamentView.remove_player()
        if player in TournamentModel.remove_player(player):
            return player

    @staticmethod
    def display_players_list():
        """Display all participants of the tournament."""
        players_list = TournamentModel.display_players_list()
        return players_list

    @staticmethod
    def alphabetical_order():
        """Display all participants in alphabetical order."""
        alphabetical_players = TournamentModel.alphabetical_order()
        return alphabetical_players

    @staticmethod
    def ranking_order():
        """Display all participants in ranking order."""
        ranking_players = TournamentModel.ranking_order()
        return ranking_players