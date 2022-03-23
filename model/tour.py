"""Information for the organisation of chass tournaments."""
import time

from tinydb import TinyDB

import constants

bullet = constants.BULLET
blitz = constants.BLITZ


class TourModel:
    """Generates tournament elements."""
    db = TinyDB(f"data/tour.json", indent=4)

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # def blitz_countdown(self, blitz=None):
    #     """The blitz gives a maximum of 5 minutes to each player"""
    #     blitz = blitz * 60
    #     while blitz:
    #         minutes, seconds = divmod(blitz, 60)
    #         timer = '{:02d}:{:02d}'.format(minutes, seconds)
    #         print(timer, end="\r")
    #         time.sleep(1)
    #         blitz -= 1
    #     print("The game is over")
    #
    # def bullet_countdown(self):
    #     """The bullet gives a maximum of 2 minutes to each player"""
    #     bullet = self.bullet * 60
    #     while bullet:
    #         minutes, seconds = divmod(bullet, 60)
    #         timer = '{:02d}:{:02d}'.format(minutes, seconds)
    #         print(timer, end="\r")
    #         time.sleep(1)
    #         bullet -= 1
    #     print("The game is over")
