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
    
        if reception_choice_menu >= 5:
            print("Value error.")
   
        if reception_choice_menu == 1:
            PlayerController.player_menu()

        # Reception of tournament menu
        if reception_choice_menu == 2:
            TournamentController.tournament_menu()
        
            # exit game
        if reception_choice_menu == 4:
            # Decoration text display all players in this tournament.
            exit_programme = " EXIT CHESS CENTER "
            print(f"\n{exit_programme.center(106, ' ')}")
        
            information_decoration = " Exiting the program "
            print(f"{information_decoration.center(106, '*')}")
        
            exit_list = "> [1]Non  [2]Yes <"
            print(f"\n{exit_list.center(106, '-')}")
        
            # Input the number choice of the reception menu
            select_start_menu = input(f"Select the menu number : ")
            exit_choice_menu = int(select_start_menu)
            if exit_choice_menu >= 3:
                print("Value error")
            if exit_choice_menu == 1:
                reception = True
            if exit_choice_menu == 2:
                reception = False
