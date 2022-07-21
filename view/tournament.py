"""Enter information for the tournament organization."""
from datetime import date


class TournamentView:
    """What information is needed for the tournament."""

    @staticmethod
    def name() -> str:
        return input("Enter the tournament name: ").capitalize()

    @staticmethod
    def place() -> str:
        return input("Place of the tournament: ").capitalize()

    @staticmethod
    def start_date() -> date:
        return date.today()

    @staticmethod
    def end_date() -> int:
        return int(TournamentView.select_menu())

    @staticmethod
    def during_time(nb_day):
        print(f"\nThis tournament will play in {nb_day + 1} day(s).")
        
    @staticmethod
    def how_many_day() -> str:
        return input("How many days ? ")
        
    @staticmethod
    def number_of_players(nb_players):
        print(f"\nThis tournament will play with {nb_players} players")

    @staticmethod
    def number_of_rounds(nb_rounds):
        print(f"\nThis tournament will play in {nb_rounds} rounds.")
        
    @staticmethod
    def number_rounds() -> str:
        return input("\nHow many round ? ")

    @staticmethod
    def how_many_rounds() -> str:
        return input("How many rounds ? ")

    @staticmethod
    def decoration_text_tournament_reception():
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, ' ')}")

    @staticmethod
    def decoration_text_tournament_creation():
        tournament_creation = " TOURNAMENT CREATION "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def decoration_text_append_tournament_player():
        add_players = " APPEND TOURNAMENT PLAYERS "
        print(f"\n{add_players.center(106, ' ')}")

    @staticmethod
    def decoration_text_all_tournament_player():
        all_player = " ALL PLAYERS IN TOURNAMENT "
        print(f"\n{all_player.center(106, ' ')}")

    @staticmethod
    def decoration_text_remove_tournament_player():
        tournament_creation = " REMOVE PLAYERS TOURNAMENT "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def decoration_text_number_of_round():
        number_rounds = " NUMBER ROUNDS "
        print(f"\n{number_rounds.center(106, ' ')}")

    @staticmethod
    def decoration_text_number_of_days():
        number_days = " NUMBER DAYS "
        print(f"\n{number_days.center(106, ' ')}")

    @staticmethod
    def decoration_text_number_of_player():
        number_players = " NUMBER PLAYERS "
        print(f"\n{number_players.center(106, ' ')}")

    @staticmethod
    def tournament_menu():
        tournament_list = "> [1]Create  [2]Add player  [3]Display player  " \
                          "[4]Remove player  [5]Quit <"
        print(f"\n{tournament_list.center(106, '-')}")

    @staticmethod
    def validate_menu():
        validate = "> [1]Validate  [2]Change <"
        print(f"\n{validate.center(106, '-')}")

    @staticmethod
    def select_menu():
        return input("Select the menu number : ")

    @staticmethod
    def enter_information():
        information_decoration = " Enter information "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def decoration_text_select_choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def decoration_text_list_tournament_player():
        information_decoration = " All players in the tournament"
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def value_error():
        print("Value error.")

    @staticmethod
    def input_error(var):
        print(f"Invalid input: {var}.\nPlease try again.")
