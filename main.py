"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController
from controller.tour import TourController
from controller.match import MatchController


if __name__ == '__main__':
    """Welcome to the game."""
    """Sentence when opening the game."""
    welcome = " Welcome to the << CENTER-ECHEC >> application "
    print(f"\n{welcome.center(90, ' ')}\n")
    
    """Follow the instructions."""
    instruction = " Please follow the instructions below: "
    print(f"{instruction.center(90, ' ')} \n")
    
    """Starting the game"""
    """Creation of a tournament."""
    tournament = " Creating a tournament "
    print(f"{tournament.center(90, '-')}")
    
    new_tournament = TournamentController()
    TournamentController.new_tournament()
    
    """Register players."""
    player = " Register players "
    print(f"{player.center(90, '-')}")
    
    create_player = PlayerController()
    PlayerController.create_player()

    """New round."""
    tour = " New round "
    print(f"{tour.center(90, '-')}")

    # new_tour = TourController()
    # TourController.new_tour()
    #
    """Match results."""
    match = " Match results "
    print(f"{match.center(90, '-')}")

    game_management = MatchController()
    MatchController.score_match()
