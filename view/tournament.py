"""Enter information for the tournament organization."""
from datetime import date, timedelta

import constants
nb_day = constants.NUMBER_OF_DAY


class TournamentView:
    """What information is needed for the tournament."""

# Function to create information from view.
    @staticmethod
    def name():
        """
        Generate a name tournament.
        Returns:
            str: name
        """
        while True:
            name: str = input("Enter the tournament name: ").capitalize()
            if not name.isalpha():
                print(f"Invalid name")
            else:
                return name

    @staticmethod
    def place():
        """
        Generate place of the tournament.
        Returns:
            str: place
        """
        while True:
            place: str = input("Place of the tournament: ").capitalize()
            if not place.isalpha():
                print("\nInvalid name!\nPlease input another name.\n")
            else:
                return place

    @staticmethod
    def start_date():
        """
        Generate the date the tournament begins.
        Returns:
            date: start
        """
        start_date = date.today()
        start_date = start_date.strftime("%A %d %B %Y")
        return start_date
    
    @staticmethod
    def end_date():
        """
        Tournament end date.
        :arguments:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        end_date = date.today() + timedelta(nb_day)
        if end_date == date.today():
            return "same day"
        else:
            return end_date.strftime("%A %d %B %Y")
