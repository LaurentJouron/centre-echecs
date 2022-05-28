"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel
from controller.player import PlayerController


class TournamentController:

    @staticmethod
    def tournament_menu():
        global_tournament = None
        tournament = True
        while tournament:
            TournamentView.tournament_reception()
            TournamentView.select_choice()
            TournamentView.tournament_menu()

            """Input the number choice of the tournament menu"""
            select_tournament_menu = TournamentView.select_menu()
            choice_tournament_menu = int(select_tournament_menu)

            if choice_tournament_menu >= 6:
                TournamentView.value_error()

            if choice_tournament_menu == 1:
                """Decoration text creation tournament for in line game."""
                TournamentView.tournament_creation()
                TournamentView.enter_information()

                """Input information for create tournament."""
                global_tournament = TournamentController.new_tournament()

            if choice_tournament_menu == 2:
                """Decoration text creation tournament for in line game."""
                TournamentView.append_tournament_player()
                TournamentView.enter_information()

                """Enter the information for a new tournament and assign 
                the global variable"""
                TournamentController.append_player(global_tournament)

            if choice_tournament_menu == 3:
                """Decoration text display all players in this tournament."""
                TournamentView.all_tournament_player()
                TournamentView.list_tournament_player()

                """Display all players in this tournament."""
                all_players = TournamentController
                print(all_players.get_players_list(global_tournament))

            if choice_tournament_menu == 4:
                """Decoration text delete player in this tournament."""
                TournamentView.remove_tournament_player()
                TournamentView.enter_information()

                """Input information for delete player in this tournament."""
                TournamentController.remove_player(global_tournament)

            if choice_tournament_menu == 5:
                tournament = False

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
        return tournament.get_players_list()

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = PlayerController.get_one_player()
        tournament.remove_player(player)
