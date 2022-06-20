"""Management of chess player results."""
import time

import constants


class MatchController:
    """Controls the organization of games and scores in real time."""

    @staticmethod
    def blitz():
        """The blitz gives a maximum of 5 minutes to each player"""
        blitz_time = constants.BLITZ
        blitz = blitz_time * 60
        while blitz:
            minutes, seconds = divmod(blitz_time, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            blitz_time -= 1
        print("The game is over")

    @staticmethod
    def bullet_countdown():
        """The bullet gives a maximum of 2 minutes to each player"""
        bullet = constants.BULLET
        bullet = bullet * 60
        while bullet:
            minutes, seconds = divmod(bullet, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            bullet -= 1
        print("The game is over")
