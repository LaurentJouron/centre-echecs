"""Information of the chess tournament."""
from tinydb import TinyDB
from controller.tournament import TournamentController

""" Creation of the file for the tournament. """
db = TinyDB("data/tournament.json", indent=4)


class TournamentModel:
    """Information of the chess tournament."""
    def __init__(self, name, place, start_date, end_date, number_of_round,
                 number_of_players):
        
        """Builder of the model tournament."""
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.number_of_players = number_of_players
    
    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"The {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am and end on" \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place {self.place} with " \
               f"{self.number_of_players} players in {self.number_of_round} " \
               f"rounds.\n"

    @staticmethod
    def add_tournament():
        tournament = TournamentController.new_tournament()
        db.insert({"name": tournament.name,
                   "place": tournament.place,
                   "start_date": tournament.start_date,
                   "end_date": tournament.end_date,
                   "number_of_round": tournament.number_of_round,
                   "number_of_players": tournament.number_of_players})

    @staticmethod
    def display_tournament_information():
        for tournament in db:
            print(tournament)

    @staticmethod
    def delete_data_file():
        db.truncate()
