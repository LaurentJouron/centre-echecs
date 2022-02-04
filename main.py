"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController
from controller.match import MatchController


if __name__ == '__main__':
    
    """Creation of a tournament."""
    tournament = " Création d'un tournoi "
    print(f"\n{tournament.center(90, '-')}")
    
    new_tournament = TournamentController()
    TournamentController.new_tournament()
    
    """Creation of a new player."""
    player = " Enregistrer les joueurs "
    print(f"{player.center(90, '-')}")
    
    create_player = PlayerController()
    PlayerController.create_player()

    game_management = MatchController()
    MatchController.game_management()
