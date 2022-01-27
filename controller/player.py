"""Tournament player registration management"""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create_player():
        player_data = PlayerView.new_player()
        player = PlayerModel(player_data[0],
                             player_data[1],
                             player_data[2],
                             player_data[3],
                             player_data[4])
        return PlayerView.display_player(player)
        