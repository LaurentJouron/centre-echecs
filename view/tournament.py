"""Enter information for the tournament organization."""
from datetime import date, timedelta

import constants

nb_day = constants.NUMBER_OF_DAY
nb_players = constants.NUMBER_OF_PLAYERS
nb_round = constants.NUMBER_OF_ROUND


class TournamentView:
    """What information is needed for the tournament."""

# Function
    @staticmethod
    def name() -> str:
        """
        Generate a name tournament.
        Returns:
            str: name
        """
        while True:
            name: str = input("Enter the tournament name: ").capitalize()
            if not name.isalpha():
                print("Invalid name")
            else:
                return name

    @staticmethod
    def place() -> str:
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
    def start_date() -> str:
        """
        Generate the date the tournament begins.
        Returns:
            date: start
        """
        start_date = date.today()
        start_date = start_date.strftime("%A %d %B %Y")
        return start_date

    @staticmethod
    def end_date() -> str:
        """
        Tournament end date.
        :arguments:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        TournamentView.number_of_days()
        TournamentView.select_choice()

        print(f"\nThis tournament will play in {nb_day + 1} day(s).")

        TournamentView.validate_menu()

        today = TournamentView.start_date()
        validate = int(TournamentView.select_menu())
        if validate == 1:
            print(f"\nThis tournament will play in {nb_day + 1} days.")
            end_date = date.today() + timedelta(nb_day)
            if end_date == date.today():
                return "same day"
        elif validate == 2:
            new_days = input("\nHow many days ? ")
            new_number = int(new_days)
            print(f"\nThis tournament will play in {new_number} days.")
            end_date = today + timedelta(new_number - 1)
            return end_date.strftime("%A %d %B %Y")

    @staticmethod
    def number_rounds() -> int:
        """
        Generate number of rounds for the tournament.
        Returns:
            int: number of rounds
        """
        TournamentView.number_of_round()
        TournamentView.select_choice()

        print(f"\nThis tournament will play in {nb_round} rounds.")

        TournamentView.validate_menu()

        validate = int(TournamentView.select_menu())
        if validate == 1:
            print(f"\nThis tournament will play in {nb_round} rounds.")
            return nb_round
        if validate == 2:
            new_number = input("\nHow many round ? ")
            new_number = int(new_number)
            print(f"\nThis tournament will play in {new_number} rounds.")
            return new_number

    @staticmethod
    def number_players() -> int:
        """
        Generate number of player for the tournament.
        Returns:
            int: number of player
        """
        TournamentView.number_of_player()
        TournamentView.select_choice()

        print(f"\nThis tournament will play with {nb_players} players")

        TournamentView.validate_menu()

        validate = int(TournamentView.select_menu())
        if validate == 1:
            print(f"\nThis tournament will play with {nb_players} players.")
            return nb_players
        if validate == 2:
            new_number = input("\nHow many players ? ")
            new_number = int(new_number)
            print(f"\nThis tournament will play with {new_number} players.")
            return new_number

# Title decoration text for tournament in line game.
    @staticmethod
    def tournament_reception():
        """Display the title decoration for tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, ' ')}")

    @staticmethod
    def tournament_creation():
        """Display the title decoration for tournament creation"""
        tournament_creation = " TOURNAMENT CREATION "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def append_tournament_player():
        """Display the title decoration for tournament append player"""
        add_players = " APPEND TOURNAMENT PLAYERS "
        print(f"\n{add_players.center(106, ' ')}")

    @staticmethod
    def all_tournament_player():
        """Display the title decoration for tournament append player"""
        all_player = " ALL PLAYERS IN TOURNAMENT "
        print(f"\n{all_player.center(106, ' ')}")

    @staticmethod
    def remove_tournament_player():
        """Display the title decoration remove tournament player"""
        tournament_creation = " REMOVE PLAYERS TOURNAMENT "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def number_of_round():
        """Display the title decoration number round of this tournament"""
        number_rounds = " NUMBER ROUNDS "
        print(f"\n{number_rounds.center(106, ' ')}")

    @staticmethod
    def number_of_days():
        """Display the title decoration number days of this tournament"""
        number_days = " NUMBER DAYS "
        print(f"\n{number_days.center(106, ' ')}")

    @staticmethod
    def number_of_player():
        """Display the title decoration number players of this tournament"""
        number_players = " NUMBER PLAYERS "
        print(f"\n{number_players.center(106, ' ')}")
        
# Tournament reception menu
    @staticmethod
    def tournament_menu():
        """Display menu tournament decoration"""
        tournament_list = "> [1]Create  [2]Add player  [3]Display player  " \
                          "[4]Remove player  [5]Quit <"
        print(f"\n{tournament_list.center(106, '-')}")

    @staticmethod
    def validate_menu():
        """Display menu validate or change"""
        validate = "> [1]Validate  [2]Change <"
        print(f"\n{validate.center(106, '-')}")

# Input
    @staticmethod
    def select_menu():
        """Define the number of the menu you want.
        Returns:
            int: number that corresponds to the choice of the menu"""
        return input("Select the menu number : ")

# Instruction
    @staticmethod
    def enter_information():
        """Display information decoration for player"""
        information_decoration = " Enter information "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def select_choice():
        """Display choice decoration for tournament"""
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def list_tournament_player():
        """Display the title decoration for tournament all player"""
        information_decoration = " All players in the tournament"
        print(f"{information_decoration.center(106, '*')}")

# Error
    @staticmethod
    def value_error():
        print("Value error.")
