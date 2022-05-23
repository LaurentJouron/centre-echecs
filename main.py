"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController
from controller.round import RoundController

global_tournament = None
global_players = None
global_rounds = None
global_day = None


if __name__ == '__main__':
    RoundController.append_player()
    # Open application
    welcome_application = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome_application.center(106, ' ')}")

    instruction = " Please follow the instructions below "
    print(f"\n{instruction.center(106, ' ')}")

    # Reception of application
    reception = True
    while reception:

        # Decoration text reception for in line game.
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, ' ')}")

        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

        start_menu = "> [1]Player list  [2]Tournament  [3]Round  [4]Quit <"
        print(f"\n{start_menu.center(106, '-')}")

        # Input the number choice of the reception menu
        select_start_menu = input(f"Select the menu number : ")
        reception_choice_menu = int(select_start_menu)

        # Reception of players menu
        if reception_choice_menu == 1:
            players = True
            while players:

                # Decoration text players reception in line game.
                player_reception = " PLAYER RECEPTION "
                print(f"\n{player_reception.center(106, ' ')}")

                choice_decoration = " Make your choice "
                print(f"{choice_decoration.center(106, '*')}")

                player_menu = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
                print(f"\n{player_menu.center(106, '-')}")

                # Input the number choice of the players menu
                select_player_menu = input(f"Select the menu number : ")
                choice_players_menu = int(select_player_menu)

                if choice_players_menu >= 5:
                    print("Value error.")

                if choice_players_menu == 1:
                    # Decoration text players creation for in line game.
                    player_creation = " PLAYER CREATION "
                    print(f"\n{player_creation.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    # Input information for create player in data file.
                    PlayerController.create()

                if choice_players_menu == 2:
                    # Decoration text get all players in line game.
                    all_player = " ALL PLAYERS IN LIST "
                    print(f"\n{all_player.center(106, ' ')}")

                    information_decoration = " Display all players in list "
                    print(f"{information_decoration.center(106, '*')}")

                    # Display all players in data file.
                    all_players = PlayerController
                    print(str(all_players.get_all()))

                if choice_players_menu == 3:
                    # Decoration text delete players for in line game.
                    delete_player = " PLAYER DELETE "
                    print(f"\n{delete_player.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    # Input information for delete player in data file.
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

                tournament_list = "> [1]Create  [2]Modify  [3]Quit <"
                print(f"\n{tournament_list.center(106, '-')}")

                # Input the number choice of the tournament menu
                select_tournament_menu = input(f"Select the menu number : ")
                choice_tournament_menu = int(select_tournament_menu)

                if choice_tournament_menu >= 4:
                    print("Value error.")

                if choice_tournament_menu == 1:
                    # Decoration text creation tournament for in line game.
                    tournament_creation = " TOURNAMENT CREATION "
                    print(f"\n{tournament_creation.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    # Input information for create tournament.
                    global_tournament = TournamentController.new_tournament()
                    global_players = TournamentController.number_players()
                    global_rounds = TournamentController.number_rounds()

                if choice_tournament_menu == 2:

                    # Decoration text creation tournament for in line game.
                    tournament_creation = " MODIFICATION TOURNAMENT "
                    print(f"\n{tournament_creation.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    # Input information for create tournament.
                    global_tournament = TournamentController.new_tournament()
                    global_players = TournamentController.number_players()
                    global_rounds = TournamentController.number_rounds()

                if choice_tournament_menu == 3:
                    tournament = False

        if reception_choice_menu == 3:
            rounds = True
            while rounds:

                # Decoration text round reception in line game.
                round_reception = " ROUND RECEPTION "
                print(f"\n{round_reception.center(106, ' ')}")

                choice_decoration = " Make your choice "
                print(f"{choice_decoration.center(106, '*')}")

                round_menu = "> [1]Add_player  [2]Show_player_list  [3]Remove_player  [4]First_round  [5]Quit <"
                print(f"\n{round_menu.center(106, '-')}")

                # Input the number choice of the players menu
                select_round_menu = input(f"Select the menu number : ")
                choice_round_menu = int(select_round_menu)

                if choice_round_menu == 1:

                    add_players = " APPEND TOURNAMENT PLAYERS "
                    print(f"\n{add_players.center(106, ' ')}")

                    information_decoration = " Enter information "
                    print(f"{information_decoration.center(106, '*')}")

                    # Input information for append player in this tournament.
                    RoundController.append_player(global_tournament)


                # if choice_round_menu == 2:
                #     # Decoration text display all players in this tournament.
                #     all_player = " ALL PLAYERS IN TOURNAMENT "
                #     print(f"\n{all_player.center(106, ' ')}")
                #
                #     information_decoration = " Display all players in list "
                #     print(f"{information_decoration.center(106, '*')}")
                #
                #     # Display all players in this tournament.
                #     TournamentController.get_players_list(global_tournament)
                #
                # if choice_round_menu == 4:
                #     # Decoration text delete player in this tournament.
                #     tournament_creation = " REMOVE PLAYERS TOURNAMENT "
                #     print(f"\n{tournament_creation.center(106, ' ')}")
                #
                #     information_decoration = " Enter information "
                #     print(f"{information_decoration.center(106, '*')}")
                #
                #     # Input information for delete player in this tournament.
                #     TournamentController.remove_player(global_tournament)

                if choice_round_menu == 5:
                    rounds = False


            # exit game
        if reception_choice_menu == 4:
            reception = False
