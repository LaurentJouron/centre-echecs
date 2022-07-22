"""All views information for the players will participate."""


class PlayerView:
    """The player information."""
    def __init__(self):
        pass

    @staticmethod
    def get_first_name():
        return input("Please enter the player’s first name: ").capitalize()
        
    @staticmethod
    def get_last_name():
        return input("Enter the last name: ").capitalize()
    
    @staticmethod
    def get_birthday():
        return input("Enter date of birth: ")
    
    @staticmethod
    def get_gender():
        return input("Select M for men or W for women: ")
    
    @staticmethod
    def get_ranking():
        return input("Indicate your place in the national ranking: ")

    @staticmethod
    def remove_confirmation(first_name, last_name):
        print(f"\n{first_name} {last_name} has been deleted from the list.")

    @staticmethod
    def player_register(full_name):
        print(f'{full_name} is register.')

    @staticmethod
    def player_reception():
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, ' ')}")

    @staticmethod
    def player_creation():
        player_creation = " PLAYER CREATION "
        print(f"\n{player_creation.center(106, ' ')}")

    @staticmethod
    def all_players():
        all_player = " ALL PLAYERS IN LIST "
        print(f"\n{all_player.center(106, ' ')}")

    @staticmethod
    def delete_players():
        """Display the title decoration for delete player"""
        delete_player = " PLAYER DELETE "
        print(f"\n{delete_player.center(106, ' ')}")

    @staticmethod
    def player_menu():
        player_menu = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{player_menu.center(106, '-')}")

    @staticmethod
    def select_player_menu():
        return input("Select the menu number : ")

    @staticmethod
    def enter_information():
        information_decoration = " Enter information "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def select_choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def display_all_players():
        information_decoration = " Display all players in list "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def value_error():
        print("Value error.")

    @staticmethod
    def input_error(var):
        print(f"Invalid input: {var}. Please try again.")
