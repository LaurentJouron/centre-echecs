"""Information of the chess tournament."""


class TournamentModel:
    """Information of the chess tournament."""

    def __init__(self, name, place, start_date, end_date, rounds, players):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players

    def def_all_information_of_tournament(self):
        """Get the information of a tournament."""
        return self.name + " " +\
            self.place + " " +\
            self.start_date + " " + \
            self.end_date + " " +\
            self.rounds + " " +\
            self.players
