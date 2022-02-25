"""Tournament player registration management."""

from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""
    def __init__(self):
        self.player_view = PlayerView()

    def create_player(self):
        """Imports view data, imports model data and compares accuracy."""
        player_data = self.player_view.get_player_information()
        player = PlayerModel(player_data[0],    # first_name
                             player_data[1],    # last_name
                             player_data[2],    # birthday
                             player_data[3],    # gender
                             player_data[4])    # ranking
        return player
