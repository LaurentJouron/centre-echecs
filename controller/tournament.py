"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController

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
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        player_name = TournamentView.append_player()
        player = PlayerController.get_player_by_name(player_name)
        tournament.append_players(player)

    # @staticmethod
    # def remove_player():
    #     """Remove player un tournament list"""
    #     player = TournamentView.remove_player()
    #     TournamentModel.append_players()
    #
    # @staticmethod
    # def display_players_list():
    #     """Display all participants of the tournament."""
    #     players_list = TournamentModel.display_players_list()
    #     return players_list
    #
    # @staticmethod
    # def alphabetical_order():
    #     """Display all participants in alphabetical order."""
    #     alphabetical_players = TournamentModel.alphabetical_order()
    #     return alphabetical_players
    #
    # @staticmethod
    # def ranking_order():
    #     """Display all participants in ranking order."""
    #     ranking_players = TournamentModel.ranking_order()
    #     return ranking_players