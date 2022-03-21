"""Tournament player registration management."""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create_player():
        """Imports view data, imports model data and compares accuracy."""
        first_name, last_name, birthday, gender, ranking = \
            PlayerView.get_all_information()
        
        player = PlayerModel(first_name, last_name, birthday, gender, ranking)
        
        return player
