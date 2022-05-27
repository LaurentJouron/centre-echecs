"""Tournament player registration management."""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def player_menu():
        players = True
        while players:
            PlayerView.player_reception()
            PlayerView.select_choice()
            PlayerView.player_menu()

            select_player_menu = PlayerView.select_player_menu()
            choice_players_menu = int(select_player_menu)

            if choice_players_menu >= 5:
                PlayerView.value_error()

            if choice_players_menu == 1:
                """Input information for create player in data file."""
                PlayerController.create()

            if choice_players_menu == 2:
                """Display all players in data file."""
                all_players = PlayerController
                print(str(all_players.get_all()))

            if choice_players_menu == 3:
                """Input information for delete player in data file."""
                PlayerController.remove()

            if choice_players_menu == 4:
                """Input information for exit the players menu."""
                players = False

    @staticmethod
    def create():
        """Imports view data, imports model data and compares accuracy."""
        PlayerView.player_creation()
        PlayerView.enter_information()

        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        birthday = PlayerView.get_birthday()
        gender = PlayerView.get_gender()
        ranking = PlayerView.get_ranking()

        player = PlayerModel(first_name=first_name,
                             last_name=last_name,
                             birthday=birthday,
                             gender=gender,
                             ranking=ranking)
        player.save()
        print(str(player))
        return player

    @staticmethod
    def get_all():
        """Deserializes the database data in list comprehension."""
        PlayerView.all_players()
        PlayerView.display_all_players()

        return PlayerModel.get_all()

    @staticmethod
    def remove():
        """Removes an item from the list"""
        PlayerView.delete_players()
        PlayerView.enter_information()

        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel(first_name=first_name,
                             last_name=last_name)
        player.remove()
        PlayerView.remove_confirmation(first_name, last_name)

    @staticmethod
    def get_one_player():
        """Get a player with his first-name"""
        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel.get_one_player(first_name=first_name,
                                            last_name=last_name)
        one_player = (player["first_name"],
                      player["last_name"],
                      player["birthday"],
                      player["gender"],
                      player["ranking"])
        return one_player

    @staticmethod
    def remove_player_list():
        """Removes an item from the list"""
        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel(first_name=first_name,
                             last_name=last_name)
        return player
