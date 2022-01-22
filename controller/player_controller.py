"""Tournament player registration management"""
from view.player_view import PlayerView
from model.player_model import PlayerModel


class PlayerController:
    """The player information you need to organize a tournament."""

    def create_player():
        create_player = PlayerView().create_player
        player = PlayerModel(create_player[0], create_player[1], create_player[2], create_player[3], create_player[4])
        return PlayerView.get_input_player(player)

