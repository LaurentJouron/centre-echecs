"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController
from view.chess_center import ChessCenterView


class ChessCenterController:

    ChessCenterView.welcome_application()
    ChessCenterView.instruction()

    reception = True
    while reception:

        """Decoration text reception for in line game"""
        ChessCenterView.reception_name()
        ChessCenterView.choice_decoration()
        ChessCenterView.start_menu()

        """Input the number choice of the reception menu"""
        reception_choice_menu = int(ChessCenterView.select_reception_menu())

        if reception_choice_menu >= 5:
            ChessCenterView.value_error()

        if reception_choice_menu == 1:
            PlayerController.player_menu()

        """Reception of tournament menu"""
        if reception_choice_menu == 2:
            TournamentController.tournament_menu()

        """exit game"""
        if reception_choice_menu == 4:
            """Decoration text display all players in this tournament."""
            ChessCenterView.exit_program()
            ChessCenterView.exiting_program()
            ChessCenterView.exit_confirmation_menu()

            """Input the number choice of the reception menu"""
            select_start_menu = int(ChessCenterView.select_reception_menu())

            if select_start_menu >= 3:
                ChessCenterView.value_error()
            if select_start_menu == 1:
                reception = True
            if select_start_menu == 2:
                reception = False
