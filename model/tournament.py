"""Information of the chess tournament."""
from tinydb import TinyDB, where


class TournamentModel:
    """Builder of the model tournament."""
    db = TinyDB(f"data/players.json", indent=4)
    
    def __init__(self, name, place, start_date, end_date):
        self.name: str = name
        self.place: str = place
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.players: list = []
        self.rounds: list = []

    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"\nThe {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am, and end, on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}.\n"

    def __len__(self):
        """Number of player in tournament list."""
        return len(self.players)
    # return __len__

    def append_players(self, player):
        """Adds players to the tournament list."""
        player = TournamentModel.db.search(where('first-name' == player))
        self.players.append(player)
    # __add__

    def remove_player(self, player):
        """Remove player in tournament list."""
        self.players.remove(player)

    def display_players_list(self):
        """Display players from tournament list."""
        return self.players[:]
    # return TournamentModel.__class__.__dict__

    def alphabetical_order(self):
        """Sort players alphabetically"""
        self.players.sort()

    def ranking_order(self):
        """Sort players ranking"""
        self.players.sort(key=lambda ranking: self.players)


"""Une méthode qui ajoute un tour dans le tableau des tours"""
