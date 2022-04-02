"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel


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
        player = TournamentView.append_player()
        first_name = TournamentModel.append_players(player)
        return first_name


"""round"""
