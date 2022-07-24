"""Tournament player registration management."""
from datetime import datetime

from view.player import PlayerView as View
from model.player import PlayerModel as Model


class Player:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def player_menu():
        players = True
        while players:
            View.player_reception()
            View.select_choice()
            View.player_menu()

            select_player_menu = View.select_player_menu()
            choice_players_menu = int(select_player_menu)

            if choice_players_menu >= 5:
                View.value_error()

            if choice_players_menu == 1:
                """Input information for create player in data file."""
                Player.create()

            elif choice_players_menu == 2:
                """Display all players in data file."""
                all_players = Player
                print(all_players.get_all())

            elif choice_players_menu == 3:
                """Input information for delete player in data file."""
                Player.remove()

            elif choice_players_menu == 4:
                """Input information for exit the players menu."""
                players = False

    @staticmethod
    def get_first_name():
        """Define the first-name of participants.
        Returns:
            str: players first-name """
        while True:
            first_name = View.get_first_name()
            if not first_name.isalpha():
                View.input_error(first_name)
            else:
                return first_name
    
    @staticmethod
    def get_last_name():
        """Define the last_name of participants.
        Returns:
            str: players last-name """
        while True:
            last_name = View.get_last_name()
            if not last_name.isalpha():
                View.input_error(last_name)
            else:
                return last_name

    @staticmethod
    def get_birthday():
        """Define the birthday of participants.
        Returns:
            date: players birthday """
        while True:
            birthday = View.get_birthday()
            if not birthday.isdigit():
                View.input_error(birthday)
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
            gender = View.get_gender()
            gender = gender.upper()
            if gender == "W":
                return "woman"
            elif gender == "M":
                return "man"
            else:
                View.input_error(gender)

    @staticmethod
    def get_ranking():
        """Define the ranking of participants.
        Returns:
            int: players national ranking """
        while True:
            ranking = View.get_ranking()
            if not ranking.isdigit() or ranking <= "1":
                View.input_error(ranking)
            else:
                return ranking

    @staticmethod
    def create():
        """Imports view data, imports model data and compares accuracy."""
        View.player_creation()
        View.enter_information()

        first_name = View.get_first_name()
        last_name = View.get_last_name()
        birthday = View.get_birthday()
        gender = View.get_gender()
        ranking = View.get_ranking()

        player = Model(first_name=first_name,
                       last_name=last_name,
                       birthday=birthday,
                       gender=gender,
                       ranking=ranking)
        player.save()
        View.player_register(f"{first_name} {last_name}")
        return player

    @staticmethod
    def get_all():
        """Deserializes the database data in list comprehension."""
        View.all_players()
        View.display_all_players()
        return Model.get_all()

    @staticmethod
    def remove():
        """Removes an item from the list"""
        View.delete_players()
        View.enter_information()

        first_name = View.get_first_name()
        last_name = View.get_last_name()
        player = Model(first_name=first_name, last_name=last_name)
        player.remove()
        View.remove_confirmation(first_name, last_name)

    @staticmethod
    def get_one_player():
        """Get a player with his first-name"""
        first_name = View.get_first_name()
        last_name = View.get_last_name()
        player = Model.get_one_player(first_name=first_name, last_name=last_name)
        return player["first_name"], player["last_name"], player["birthday"], player["gender"], player["ranking"]

    @staticmethod
    def remove_player_list():
        """Removes an item from the list"""
        first_name = View.get_first_name()
        last_name = View.get_last_name()
        return Model(first_name=first_name, last_name=last_name)
