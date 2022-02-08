"""Generates encounter information."""


class TourView:

    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2

    def how_many_players(self):
        """How many player in tournament and creat 2 groups."""


    def first_tour(self):
        player1 = self.players[::2]
        player2 = self.players[1::2]
        print(player2, player1)
