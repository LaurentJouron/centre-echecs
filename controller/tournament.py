"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController

import constants
constants_players = constants.NUMBER_OF_PLAYERS


class TournamentController:
    
    @staticmethod
    def tournament_reception():
        TournamentView.reception_tournament()
    
    @staticmethod
    def new_tournament():
        """Imports view data, imports model data and compares accuracy."""
        TournamentView.creation()
        name, place, start_date, end_date = TournamentView.get_all()
        tournament = TournamentModel(name, place, start_date, end_date)
        TournamentController.days_players_rounds()
        return tournament

    @staticmethod
    def days_players_rounds():
        nb_days = TournamentView.number_of_day()
        nb_players = TournamentView.number_of_player()
        nb_rounds = TournamentView.number_of_round()
        return nb_days, nb_players, nb_rounds
    
    @staticmethod
    def tournament_validate():
        validate = TournamentView.tournament_validate()
        return validate
    
    @staticmethod
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        player_name = TournamentView.append_player()
        player = PlayerController.get_player_by_name(player_name)
        tournament.append_player(player)

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = TournamentView.remove_player()
        tournament.remove_player(player)

    @staticmethod
    def display_players_list(tournament):
        """Display all participants of the tournament."""
        return tournament.display_players_list()
        
    @staticmethod
    def alphabetical_order(tournament):
        """Display all participants in alphabetical order."""
        return tournament.alphabetical_order()

    @staticmethod
    def ranking_order(tournament):
        """Display all participants in ranking order."""
        return tournament.ranking_order()
