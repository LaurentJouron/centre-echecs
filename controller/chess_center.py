"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController
from view.chess_center import ChessCenterView


class ChessCenter:
    """Decoration text when opening the application."""
    ChessCenterView.welcome_application()
    ChessCenterView.instruction()

    reception = True
    while reception:

        """Decoration text reception for in line game"""
        ChessCenterView.reception_name()
        ChessCenterView.choice_decoration()
        ChessCenterView.start_menu()

        """Input the number choice of the reception menu"""
        input_menu = int(ChessCenterView.input_menu())

        if input_menu >= 5:
            ChessCenterView.value_error()

        if input_menu == 1:
            """Reception of player menu"""
            PlayerController.player_menu()

        elif input_menu == 2:
            """Reception of tournament menu"""
            TournamentController.tournament_menu()

        elif input_menu == 4:
            """exit game"""
            """Decoration text display all players in this tournament."""
            ChessCenterView.exit_program()
            ChessCenterView.exiting_program()
            ChessCenterView.exit_confirmation_menu()

            """Input the number choice of the exit menu"""
            exit_menu = int(ChessCenterView.input_menu())

            if exit_menu >= 3:
                ChessCenterView.value_error()
            if exit_menu == 1:
                reception = True
            elif exit_menu == 2:
                reception = False
