"""Management of the tournament organization"""
from tinydb import TinyDB, Query, where

from view.tournament import TournamentView
from model.tournament import TournamentModel


class TournamentController:
    db = TinyDB(f"data/players.json", indent=4)
    
    @staticmethod
    def new_tournament():
        """Imports view data, imports model data and compares accuracy."""
        name, place, start_date, end_date = TournamentView.get_all()
        
        tournament = TournamentModel(name, place, start_date, end_date)
        return tournament

    @staticmethod
    def append_player():
        """Returns the players to be added to the tournament list."""
        add_players = []
        db_players = TournamentController.db.all()
        for players in db_players:
            add_players.append(players)
        add_players = TournamentModel.append_players(add_players)
        print(add_players)

"""round"""
