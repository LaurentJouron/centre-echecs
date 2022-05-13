"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController

global_tournament = None


if __name__ == '__main__':

    # Open application
    welcome_application = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome_application.center(106, ' ')}")

    instruction = " Please follow the instructions below "
    print(f"\n{instruction.center(106, ' ')}")

    # Reception of application
    reception = True
    while reception:

        # Decoration recetion text for in line game.
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, ' ')}")

        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

        start_menu = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
        print(f"\n{start_menu.center(106, '-')}")

        # Input the choice
        select_start_menu = input(f"Select the menu number : ")
        reception_choice_menu = int(select_start_menu)

        # Reception of players menu
        if reception_choice_menu == 1:
            players = True
            while players:

                # Decoration for players reception for in line game.
                player_reception = " PLAYER RECEPTION "
                print(f"\n{player_reception.center(106, ' ')}")

                choice_decoration = " Make your choice "
                print(f"{choice_decoration.center(106, '*')}")

                player_menu = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
                print(f"\n{player_menu.center(106, '-')}")

                # Input the choice
                select_player_menu = input(f"Select the menu number : ")
                choice_players_menu = int(select_player_menu)

                if choice_players_menu >= 5:
                    print("Value error.")

                if choice_players_menu == 1:
                    player_creation = " PLAYER CREATION "
                    print(f"\n{player_creation.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    PlayerController.create()

                if choice_players_menu == 2:
                    all_player = " ALL PLAYERS IN LIST "
                    print(f"\n{all_player.center(106, ' ')}")

                    information_decoration = " Display all players in list "
                    print(f"{information_decoration.center(106, '*')}")

                    PlayerController.get_all()

                if choice_players_menu == 3:
                    delete_player = " PLAYER DELETE "
                    print(f"\n{delete_player.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    PlayerController.remove()

                if choice_players_menu == 4:
                    players = False

        # Reception of tournament menu
        if reception_choice_menu == 2:
            tournament = True
            while tournament:

                # Decoration for tournament reception for in line game.
                tournament_reception = " TOURNAMENT RECEPTION "
                print(f"\n{tournament_reception.center(106, ' ')}")

                choice_decoration = " Make your choice "
                print(f"{choice_decoration.center(106, '*')}")

                tournament_list = "> [1]Create  [2]Add player  " \
                                  "[3]Display player  [4]Quit <"
                print(f"\n{tournament_list.center(106, '-')}")

                # Input the choice
                select_tournament_menu = input(f"Select the menu number : ")
                choice_tournament_menu = int(select_tournament_menu)

                if choice_tournament_menu >= 5:
                    print("Value error.")

                if choice_tournament_menu == 1:
                    tournament_creation = " TOURNAMENT CREATION "
                    print(f"\n{tournament_creation.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    tournament_controller = TournamentController()
                    tournament = tournament_controller.new_tournament()

                    global_tournament = tournament

                if choice_tournament_menu == 2:
                    add_players = " APPEND TOURNAMENT PLAYERS "
                    print(f"\n{add_players.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    TournamentController.append_player(global_tournament)

                if choice_tournament_menu == 3:
                    TournamentController.get_players_list(global_tournament)

                if choice_tournament_menu == 4:
                    tournament = False

        if reception == 3:
            pass

        # exit game
        if reception_choice_menu == 4:
            reception = False
