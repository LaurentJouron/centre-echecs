"""Enter information for the tournament organization."""
from datetime import date, timedelta

import constants
nb_day = constants.NUMBER_OF_DAY
nb_player: int = constants.NUMBER_OF_PLAYERS
nb_round: int = constants.NUMBER_OF_ROUND


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
        Agrs:
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
    
    @staticmethod
    def number_of_day():
        number_day = constants.NUMBER_OF_DAY + 1
        print(f"\nThe tournament is planned on {number_day} day(s).")
        TournamentView.validate_list()
        choice = input(f"Please enter an choice : ")
        choice = int(choice)
        if choice == 1:
            new_number_day = input("How many days ? ")
            nbr_day = int(new_number_day) - 1
            print(f"The tournament will last {new_number_day} days ")
            return nbr_day
        return number_day
    
    @staticmethod
    def number_of_player():
        number_players = constants.NUMBER_OF_PLAYERS
        print(f"\nThe tournament is planned with {number_players} players.")
        TournamentView.validate_list()
        choice = input(f"Please enter an choice : ")
        choice = int(choice)
        if choice == 1:
            new_number_players = input("How many players ? ")
            new_number_players = int(new_number_players)
            print(f"The tournament will be held with {new_number_players} "
                  f"players ")
            return new_number_players
        return number_players

    @staticmethod
    def number_of_round():
        number_round = constants.NUMBER_OF_ROUND
        print(f"\nThe tournament is planned in {number_round} rounds.")
        TournamentView.validate_list()
        choice = input(f"Please enter an choice : ")
        choice = int(choice)
        if choice == 1:
            new_number_rounds = input("How many rounds ? ")
            number_round = int(new_number_rounds)
            print(f"The tournament will take place over {number_round} "
                  f"rounds. ")
            return number_round
        if choice == 2:
            return number_round

# Decoration list of choice for the command line game.
    @staticmethod
    def tournament_menu():
        tournament_list = "> [1]Create  [2]Add player  [3]Display player  " \
                          "[4]Quit <"
        print(f"\n{tournament_list.center(106, '-')}")

    @staticmethod
    def validate_list():
        validate_list = "> [1]Modify  [2]Validate <"
        print(f"\n{validate_list.center(106, '-')}")

# Decoration title for the command line game.
    @staticmethod
    def tournament_reception():
        """Management tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, ' ')}")

    @staticmethod
    def tournament_creation():
        tournament_creation = " TOURNAMENT CREATION "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def tournament_validation():
        tournament_validation = " TOURNAMENT VALIDATION "
        print(f"\n{tournament_validation.center(106, ' ')}")

    @staticmethod
    def add_player():
        add_players = " APPEND TOURNAMENT PLAYERS "
        print(f"\n{add_players.center(106, ' ')}")

    @staticmethod
    def display_player():
        display_player = " DISPLAY TOURNAMENT ROUNDS "
        print(f"\n{display_player.center(106, ' ')}")

    @staticmethod
    def number_days():
        number_days = " VALIDATE THE NUMBER DAYS "
        print(f"\n{number_days.center(106, ' ')}")

    @staticmethod
    def number_players():
        number_player = " VALIDATE THE NUMBER PLAYERS "
        print(f"\n{number_player.center(106, ' ')}")
        
    @staticmethod
    def number_rounds():
        number_rounds = " VALIDATE THE NUMBER ROUNDS "
        print(f"\n{number_rounds.center(106, ' ')}")

# Decoration need to do for the command line game.
    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")
        
    @staticmethod
    def information():
        choice = " Enter information "
        print(f"{choice.center(106, '*')}")

# Decoration enter integer for the command line game.
    @staticmethod
    def input_int():
        input_int = input(f"Please enter an choice : ")
        input_int = int(input_int)
        return input_int

# Decoration enter string for the command line game.
    @staticmethod
    def input_str():
        input_str = input(f"Please enter an information : ").capitalize()
        return input_str
