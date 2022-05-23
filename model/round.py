from main import global_players


class RoundModel:
    def __init__(self):
        self.players: list = []
        self.rounds: list = []

    def append_player(self, player):
        """Adds players to the tournament list."""
        if len(self.players) < global_players:
            self.players.append(player)
        else:
            print("This tournament is completed")

    # def remove_player(self, player):
    #     """Remove player in tournament list."""
    #     self.players.remove(player)
    #
    # def get_players_list(self):
    #     """Display players from tournament list."""
    #     return self.players[:]

    # def alphabetical_order(self):
    #     """Sort players alphabetically"""
    #     self.players.sort()
    #
    # def ranking_order(self):
    #     """Sort players ranking"""
    #     self.players.sort(key=lambda ranking: self.players)
    #
    # def first_party(self):
    #     """Organize the first round player-to-player."""
    #     first_player: int = 0
    #     second_player: int = 4
    #     for _ in range(nb_game):
    #         first_tour = self.players[first_player::second_player]
    #         first_player += 1
    #         second_player += 1
    #         self.rounds.append([first_tour])
    #
    # def other_party(self):
    #     """Organizes player-to-player games for the remainder of the
    #     tournament """
    #     pass

