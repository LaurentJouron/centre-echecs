"""Enter information for the tournament organization."""
from datetime import date
from datetime import timedelta
import constants

number_of_day: int = constants.NUMBER_OF_DAY
number_of_round: int = constants.NUMBER_OF_ROUND
number_of_players: int = constants.NUMBER_OF_PLAYERS


class TournamentView:
    """What information is needed for the tournament."""

    @staticmethod
    def get_information_of_tournament():
        """Name the tournament."""
        name: str = input("Enter the name of the tournament: ").capitalize()

        """Where the tournament goes."""
        place: str = input("Venue of the tournament: ").capitalize()

        """On what date the tournament begins."""
        start_date: date = date.today()

        """Tournament end date."""
        end_date: date = start_date + timedelta(number_of_day)

        return name, place, start_date, end_date, number_of_round,\
               number_of_players
