"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController


class TournamentController:
        
    @staticmethod
    def new_tournament():
        """
        imports the data of the views
        and passes these data parameters in the models.
        """
        name = TournamentView.name()
        place = TournamentView.place()
        start_date = TournamentView.start_date()
        end_date = TournamentView.end_date()

        tournament = TournamentModel(name=name,
                                     place=place,
                                     start_date=start_date,
                                     end_date=end_date)
        print(str(tournament))
        return tournament

    @staticmethod
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        player_name = TournamentView.append_player()
        player = PlayerController.get_player_by_name(player_name)
        tournament.append_player(player)

    @staticmethod
    def get_players_list(tournament):
        """Display all participants of the tournament."""
        print(tournament.get_players_list())

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = TournamentView.remove_player()
        tournament.remove_player(player)
