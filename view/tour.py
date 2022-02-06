"""Generates encounter information."""


class TourView:
    players = ["Thierno", "Virginie", "Louis", "Antoine", "Laurent", "Julia",
               "Marie", "Gérard"]
    player1 = players[::2]
    player2 = players[1::2]
    
    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
