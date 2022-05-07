"""Information of the chess tournament."""
import constants

nb_game: int = constants.NUMBER_OF_PLAYERS//2   # Number of game in one round
nb_player: int = constants.NUMBER_OF_PLAYERS
nb_round: int = constants.NUMBER_OF_ROUND


class TournamentModel:
    """Builder of the model tournament."""
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
               f"{self.start_date} at 9:00 am, and end on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}."

    def append_player(self, player):
        """Adds players to the tournament list."""
        players = nb_player
        player_list = len(self.players)
        while player_list < players:
            self.players.append(player)
        else:
            print("Registration is complete for this tournament.")


    def remove_player(self, player):
        """Remove player in tournament list."""
        self.players.remove(player)

    def display_players_list(self):
        """Display players from tournament list."""
        return self.players[:]

    def alphabetical_order(self):
        """Sort players alphabetically"""
        self.players.sort()

    def ranking_order(self):
        """Sort players ranking"""
        self.players.sort(key=lambda ranking: self.players)

    def first_party(self):
        """Organize the first round player-to-player."""
        first_player: int = 0
        second_player: int = 4
        for _ in range(nb_game):
            first_tour = self.players[first_player::second_player]
            first_player += 1
            second_player += 1
            self.rounds.append([first_tour])

    def other_party(self):
        """Organizes player-to-player games for the remainder of the
        tournament """
        pass
