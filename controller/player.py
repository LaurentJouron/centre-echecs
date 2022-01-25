"""Tournament player registration management"""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    def create_player():
        create_player = PlayerView
        player = PlayerModel(create_player[0],
                             create_player[1],
                             create_player[2],
                             create_player[3],
                             create_player[4])
        return PlayerView(player)
