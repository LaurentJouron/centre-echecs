"""Enter information for the tournament organization."""
from datetime import date
from datetime import timedelta

import constants

number_of_day = constants.NUMBER_OF_DAY


class TournamentView:
    """What information is needed for the tournament."""
    
    @staticmethod
    def information_for_tournament():
        """Name the tournament."""
        name: str = input("Enter the name of the tournament: ").capitalize()
    
        """Where the tournament goes."""
        place: str = input("Venue of the tournament: ").capitalize()

        """On what date the tournament begins."""
        start_date = date.today()
    
        """Tournament end date."""
        end_date = start_date + timedelta(number_of_day)
        number_of_round = constants.NUMBER_OF_ROUND
        number_of_players = constants.NUMBER_OF_PLAYERS

        return name, place, start_date, end_date, number_of_round, \
               number_of_players
