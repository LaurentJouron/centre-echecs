"""Enter information for the tournament organization."""
from datetime import date, timedelta

import constants

nb_day = constants.NUMBER_OF_DAY
nb_players = constants.NUMBER_OF_PLAYERS
nb_round = constants.NUMBER_OF_ROUND


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
        number_days = " NUMBER DAYS "
        print(f"\n{number_days.center(106, ' ')}")

        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

        print(f"\nThis tournament will play in {nb_day + 1} day(s).")

        validate_days = "> [1]Validate  [2]Change <"
        print(f"\n{validate_days.center(106, '-')}")

        today = TournamentView.start_date()

        validate = input("Do you want to change the number of days ? ")
        validate = int(validate)
        if validate == 1:
            print(f"\nThis tournament will play in {nb_day + 1} days.")
            end_date = date.today() + timedelta(nb_day)
            if end_date == date.today():
                return "same day"
        if validate == 2:
            new_days = input("\nHow many days ? ")
            new_number = int(new_days)
            print(f"\nThis tournament will play in {new_number} days.")
            end_date = today + timedelta(new_number - 1)
            return end_date.strftime("%A %d %B %Y")

    @staticmethod
    def number_players():
        """
        Generate number of player for the tournament.
        Returns:
            int: number of player
        """

        number_players = " NUMBER PLAYERS "
        print(f"\n{number_players.center(106, ' ')}")

        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

        print(f"\nThis tournament will play with {nb_players} players")

        validate_players = "> [1]Validate  [2]Change <"
        print(f"\n{validate_players.center(106, '-')}")

        validate = input("Do you want to change the number of player ? ")
        validate = int(validate)
        if validate == 1:
            print(f"\nThis tournament will play with {nb_players} players.")
            return nb_players
        if validate == 2:
            new_number = input("\nHow many players ? ")
            new_number = int(new_number)
            print(f"\nThis tournament will play with {new_number} players.")
            return new_number

    @staticmethod
    def number_rounds():
        """
        Generate number of rounds for the tournament.
        Returns:
            int: number of rounds
        """

        number_rounds = " NUMBER ROUNDS "
        print(f"\n{number_rounds.center(106, ' ')}")

        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

        print(f"\nThis tournament will play in {nb_round} rounds.")

        validate_rounds = "> [1]Validate  [2]Change <"
        print(f"\n{validate_rounds.center(106, '-')}")

        validate = input("Do you want to change the number of rounds ? ")
        validate = int(validate)
        if validate == 1:
            print(f"\nThis tournament will play in {nb_round} rounds.")
            return nb_round
        if validate == 2:
            new_number = input("\nHow many round ? ")
            new_number = int(new_number)
            print(f"\nThis tournament will play in {new_number} rounds.")
            return new_number
