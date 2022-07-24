"""Entry point."""

from controller.tournament import Tournament
from controller.player import Player
from view.chess_center import ChessCenterView as View


class ChessCenter:
    """Decoration text when opening the application."""
    View.welcome_application()
    View.instruction()

    reception = True
    while reception:

        """Decoration text reception for in line game"""
        View.reception_name()
        View.choice_decoration()
        View.start_menu()

        """Input the number choice of the reception menu"""
        input_menu = int(View.input_menu())

        if input_menu >= 5:
            View.value_error()

        if input_menu == 1:
            """Reception of player menu"""
            Player.player_menu()

        elif input_menu == 2:
            """Reception of tournament menu"""
            Tournament.tournament_menu()

        elif input_menu == 4:
            """exit game"""
            """Decoration text display all players in this tournament."""
            View.exit_program()
            View.exiting_program()
            View.exit_confirmation_menu()

            """Input the number choice of the exit menu"""
            exit_menu = int(View.input_menu())

            if exit_menu >= 3:
                View.value_error()
            if exit_menu == 1:
                reception = True
            elif exit_menu == 2:
                reception = False
