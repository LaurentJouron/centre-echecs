"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController

if __name__ == '__main__':
    
    """Creation of a tournament."""
    new_tournament = TournamentController()
    TournamentController.new_tournament()
    
    player = " Commencez à enregistrer les joueurs "
    print(f"{player.center(60, '-')}\n")
    
    """Creation of a new player."""
    create_player = PlayerController()
    PlayerController.create_player()
