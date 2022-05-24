# from model.player import PlayerModel
# from view.round import RoundView
from model.round import RoundModel
from controller.player import PlayerController


class RoundController:
    @staticmethod
    def append_player():
        """Returns the players to be added to the tournament list."""
        player = PlayerController.get_one_player()
        RoundModel.append_player(player)

    @staticmethod
    def get_players_list(tournament):
        """Display all participants of the tournament."""
        print(tournament.get_players_list())

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = PlayerController.remove_player_list()
        tournament.remove_player(player)
