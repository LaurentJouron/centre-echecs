"""Entry point."""

from controller.tournament import TournamentController
# from controller.player import PlayerController
# from controller.tour import TourController
# from controller.match import MatchController

if __name__ == '__main__':
    """Reception"""
    welcome = " Welcome to the << CENTER-ECHEC >> application "
    print(f"\n{welcome.center(90, ' ')}\n")
    
    instruction = " Please follow the instructions below "
    print(f"{instruction.center(90, ' ')} \n")

    """Creation of a tournament."""
    tournament = " Creating a tournament "
    print(f"{tournament.center(90, '-')}")

    """Starting the game"""
    tournament_controller = TournamentController()
    print(str(TournamentController.new_tournament()))

    start_of_tournament = " Start of the tournament "
    print(f"\n {start_of_tournament.center(90, '-')}")

    # """Register players."""
    # player = " Register players "
    # print(f"{player.center(90, '-')}")

    # player_controller = PlayerController()
    # PlayerController.create_player(self=player_controller)

    # """New round."""
    # tour = " New round "
    # print(f"{tour.center(90, '-')}")

    # tour_controller = TourController()
    # TourController.new_tour()

    # """Match results."""
    # match = " Match results "
    # print(f"{match.center(90, '-')}")
    # score = " Selects: 1 for win - D for tie - 0 for lose "
    # print(f"{score.center(90, ' ')}")

