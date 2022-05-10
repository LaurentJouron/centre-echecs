"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController


class TournamentController:

    @staticmethod
    def tournament_reception():
        TournamentView.tournament_reception()
        TournamentView.choice()
        TournamentView.tournament_menu()
        choice = TournamentView.input_int()
        return choice
        
    @staticmethod
    def new_tournament():
        """
        imports the data of the views
        and passes these data parameters in the models.
        """
        TournamentView.tournament_creation()
        TournamentView.information()

        name = TournamentView.name()
        place = TournamentView.place()
        start_date = TournamentView.start_date()
        end_date = TournamentView.end_date()

        tournament = TournamentModel(name, place, start_date, end_date)
        print(str(tournament))
        return tournament

    @staticmethod
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        TournamentView.add_player()
        TournamentView.information()
        player_name = TournamentView.append_player()
        player = PlayerController.get_player_by_name(player_name)
        tournament.append_player(player)

    @staticmethod
    def display_players_list(tournament):
        """Display all participants of the tournament."""
        return tournament.display_players_list()

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = TournamentView.remove_player()
        tournament.remove_player(player)

    # @staticmethod
    # def alphabetical_order(tournament):
    #     """Display all participants in alphabetical order."""
    #     return tournament.alphabetical_order()

    # @staticmethod
    # def ranking_order(tournament):
    #     """Display all participants in ranking order."""
    #     return tournament.ranking_order()

    # @staticmethod
    # def validate_number_rounds():
    #     TournamentView.number_rounds()
    #     TournamentView.choice()
    #     number_round = TournamentView.number_of_round()
    #     TournamentView.choice()
    #     nb_rounds = TournamentView.number_of_round()
    #     if nb_rounds == 1:
    #         return number_round
    #     return
    #
    # @staticmethod
    # def validate_number_days():
    #     TournamentView.number_days()
    #     TournamentView.choice()
    #     number_days = TournamentView.number_of_day()
    #     TournamentView.choice()
    #     nb_days = TournamentView.validate_list()
    #     if nb_days == 1:
    #         return number_days
    #
    # @staticmethod
    # def validate_number_players():
    #     TournamentView.number_players()
    #     TournamentView.choice()
    #     number_players = TournamentView.number_of_player()
    #     TournamentView.choice()
    #     nb_players = TournamentView.validate_list()
    #     if nb_players == 1:
    #         return number_players
