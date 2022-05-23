"""Information of the chess tournament."""


class TournamentModel:
    """Builder of the model tournament."""
    def __init__(self, name, place, start_date, end_date):
        self.name: str = name
        self.place: str = place
        self.start_date: str = start_date
        self.end_date: str = end_date

    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"\nThe {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am, and end on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}.\n" \
