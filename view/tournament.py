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
        while True:
            name: str = input("Enter the tournament name: ").capitalize()
            if not name.isalpha():
                print(f"Invalid name")
                ValueError()
            else:
                return name

    @staticmethod
    def place():
        """
        Generate place of the tournament.
        Returns:
            str: Tournament place
        """
        while True:
            place: str = input("Place of the tournament: ").capitalize()
            if not place.isalpha():
                print("Invalid place name")
                ValueError()
            else:
                return place

    @staticmethod
    def start_date():
        """
        Generate the date the tournament begins.
        Returns:
            date: start tournament
        """
        start_date = date.today()
        start_date = start_date.strftime("%A %d %B %Y")
        return start_date
    
    @staticmethod
    def end_date():
        """
        Tournament end date.
        Agrs:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        end_date = date.today() + timedelta(number_of_day)
        if end_date == date.today():
            return "same day"
        else:
            return end_date.strftime("%A %d %B %Y")
        
    @staticmethod
    def get_all():
        """Groups all functions of the class.
        Returns:
            list: [name, place, start_date, end_date, players, rounds]
        """
        name = TournamentView.name()
        place = TournamentView.place()
        start_date = TournamentView.start_date()
        end_date = TournamentView.end_date()
        return name, place, start_date, end_date
    
    @staticmethod
    def append_player():
        """Define the first-name of participants you want to add to the
        tournament.
        Returns:
            str: players first-name """
        player = input("Please select first_name player you add: """).capitalize()
        return player

    @staticmethod
    def remove_player():
        """Define the first-name of participants you want to remove to the
        tournament.
        Returns:
            str: players first-name """
        player = input("Please select first_name player you remove: """).capitalize()
        return player