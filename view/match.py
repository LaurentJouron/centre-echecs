"""Enter the results of the players participating in the tournament."""


class MatchView:
    def __init__(self):
        pass
    
    def result_player1(self):
        """Define the result of the player1."""
        while True:
            score1 = input("Select the player1 score: ")
            if score1 == "0":
                return ["player1", 0]
            elif score1 == "D":
                return ["player1", 0.5]
            elif score1 == "1":
                return ["player1", 1]
            else:
                score1 = False
                if not score1:
                    print(f"Input error")

    def result_player2(self):
        """Define the result of the player1."""
        while True:
            score2 = input("Select the player2 score: ")
            if score2 == "0":
                return ["player2", 0]
            elif score2 == "D":
                return ["player2", 0.5]
            elif score2 == "1":
                return ["player2", 1]
            else:
                score2 = False
                if not score2:
                    print(f"Input error")
                    
    def results(self):
        score1 = self.result_player1()
        score2 = self.result_player2()
        return ["player1: ", score1], ["player2", score2]

    def display_winner(self, match):
        winner = " The winner "
        print(f"\n {winner.center(90,'-')}")
        if self.result_player1() == "1":
            print(f"Player 1 wins the game and scores {match.score1} point.")
        if self.result_player2() == "1":
            print(f"Player 2 wins the game and scores {match.score2} point.")
        if self.result_player1() == "0.5":
            print(f"Players are tied for {match.score1} points each.")
