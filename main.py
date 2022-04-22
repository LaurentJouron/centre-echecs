"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController


if __name__ == '__main__':
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")
    
    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')}\n")
    
    national_player_list = " Add player to the national list "
    print(f"{national_player_list.center(106, '*')}\n")
    
    new_players = "> 1 = new player  /  2 = show all  /  3 = remove  /  4 = begin party <"
    print(f"{new_players.center(106, '-')}")
    
    new_players = input(f"Select 1, 2, 3 or 4 : ")
    new_players = int(new_players)
    
    while new_players != 5:
        if new_players > 4:
            print("Error value")
        if new_players == 1:
            PlayerController.create()
        if new_players == 2:
            PlayerController.get_all()
        if new_players == 3:
            PlayerController.remove()
        if new_players == 4:
            tournament = " Tournament creation "
            print(f"{tournament.center(106, '*')}")
            
            tournament_controller = TournamentController()
            print(str(tournament_controller.new_tournament()))
            
            tournament_validate = "> 1 = Modify  /  2 = validate <"
            print(f"{tournament_validate.center(106, '-')}")

            tournament_start = input(f"Select 1, 2 : ")
            tournament_start = int(tournament_start)
            
            while tournament_start != 3:
                if tournament_start == 1:
                    tournament_modification = " Tournament modification "
                    print(f"{tournament_modification.center(106, '-')}")
                    
                    tournament_controller = TournamentController()
                    print(str(tournament_controller.new_tournament()))
                
                if tournament_start == 2:
                    players_tournament = " Select players for this tournament "
                    print(f"\n{players_tournament.center(106, '*')}\n")
                    
                    tournament_player = "> 1 = add player  /  2 = Display players  /  3 = play <"
                    print(f"{tournament_player.center(106, '-')}")
                    
                    tournament_player = input(f"Select 1, 2 , 3: ")
                    tournament_player = int(tournament_player)

                    while tournament_player != 3:
                        if tournament_player == 1:
                            tournament_player = " Register tournament players "
                            print(f"{tournament_player.center(106, '-')}")

                            append_player = TournamentController.append_player(tournament)
                    
                        # if tournament_player == 2:
                        #     display_players_list = TournamentController.display_players_list(tournament)

                        # if tournament_player == 3:
                        #     pass
                        
                        tournament_player = "> 1 = add player  /  2 = Display players  /  3 = play <"
                        print(f"{tournament_player.center(106, '-')}")
                        tournament_player = input(f"Select 1, 2 , 3: ")
                        tournament_player = int(tournament_player)
                        
                tournament_validate = "> 1 = Modify  /  2 = validate <"
                print(f"{tournament_validate.center(106, '-')}")
                tournament_start = input(f"Select 1, 2 : ")
                tournament_start = int(tournament_start)
                
        new_players = "> 1 = new player  /  2 = show all  /  3 = remove  /  " \
                      "4 = begin party <"
        print(f"{new_players.center(106, '-')}")
        new_players = input(f"\nSelect 1, 2, 3 or 4 : ")
        new_players = int(new_players)
