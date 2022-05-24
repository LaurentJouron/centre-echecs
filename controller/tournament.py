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
        nb_rounds = TournamentView.number_rounds()
        nb_players = TournamentView.number_players()

        tournament = TournamentModel(name=name,
                                     place=place,
                                     start_date=start_date,
                                     end_date=end_date,
                                     nb_rounds=nb_rounds,
                                     nb_players=nb_players)
        print(str(tournament))
        return tournament

    @staticmethod
    def number_players():
        """Get the number of players of this tournament."""
        number_of_players = TournamentView.number_players()
        return number_of_players

    @staticmethod
    def number_rounds():
        """Get the number of rounds of this tournament."""
        number_of_rounds = TournamentView.number_rounds()
        return number_of_rounds

    @staticmethod
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        if tournament is None:
            print("You need to create tournament before to add players.")
            return
        if tournament != "":
            player = PlayerController.get_one_player()
            tournament.append_player(player)

    @staticmethod
    def get_players_list(tournament):
        """Display all participants of the tournament."""
        print(tournament.get_players_list())

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = PlayerController.get_one_player()
        tournament.remove_player(player)
