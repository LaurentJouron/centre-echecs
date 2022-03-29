"""Information of the chess tournament."""


class TournamentModel:
    """Builder of the model tournament."""
    def __init__(self, name, place, start_date, end_date):
        self.name: str = name
        self.place: str = place
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.players = []
        self.rounds = []
    
    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"\nThe {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am, and end, on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}.\n"

    def modify(self):
        pass

    def append_player(self):
        return self.players.append(self.players)
    
"""méthode qui permet d'ajouter un player dans le tableau des players"""
"""Une méthode qui ajoute un tour dans le tableau des tours"""
