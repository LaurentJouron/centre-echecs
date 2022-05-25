# from view.round import RoundView
from model.round import RoundModel
from controller.tournament import TournamentController


class RoundController:

    @staticmethod
    def tournament_players(tournament):
        all_players = TournamentController.get_players_list(tournament)
        print(RoundModel.append_player(tournament, all_players))
