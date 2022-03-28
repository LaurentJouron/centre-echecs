"""Entry point."""
import constants
from controller.tournament import TournamentController
from controller.player import PlayerController
# from controller.tour import TourController
# from controller.match import MatchController

number_players = constants.NUMBER_OF_PLAYERS

if __name__ == '__main__':

    # Reception
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")

    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')} \n")

    tournament = " Tournament creation "
    print(f"{tournament.center(106, '-')}")

    while True:
        # Starting the game
        tournament_controller = TournamentController()
        print(str(tournament_controller.new_tournament()))

        tournament_validate = " Select: 1-> validate  2-> Modify "
        print(f"\n{tournament_validate.center(106, '-')}")
        
        validate = input(f"Select 1 or 2 : ")
        if validate == "1":
            start_of_tournament = " Start of the tournament "
            print(f"\n{start_of_tournament.center(106, '*')}")

            # players = PlayerController.get_all()
            # players = len(players)
            # while players < number_players:
            while True:
                player = " Register players "
                print(f"{player.center(106, ' ')}")

                player_controller = PlayerController()
                print(str(PlayerController.create()))

                new_player = " Select 1-> new player  2-> remove player 3-> " \
                             "show all"
                print(f"{new_player.center(106, '-')}")
                new_players = input(f"Select 1, 2 or 3: ").upper()
                if new_players == "1":
                    new_players = True
                if new_players == "2":
                    PlayerController.remove()
                    new_players = True
                if new_players == "3":
                    PlayerController.get_all()
                    new_players = True
            else:
                new_player = False

            # print(f"Registration is complete for this tournament.")

            if validate == "2":
                tournament_modification = " Tournament modification "
                print(f"{tournament_modification.center(106, '-')}")

                tournament_controller = TournamentController()
                print(str(tournament_controller.new_tournament()))




    # PlayerController.remove()

    # confirmation = " Confirmation "
    # print(f"\n{confirmation.center(106, '-')}")

    # player_controller = PlayerController()
    # print(str(PlayerController.create()))

    # """New round."""
    # tour = " New round "
    # print(f"{tour.center(106, '-')}")

    # tour_controller = TourController()
    # TourController.new_tour()

    # """Match results."""
    # match = " Match results "
    # print(f"{match.center(106, '-')}")
    # score = " Selects: 1 for win - D for tie - 0 for lose "
    # print(f"{score.center(106, ' ')}")
