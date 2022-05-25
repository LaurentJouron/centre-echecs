from itertools import accumulate


class RoundModel:
    def __init__(self):
        self.all_players = []

    def append_player(self, player):
        """Adds players to the round list."""
        self.all_players.append(player)

    def alphabetical_order(self):
        """Sort players alphabetically"""
        self.all_players.sort(key=lambda x: x[1])
        return self.all_players

    def ranking_order(self):
        """Sort players ranking"""
        self.all_players.sort(key=lambda x: x[4])
        return self.all_players

    def two_lists(self):
        """Divide into two lists"""
        all_players = self.all_players
        length_split = [len(all_players)//2]*2
        two_list = [all_players[x - y: x] for x, y in zip(accumulate(length_split), length_split)]
        return two_list

    # def first_party(self):
    #     """Organize the first round player-to-player."""
    #     first_player: int = 0
    #     second_player: int = 4
    #     for _ in range(nb_game):
    #         first_tour = self.players[first_player::second_player]
    #         first_player += 1
    #         second_player += 1
    #         self.rounds.append([first_tour])

    # def other_party(self):
    #     """Organizes player-to-player games for the remainder of the
    #     tournament """
    #     pass

