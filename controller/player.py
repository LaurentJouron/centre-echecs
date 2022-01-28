"""Tournament player registration management."""

from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create_player():
        player_data = PlayerView.new_player()
        player = PlayerModel(player_data[0],    # first_name
                             player_data[1],    # last_name
                             player_data[2],    # date_of_birth
                             player_data[3],    # gender
                             player_data[4])    # ranking
        return PlayerView.display_player(player)
        