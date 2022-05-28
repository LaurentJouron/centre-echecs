"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController
from view.chess_center import ChessCenterView


class ChessCenter:

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

        """Reception of player menu"""
        if input_menu == 1:
            PlayerController.player_menu()

        """Reception of tournament menu"""
        if input_menu == 2:
            TournamentController.tournament_menu()

        """exit game"""
        if input_menu == 4:
            """Decoration text display all players in this tournament."""
            ChessCenterView.exit_program()
            ChessCenterView.exiting_program()
            ChessCenterView.exit_confirmation_menu()

            """Input the number choice of the reception menu"""
            exit_menu = int(ChessCenterView.input_menu())

            if exit_menu >= 3:
                ChessCenterView.value_error()
            if exit_menu == 1:
                reception = True
            if exit_menu == 2:
                reception = False
