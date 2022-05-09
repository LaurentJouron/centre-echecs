"""Enter the information of the players who will participate."""
from datetime import datetime


class PlayerView:
    """The player information you need to organize a tournament."""
    
# player function
    @staticmethod
    def define_first_name():
        """Define the first-name of participants.
        Returns:
            str: players first-name """
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                print("Invalid first name")
                ValueError()
            else:
                return first_name.capitalize()
    
    @staticmethod
    def define_last_name():
        """Define the last_name of participants.
        Returns:
            str: players last-name """
        while True:
            last_name = input("Enter the last name: ")
            if not last_name.isalpha():
                print("Invalid name")
                ValueError()
            else:
                return last_name.capitalize()
    
    @staticmethod
    def define_birthday():
        """Define the birthday of participants.
        Returns:
            date: players birthday """
        birthday = input("Enter date of birth: ")
        birthday = datetime.strptime(birthday, "%d%m%Y"). \
            strftime("%A %d %B %Y")
        return birthday
    
    @staticmethod
    def define_gender():
        """Define the gender of participants.
        Returns:
            str: players gender """
        while True:
            gender = input("Select M for men or W for women: ")
            gender = gender.upper()
            if gender == "W":
                return "woman"
            elif gender == "M":
                return "man"
            else:
                gender = False
                if not gender:
                    print(f"Input error")
    
    @staticmethod
    def define_ranking():
        """Define the ranking of participants.
        Returns:
            int: players national ranking """
        while True:
            ranking = input("Indicate your place in the national ranking: ")
            if ranking < "1":
                print(f"Input error")
                ValueError()
            else:
                return ranking
    
    @staticmethod
    def display_all(players):
        """
        Display all players of the tournament.
        Param players: list of players
        return:
            print: information of players
        """
        for player in players:
            print(player)
    
    @staticmethod
    def remove():
        """Define the first-name of participants you want removed.
        Returns:
            str: players first-name """
        player = PlayerView.define_first_name()
        return player
    
# Header and footer decoration
# Title page
    @staticmethod
    def start_player_reception():
        """Reception to the player area title.
        Print:
            str: player_reception """
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, ' ')}")
        
    @staticmethod
    def create():
        """Player creation title.
        Print:
            str: player_creation """
        player_creation = " PLAYER CREATION "
        print(f"\n{player_creation.center(106, ' ')}")
        
    @staticmethod
    def all():
        """All list players display title.
        Print:
            str: all_player """
        all_player = " ALL PLAYERS IN LIST "
        print(f"\n{all_player.center(106, '~')}")

    @staticmethod
    def delete():
        """Remove player to list players title.
        Print:
            str: delete_player """
        delete_player = " PLAYER DELETE "
        print(f"\n{delete_player.center(106, ' ')}")

# Choice or information
    @staticmethod
    def choice():
        """Explains that you must choose between several options.
        Print:
            str: * choice * """
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def information():
        """Explains that you must choose to enter the information.
        Print:
            str: * information * """
        information = " Enter information "
        print(f"{information.center(106, '*')}")

# List of choice
    @staticmethod
    def player_menu():
        """lists of choices.
        Print:
            str: player_menu """
        player_menu = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{player_menu.center(106, '-')}")

    @staticmethod
    def validate_player():
        """lists of choices.
        Print:
            str: validate_player """
        validate_player = "> [1]Modify  [2]Validate <"
        print(f"\n{validate_player.center(106, '-')}")

# Input answer
    @staticmethod
    def input_str():
        """Select information what the manager need for organisation.
        Return:
            str: input_str """
        input_str = input(f"Please enter an information : ").capitalize()
        return input_str

    @staticmethod
    def input_int():
        """Selects the choice to access from the following menu.
        Return:
            int: input_int """
        input_int = input(f"Please enter an choice : ").capitalize()
        input_int = int(input_int)
        return input_int
