"""Enter information for the tournament organization."""
from datetime import date, timedelta

import constants

number_of_day = constants.NUMBER_OF_DAY


class TournamentView:
    """What information is needed for the tournament."""
    
    @staticmethod
    def name():
        """
        Generate a name the tournament.
        Returns:
            str: Tournament name
        """
        name: str = input("Enter the name of the tournament: ").capitalize()
        return name
    
    @staticmethod
    def place():
        """
        Generate place of the tournament.
        Returns:
            str: Tournament place
        """
        place: str = input("Venue of the tournament: ").capitalize()
        return place

    @staticmethod
    def start_date():
        """
        Generate the date the tournament begins.
        Returns:
            date: start tournament
        """
        start_date = date.today()
        return start_date
    
    @staticmethod
    def end_date(start_date):
        """
        Tournament end date.
        Agrs:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        end_date = start_date + timedelta(number_of_day)
        if end_date == start_date:
            return "same day"
        else:
            return end_date
        
    @staticmethod
    def players():
        """
        Take the number of players on the constant file.
        Returns:
            int: number of players
        """
        players = constants.NUMBER_OF_PLAYERS
        return players
    
    @staticmethod
    def rounds():
        """
        Take the number of rounds on the constant file.
        Returns:
            int: number of rounds
        """
        rounds = constants.NUMBER_OF_ROUND
        return rounds
        
    @staticmethod
    def get_all():
        """Groups all functions of the class.
        Returns:
            list: [name, place, start_date, end_date, players, rounds]
        """
        name = TournamentView.name()
        place = TournamentView.place()
        start_date = TournamentView.start_date()
        end_date = TournamentView.end_date(start_date)
        players = TournamentView.players()
        rounds = TournamentView.rounds()
        return name, place, start_date, end_date, players, rounds
        