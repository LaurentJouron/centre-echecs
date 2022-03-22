"""Tournament player registration management."""
from view.player import PlayerView
from model.player import PlayerModel


class PlayerController:
    """Control information player you need to organize a tournament."""

    @staticmethod
    def create():
        """Imports view data, imports model data and compares accuracy."""
        first_name, last_name, birthday, gender, ranking = \
            PlayerView.get_all_information()
        
        player = PlayerModel(first_name, last_name, birthday, gender, ranking)

        player.save()
        return player

    @staticmethod
    def get_all():
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
