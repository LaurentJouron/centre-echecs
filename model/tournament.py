"""Information of the chess tournament."""
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage
from controller.tournament import TournamentController


class TournamentModel:
    """Information of the chess tournament."""

    def __init__(self, name, place, start_day, end_date, number_of_round,
                 number_of_players):
        """Builder of the model tournament."""
        self.name = name
        self.place = place
        self.start_day = start_day
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.number_of_players = number_of_players

    def __str__(self) -> str:
        """Confirmation phrase of the tournament class."""
        return f"The {self.name} chess tournament starts on " \
               f"{self.start_day} at 9:00 am and end on {self.end_date}" \
               f" at 6:00 pm.\n" \
               f"He takes place {self.place} with " \
               f"{self.number_of_players} players in" \
               f" {self.number_of_round} rounds.\n"

    def add_tournament_file(self):
        """ In file"""
        db = TinyDB('chess-center.json', indent=4)
        TournamentController.new_tournament()
        db.insert({"name": self.name,
                   "place": self.place,
                   "start_date": self.start_day,
                   "end_date": self.end_date,
                   "number_of_players": self.number_of_players,
                   "number_of_rounds": self.number_of_round})
