"""All views informations for the players will participate."""
from datetime import datetime


class PlayerView:
    """The player information."""

# Function
    @staticmethod
    def get_first_name():
        """Define the first-name of participants.
        Returns:
            str: players first-name """
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                print("Invalid first name.\nSelect letters only")
            else:
                return first_name.capitalize()
    
    @staticmethod
    def get_last_name():
        """Define the last_name of participants.
        Returns:
            str: players last-name """
        while True:
            last_name = input("Enter the last name: ")
            if not last_name.isalpha():
                print("Invalid name.\nSelect letters only")
            else:
                return last_name.capitalize()
    
    @staticmethod
    def get_birthday():
        """Define the birthday of participants.
        Returns:
            date: players birthday """
        while True:
            birthday = input("Enter date of birth: ")
            if not birthday.isdigit():
                print("Invalid date entry.\nSelect number only")
            else:
                birthday = datetime.strptime(birthday, "%d%m%Y"). \
                    strftime("%A %d %B %Y")
                return birthday
    
    @staticmethod
    def get_gender():
        """Define the gender of participants.
        Returns:
            str: players gender """
        gender = ""
        while gender != "W" or "M":
            gender = input("Select M for men or W for women: ")
            gender = gender.upper()
            if gender == "W":
                return "woman"
            elif gender == "M":
                return "man"
            else:
                print(f"Value error.\nSelect M for man or W for women")
    
    @staticmethod
    def get_ranking():
        """Define the ranking of participants.
        Returns:
            int: players national ranking """
        while True:
            ranking = input("Indicate your place in the national ranking: ")
            if not ranking.isdigit() or ranking <= "1":
                print(f"Input error.\nSelect positif number only")
            else:
                return ranking

    @staticmethod
    def remove_confirmation(first_name, last_name):
        """player deletion confirmation phrase
        Print:
            str: player remove """
        print(f"\n{first_name} {last_name} has been deleted from the list.")

    @staticmethod
    def append_confirmation(first_name, last_name):
        """Display confirmation when the player is register in players file
        Print:
            str: player append """
        print(f"\n{first_name} {last_name} is register.")

# Title decoration text for players in line game.
    @staticmethod
    def player_reception():
        """Display the title decoration for player reception"""
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, ' ')}")

    @staticmethod
    def player_creation():
        """Display the title decoration for player creation"""
        player_creation = " PLAYER CREATION "
        print(f"\n{player_creation.center(106, ' ')}")

    @staticmethod
    def all_players():
        """Display the title decoration for all players"""
        all_player = " ALL PLAYERS IN LIST "
        print(f"\n{all_player.center(106, ' ')}")

    @staticmethod
    def delete_players():
        """Display the title decoration for delete player"""
        delete_player = " PLAYER DELETE "
        print(f"\n{delete_player.center(106, ' ')}")

# Player menu
    @staticmethod
    def player_menu():
        """Display menu players decoration"""
        player_menu = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{player_menu.center(106, '-')}")

# Input
    @staticmethod
    def select_player_menu():
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
        """Display choice decoration for player"""
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def display_all_players():
        """Display all players decoration"""
        information_decoration = " Display all players in list "
        print(f"{information_decoration.center(106, '*')}")

# Error
    @staticmethod
    def value_error():
        print("Value error.")
