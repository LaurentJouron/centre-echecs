"""Entry point."""

from controller.player import PlayerController
from controller.match import MatchController


if __name__ == '__main__':
    create_player = PlayerController()
    PlayerController.create_player()

    generate_parties = MatchController()
    MatchController.generate_parties()