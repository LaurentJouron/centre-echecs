"""Generates encounter information."""
import time

from model.player import PlayerModel


class TourView:
    """Generates tournament elements."""
    blitz = 5
    bullet = 2

    # def __init__(self, player1=None, player2=None, players=None):
    #     self.players = players
    #     self.player1 = player1
    #     self.player2 = player2

    def __init__(self):
        # self.players = players
        # self.player1 = player1
        # self.player2 = player2
        pass

    def how_many_players(self):
        """How many player in tournament and creat 2 groups."""
        players = PlayerModel.len()

    def first_tour(self):
        player1 = self.players[::2]
        player2 = self.players[1::2]
        print(player2, player1)

    def blitz_countdown(self):
        """The blitz gives a maximum of 5 minutes to each player"""
        blitz = self.blitz * 60
        while blitz:
            minutes, seconds = divmod(blitz, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            blitz -= 1
        print("The game is over")

    def bullet_countdown(self):
        """The bullet gives a maximum of 2 minutes to each player"""
        bullet = self.bullet * 60
        while bullet:
            minutes, seconds = divmod(bullet, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            bullet -= 1
        print("The game is over")
