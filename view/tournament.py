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
                print("\nInvalid name!\nPlease input another name.\n")
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
        player = input("Select first_name player you add: """).capitalize()
        return player

    @staticmethod
    def remove_player():
        """Define the first-name of participants you want to remove to the
        tournament.
        Returns:
            str: players first-name """
        player = input("Select first_name player you remove: """).capitalize()
        return player

# Decoration text
    @staticmethod
    def tournament_reception():
        """Management tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, '~')}")

    @staticmethod
    def tournament_menu():
        tournament_list = "> [1]Create  [2]Add player  [3]Display player  " \
                          "[4]Quit <"
        print(f"\n{tournament_list.center(106, '-')}")

    @staticmethod
    def tournament_validation():
        tournament_validation = " TOURNAMENT VALIDATION "
        print(f"\n{tournament_validation.center(106, '~')}")

    @staticmethod
    def validate_list():
        validate_list = "> [1]Modify  [2]Validate <"
        print(f"{validate_list.center(106, '-')}")

    @staticmethod
    def tournament_creation():
        tournament_creation = " TOURNAMENT CREATION "
        print(f"\n{tournament_creation.center(106, '~')}")

    @staticmethod
    def add_player():
        add_players = " REGISTER TOURNAMENT PLAYERS "
        print(f"\n{add_players.center(106, '~')}")

    @staticmethod
    def display_player():
        display_player = " DISPLAY TOURNAMENT PLAYERS "
        print(f"\n{display_player.center(106, '~')}")

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def input():
        choice = input(f"Please enter an choice : ").capitalize()
        choice = int(choice)
        return choice

    @staticmethod
    def reception_tournament():
        TournamentView.tournament_reception()
        TournamentView.choice()
        TournamentView.tournament_menu()
        TournamentView.input()

    @staticmethod
    def tournament_validate():
        TournamentView.tournament_validation()
        TournamentView.choice()
        TournamentView.validate_list()
        TournamentView.input()
