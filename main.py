"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController

global_tournament: str = "Tournament"

if __name__ == '__main__':
    """Decoration text"""
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")
    
    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')}\n")
    
    national_player_list = " Add player to the national list "
    print(f"{national_player_list.center(106, '*')}\n")

    """Management of players on the national list"""
    new_players = "> 1 = new player  /  2 = show all  /  3 = remove  /  4 = begin party <"
    print(f"{new_players.center(106, '-')}")
    
    new_players = input(f"Select : ")
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
            tournament_creation = " Tournament creation "
            print(f"{tournament_creation.center(106, '*')}")
            
            tournament_controller = TournamentController()
            tournament = tournament_controller.new_tournament()
            print(str(tournament))
            global global_tournament
            global_tournament = tournament.name

            tournament_validate = "> 1 = Modify  /  2 = validate <"
            print(f"{tournament_validate.center(106, '-')}")

            tournament_start = input(f"Select : ")
            tournament_start = int(tournament_start)
            
            while tournament_start != 3:
                if tournament_start == 1:
                    tournament_modification = " Tournament modification "
                    print(f"{tournament_modification.center(106, '-')}")

                    tournament_controller = TournamentController()
                    tournament = tournament_controller.new_tournament()
                    print(str(tournament))
                    global global_tournament
                    global_tournament = tournament.name
                
                if tournament_start == 2:
                    players_tournament = " Select players for this tournament "
                    print(f"\n{players_tournament.center(106, '*')}\n")
                    
                    tournament_player = "> 1 = add player  /  2 = Display players  /  3 = play <"
                    print(f"{tournament_player.center(106, '-')}")
                    
                    tournament_player = input(f"Select : ")
                    tournament_player = int(tournament_player)

                    while tournament_player != 3:
                        if tournament_player == 1:
                            tournament_player = " Register tournament players "
                            print(f"{tournament_player.center(106, '-')}")

                            append_player = TournamentController.append_player(global_tournament)
                    
                        # if tournament_player == 2:
                        #     display_players_list = TournamentController.display_players_list(global_tournament)

                        # if tournament_player == 3:
                        #     pass
                        
                        tournament_player = "> 1 = add player  /  2 = Display players  /  3 = play <"
                        print(f"{tournament_player.center(106, '-')}")
                        tournament_player = input(f"Select : ")
                        tournament_player = int(tournament_player)
                        
                tournament_validate = "> 1 = Modify  /  2 = validate <"
                print(f"{tournament_validate.center(106, '-')}")
                tournament_start = input(f"Select : ")
                tournament_start = int(tournament_start)
                
        new_players = "> 1 = new player  /  2 = show all  /  3 = remove  /  " \
                      "4 = begin party <"
        print(f"{new_players.center(106, '-')}")
        new_players = input(f"\nSelect : ")
        new_players = int(new_players)
