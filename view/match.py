"""Enter the results of the players participating in the tournament."""
from controller.player import PlayerController


class MatchView:
    def __init__(self):
        self.player1 = PlayerController.create_player()
        self.score1 = None
        self.player2 = PlayerController.create_player()
        self.score2 = None
    
    def result_players(self):
        """Define the result of the player1."""
        while True:
            score1 = input(f"Select the {self.player1.first_name} score: ")
            score1 = score1.upper()
            score2 = input(f"Select the {self.player2.first_name} score: ")
            score2 = score2.upper()
            if score1 == "0" and score2 == "1":
                score1 = 0
                score2 = 1
            elif score1 == "D" and score2 == "D":
                score1 = 0.5
                score2 = 0.5
            elif score1 == "1" and score2 == "0":
                score1 = 1
                score2 = 0
            else:
                score1 = False
                if not score1:
                    print(f"Input error")
            return score1, score2

    def results(self):
        player1 = self.player1.first_name + " : " + self.score1
        player2 = self.player2.first_name + " : " + self.score2
        return [[player1], [player2]]

    def display_winner(self, match):
        score = " The score "
        print(f"\n {score.center(90,'-')}")
        print(f"Here are the results of the match between "
              f"{match.player1.first_name} and {match.player2.first_name}.\n"
              f"{match.player1.first_name} scores {match.score1} point and "
              f"{match.player2.first_name} scores {match.score2} point.\n"
              f"Thank you both.")
       