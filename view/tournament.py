"""Enter information for the tournament organization."""


class TournamentView:

    @staticmethod
    def name() -> str:
        return input("Enter the tournament name: ").capitalize()

    @staticmethod
    def place():
        return input("Place of the tournament: ").capitalize()

    @staticmethod
    def how_many_day():
        return input("\nHow many days ? ")

    @staticmethod
    def number_of_the_day(nb_day):
        print(f"\nThis tournament will play in {nb_day} day(s).")

    @staticmethod
    def same_day():
        print("same day")

    @staticmethod
    def how_many_players():
        return input("\nHow many players ? ")

    @staticmethod
    def number_of_the_players(nb_players):
        print(f"\nThis tournament will play with {nb_players} players")

    @staticmethod
    def how_many_rounds():
        return input("\nHow many round ? ")

    @staticmethod
    def number_of_the_rounds(nb_round):
        print(f"\nThis tournament will play in {nb_round} rounds.")

    @staticmethod
    def create_tournament_before_add_players():
        print("You need to create tournament before to add players.")

# Title decoration text
    @staticmethod
    def title_decoration_tournament_reception():
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, ' ')}")

    @staticmethod
    def title_decoration_tournament_creation():
        tournament_creation = " TOURNAMENT CREATION "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def title_decoration_append_tournament_player():
        add_players = " APPEND TOURNAMENT PLAYERS "
        print(f"\n{add_players.center(106, ' ')}")

    @staticmethod
    def title_decoration_all_tournament_player():
        all_player = " ALL PLAYERS IN TOURNAMENT "
        print(f"\n{all_player.center(106, ' ')}")

    @staticmethod
    def title_decoration_remove_tournament_player():
        tournament_creation = " REMOVE PLAYERS TOURNAMENT "
        print(f"\n{tournament_creation.center(106, ' ')}")

    @staticmethod
    def title_decoration_number_of_round():
        number_rounds = " NUMBER ROUNDS "
        print(f"\n{number_rounds.center(106, ' ')}")

    @staticmethod
    def title_decoration_number_of_days():
        number_days = " NUMBER DAYS "
        print(f"\n{number_days.center(106, ' ')}")

    @staticmethod
    def title_decoration_number_of_player():
        number_players = " NUMBER PLAYERS "
        print(f"\n{number_players.center(106, ' ')}")

# List decoration
    @staticmethod
    def list_decoration_tournament_menu():
        tournament_list = "> [1]Create  [2]Add player  [3]Display player  " \
                          "[4]Remove player  [5]Quit <"
        print(f"\n{tournament_list.center(106, '-')}")

    @staticmethod
    def list_decoration_validate_menu():
        validate = "> [1]Validate  [2]Change <"
        print(f"\n{validate.center(106, '-')}")

# Input number
    @staticmethod
    def input_number_form_list_decoration():
        return input("Select the menu number : ")

# Instruction
    @staticmethod
    def instruction_enter_information():
        information_decoration = " Enter information "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def instruction_select_choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def instruction_list_tournament_player():
        information_decoration = " All players in the tournament"
        print(f"{information_decoration.center(106, '*')}")

# Error
    @staticmethod
    def value_error():
        print("Value error.")

    @staticmethod
    def input_error(var):
        print(f"Invalid input: {var}. Please try again.")
