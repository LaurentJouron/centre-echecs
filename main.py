"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController


if __name__ == '__main__':
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")
    
    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')}\n")
    
    list_player = " Add player to the national list "
    print(f"{list_player.center(106, '-')}\n")
    
    while True:
        add_player = "> 1 = new player  /  2 = show all  /  3 = remove  /" \
                     "  4 = begin party <"
        print(f"{add_player.center(106, '-')}")
        new_players = input(f"Select 1, 2, 3 or 4 : ")
        
        if new_players == "1":
            PlayerController.create()
        if new_players == "2":
            PlayerController.get_all()
        if new_players == "3":
            PlayerController.remove()
        pass
    
        tournament = " Tournament creation "
        print(f"{tournament.center(106, '-')}")
        
        tournament_controller = TournamentController()
        print(str(tournament_controller.new_tournament()))
        
        while True:
            tournament_validate = "> 1 = validate  /  2 = Modify  /  " \
                                  "3 = Add player <"
            print(f"{tournament_validate.center(106, '-')}")
            validate = input(f"Select 1, 2 or 3 : ")
            if validate == "1":
                start_of_tournament = " Start of the tournament "
                print(f"\n{start_of_tournament.center(106, '*')}")
            
            if validate == "2":
                tournament_modification = " Tournament modification "
                print(f"{tournament_modification.center(106, '-')}")
                
                tournament_controller = TournamentController()
                print(str(tournament_controller.new_tournament()))
            
            if validate == "3":
                tournament_player = " -->> Register tournament players <<-- "
                print(f"{tournament_player.center(106, ' ')}")
    
                append_player = TournamentController.append_player()
                print(str(tournament_controller.append_player()))
                
