"""Information of the chess tournament."""


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

    def __str__(self) -> str:
        """Confirmation phrase of the tournament class."""
        return f"The {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am and end on {self.end_date}" \
               f" at 6:00 pm.\n" \
               f"He takes place {self.place} with " \
               f"{self.number_of_players} players in" \
               f" {self.number_of_round} rounds.\n"
