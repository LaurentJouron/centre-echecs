"""Enter the results of the players participating in the tournament."""


class MatchView:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.score1 = None
        self.player2 = player2
        self.score2 = None
    
    def result_players(self):
        """Define the result of the player1."""
        while True:
            score1 = input(f"Select the {self.player1.first_name} score: ")
            score1 = score1.upper()
            if score1 == "0":
                return 0
            elif score1 == "D":
                return 0.5
            elif score1 == "1":
                return 1
            else:
                score1 = False
                if not score1:
                    print(f"Input error")
                    
            score2 = input(f"Select the {self.player2.first_name} score: ")
            score2 = score2.upper()
            if score2 == "0":
                return 0
            elif score2 == "D":
                return 0.5
            elif score2 == "1":
                return 1
            else:
                score2 = False
                if not score2:
                    print(f"Input error")
                    
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
       