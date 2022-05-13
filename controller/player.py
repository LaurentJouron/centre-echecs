"""Tournament player registration management."""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create():
        """Imports view data, imports model data and compares accuracy."""
        first_name = PlayerView.define_first_name()
        last_name = PlayerView.define_last_name()
        birthday = PlayerView.define_birthday()
        gender = PlayerView.define_gender()
        ranking = PlayerView.define_ranking()
        
        player = PlayerModel(first_name, last_name, birthday, gender, ranking)
        player.save()
        print(repr(player))
        return player
    
    @staticmethod
    def get_all():
        """Deserializes the database data."""
        players_model = []
        players = PlayerModel.get_all()
        for player in players:
            players = PlayerModel(player["first-name"],
                                  player["last-name"],
                                  player["birthday"],
                                  player["gender"],
                                  player["ranking"])
            players_model.append(players)
        return PlayerView.display_all(players_model)
    
    @staticmethod
    def remove():
        """Removes an item from the list"""
        player = PlayerView.remove()
        return PlayerModel.remove(player)
    
    @staticmethod
    def get_player_by_name(player_name):
        """Get a player with his first-name"""
        player = PlayerModel.get_one_player(player_name)
        one_player = PlayerModel(player["first-name"],
                                 player["last-name"],
                                 player["birthday"],
                                 player["gender"],
                                 player["ranking"])
        return one_player
