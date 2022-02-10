"""Entry point."""

from controller.tournament import TournamentController
from controller.player import PlayerController
from controller.tour import TourController
from controller.match import MatchController


if __name__ == '__main__':
    
    """Creation of a tournament."""
    tournament = " Création d'un tournoi "
    print(f"{tournament.center(90, '-')}")
    
    new_tournament = TournamentController()
    TournamentController.new_tournament()
    
    """Register players."""
    player = " Enregistrer les joueurs "
    print(f"{player.center(90, '-')}")
    
    create_player = PlayerController()
    PlayerController.create_player()

    """New round."""
    tour = " Nouveau tour "
    print(f"{tour.center(90, '-')}")

    # new_tour = TourController()
    # MatchController.new_tour()
    #
    # """Match results."""
    # match = " Résultats des matchs "
    # print(f"{match.center(90, '-')}")
    #
    # game_management = MatchController()
    # MatchController.game_management()


