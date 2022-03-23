"""Entry point."""

from controller.tournament import TournamentController
# from controller.player import PlayerController
# from controller.tour import TourController
# from controller.match import MatchController

if __name__ == '__main__':

    # Reception
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")

    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')} \n")

    tournament = " Tournament creation "
    print(f"{tournament.center(106, '-')}")

    # Starting the game
    tournament_controller = TournamentController()
    print(str(tournament_controller.new_tournament()))

    start_of_tournament = " Start of the tournament "
    print(f"\n{start_of_tournament.center(106, '*')}")

    player = " Register players "
    print(f"{player.center(106, '-')}")

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
