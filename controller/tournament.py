"""Management of the tournament organization"""
from datetime import date, timedelta

from view.tournament import TournamentView as View
from model.tournament import TournamentModel as Model
from controller.player import Player

import constants
nb_of_day = constants.NUMBER_OF_DAY
nb_of_players = constants.NUMBER_OF_PLAYERS
nb_of_round = constants.NUMBER_OF_ROUND


class Tournament:

    @staticmethod
    def tournament_menu():
        global_tournament = None

        tournament = True
        while tournament:
            """Decoration text reception tournament for in line game."""
            View.title_decoration_tournament_reception()
            View.instruction_select_choice()
            View.list_decoration_tournament_menu()

            """
            Input the number choice of the tournament menu.
            """
            select_tournament_menu = View.input_number_form_list_decoration()
            choice_tournament_menu = int(select_tournament_menu)

            if choice_tournament_menu >= 6:
                View.value_error()

            if choice_tournament_menu == 1:
                """Decoration text creation tournament for in line game."""
                View.title_decoration_tournament_creation()
                View.instruction_enter_information()

                """
                Input information for create tournament
                and assign the global variable.
                """
                global_tournament = Tournament.new_tournament()

            elif choice_tournament_menu == 2:
                """Decoration to add players tournament for in line game."""
                View.title_decoration_append_tournament_player()
                View.instruction_enter_information()

                """
                Enter the players information for add to the tournament.
                :parameter global variable tournament.
                """
                Tournament.append_player(global_tournament)

            elif choice_tournament_menu == 3:
                """Decoration text display all players in this tournament."""
                View.title_decoration_all_tournament_player()
                View.instruction_list_tournament_player()

                """
                Display all players in this tournament.
                :parameter global variable tournament.
                """
                all_players = Tournament
                print(all_players.get_players_list(global_tournament))

            elif choice_tournament_menu == 4:
                """Decoration text delete player in this tournament."""
                View.title_decoration_remove_tournament_player()
                View.instruction_enter_information()

                """
                Input information for delete player in this tournament.
                :parameter global variable tournament.
                """
                Tournament.remove_player(global_tournament)

            elif choice_tournament_menu == 5:
                tournament = False

    @staticmethod
    def name() -> str:
        """
        Generate a name tournament.
        Returns:
            str: name
        """
        while True:
            name = View.name()
            if not name.isalpha():
                View.input_error(name)
            else:
                return name

    @staticmethod
    def place():
        """
        Generate place of the tournament.
        Returns:
            str: place
        """
        while True:
            place = View.place()
            if not place.isalpha():
                View.input_error(place)
            else:
                return place

    @staticmethod
    def start_date():
        """
        Generate the date the tournament begins.
        Returns:
            date: start
        """
        start_date = date.today()
        start_date = start_date.strftime("%A %d %B %Y")
        return start_date

    @staticmethod
    def end_date():
        """
        Tournament end date.
        :arguments:
            date: start date
        Returns:
            str: same day
            or
            date: end date
        """
        View.title_decoration_number_of_days()
        View.instruction_select_choice()
        View.number_of_the_day(nb_of_day + 1)
        View.list_decoration_validate_menu()
        today = Tournament.start_date()
        validate = int(View.input_number_form_list_decoration())

        if validate == 1:
            View.number_of_the_day(nb_of_day + 1)
            end_date = date.today() + timedelta(nb_of_day)
            if end_date == date.today():
                return View.same_day()
        elif validate == 2:
            new_days = View.how_many_day()
            new_number = int(new_days)
            View.number_of_the_day(nb_of_day)
            end_date = today + timedelta(new_number - 1)
            return end_date.strftime("%A %d %B %Y")

    @staticmethod
    def number_rounds():
        """
        Generate number of rounds for the tournament.
        Returns:
            int: number of rounds
        """
        View.title_decoration_number_of_round()
        View.instruction_select_choice()
        View.number_of_the_rounds(nb_of_round)
        View.list_decoration_validate_menu()

        validate = int(View.input_number_form_list_decoration())
        if validate == 1:
            View.number_of_the_rounds(nb_of_round)
            return nb_of_round
        if validate == 2:
            new_number = View.how_many_rounds()
            new_number = int(new_number)
            View.number_of_the_rounds(new_number)
            return new_number

    @staticmethod
    def number_players():
        """
        Generate number of player for the tournament.
        Returns:
            int: number of player
        """
        View.title_decoration_number_of_player()
        View.instruction_select_choice()
        View.number_of_the_players(nb_of_players)
        View.list_decoration_validate_menu()
        validate = int(View.input_number_form_list_decoration())

        if validate == 1:
            View.number_of_the_players(nb_of_players)
            return nb_of_players
        if validate == 2:
            new_number = View.how_many_players()
            new_number = int(new_number)
            View.number_of_the_players(new_number)
            return new_number

    @staticmethod
    def new_tournament():
        """
        imports the data of the views
        and passes these data parameters in the models.
        """
        name = View.name()
        place = View.place()
        start_date = Tournament.start_date()
        end_date = Tournament.end_date()
        nb_rounds = Tournament.number_rounds()
        nb_players = Tournament.number_players()

        new_tournament = Model(name=name,
                               place=place,
                               start_date=start_date,
                               end_date=end_date,
                               nb_rounds=nb_rounds,
                               nb_players=nb_players)
        View.confirmation_of_tournament_creation(name, place, start_date,
                                                 end_date, nb_players,
                                                 nb_rounds)
        return new_tournament

    @staticmethod
    def append_player(tournament):
        """Returns the players to be added to the tournament list."""
        if tournament is None:
            View.create_tournament_before_add_players()
            return
        if tournament != "":
            player = Player.get_one_player()
            tournament.append_player(player)

    @staticmethod
    def get_players_list(tournament):
        """Display all participants of the tournament."""
        return tournament.get_players_list()

    @staticmethod
    def remove_player(tournament):
        """Remove player un tournament list"""
        player = Player.get_one_player()
        tournament.remove_player(player)
