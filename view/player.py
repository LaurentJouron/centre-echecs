"""Enter the information of the players who will participate."""
from datetime import datetime


class PlayerView:
    """The player information you need to organize a tournament."""
    
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
    def get_all_information():
        """
        Groups all fonction of the class.
        Returns:
             list: [first_name, last_name, birthday, gender, ranking]
        """
        first_name = PlayerView.define_first_name()
        last_name = PlayerView.define_last_name()
        birthday = PlayerView.define_birthday()
        gender = PlayerView.define_gender()
        ranking = PlayerView.define_ranking()
        return first_name, last_name, birthday, gender, ranking
    
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

    @staticmethod
    def start_player_reception():
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, '~')}")

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def player_menu():
        list_of_choice = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")

    @staticmethod
    def input():
        choice = input(f"Please enter an choice : ").capitalize()
        choice = int(choice)
        return choice

    @staticmethod
    def create():
        player_creation = " PLAYER CREATION "
        print(f"\n{player_creation.center(106, '~')}")

    @staticmethod
    def information():
        choice = " Enter information "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def confirmation(player):
        print(repr(player))

    @staticmethod
    def all():
        all_player = " ALL PLAYERS IN LIST "
        print(f"\n{all_player.center(106, '~')}")

    @staticmethod
    def delete():
        delete_player = " PLAYER DELETE "
        print(f"\n{delete_player.center(106, '~')}")
