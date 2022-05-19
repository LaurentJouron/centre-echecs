"""Tournament player registration management."""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create():
        """Imports view data, imports model data and compares accuracy."""
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
        return PlayerModel.get_all()

    @staticmethod
    def remove():
        """Removes an item from the list"""
        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel(first_name=first_name,
                             last_name=last_name)
        player.remove()

    @staticmethod
    def get_player_by_name():
        """Get a player with his first-name"""
        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel(first_name=first_name,
                             last_name=last_name)
        return player.get_one

    @staticmethod
    def remove_player_list():
        """Removes an item from the list"""
        first_name = PlayerView.get_first_name()
        last_name = PlayerView.get_last_name()
        player = PlayerModel(first_name=first_name,
                             last_name=last_name)
        return player
