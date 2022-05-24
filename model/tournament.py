"""Information of the chess tournament."""


class TournamentModel:
    """Builder of the model tournament."""
    def __init__(self, name, place, start_date, end_date, nb_rounds,
                 nb_players):
        self.name: str = name
        self.place: str = place
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.nb_rounds: int = nb_rounds
        self.nb_players: int = nb_players
        self.players: list = []
        self.rounds: list = []

    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"\nThe {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am, and end on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}.\n" \
               f"It will be played with {self.nb_players} players in " \
               f"{self.nb_rounds} rounds."

    @property
    def half_nb_players(self):
        return int(self.nb_players/2)

    def append_player(self, player):
        """Adds players to the tournament list."""
        if len(self.players) < self.nb_players:
            self.players.append(player)
        else:
            print("This tournament is completed")

    def get_players_list(self):
        """Display players from tournament list."""
        return self.players[:]

    def remove_player(self, player):
        """Remove player in tournament list."""
        self.players.remove(player)

    # def first_party(self):
    #     """Organize the first round player-to-player."""
    #     first_player: int = 0
    #     second_player: int = self.half_nb_players
    #     for _ in range(self.half_nb_players):
    #         first_tour = self.players[first_player::second_player]
    #         first_player += 1
    #         second_player += 1
    #         self.rounds.append([first_tour])
    #     print(self.rounds)
