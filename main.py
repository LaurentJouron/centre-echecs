"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController

NUMBER_OF_DAYS = 1
NUMBER_OF_ROUNDS = 4
NUMBER_OF_PLAYER = 8

if __name__ == '__main__':
    
    """Creation of a tournament."""
    new_tournament = TournamentController()
    TournamentController.new_tournament()
    
    """Creation of a new player."""
    create_player = PlayerController()
    PlayerController.create_player()

