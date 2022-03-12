"""Enter information for the tournament organization."""
from datetime import date
from datetime import timedelta

import constants

number_of_day: int = constants.NUMBER_OF_DAY


class TournamentView:
    """What information is needed for the tournament."""
    
    @staticmethod
    def organize_new_tournament():
        """Name the tournament."""
        name: str = input("Enter the name of the tournament: ").capitalize()
        
        """Where the tournament goes."""
        place: str = input("Venue of the tournament: ").capitalize()

        """On what date the tournament begins."""
        start_day: date = date.today()

        """Tournament end date."""
        end_date: date = start_day + timedelta(number_of_day)
        
        number_of_players: int = constants.NUMBER_OF_PLAYERS
        number_of_round: int = constants.NUMBER_OF_ROUND
        
        return [name, place, start_day, end_date, number_of_round,
                number_of_players]
