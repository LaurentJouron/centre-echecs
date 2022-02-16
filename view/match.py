"""Enter the results of the players participating in the tournament."""


class MatchView:
    def __init__(self):
        pass
    
    def result_player1(self):
        """Define the result of the player1."""
        while True:
            player1 = input("Select the player1 score 0 / D / 1 : ")
            if player1 == "0":
                return 0
            elif player1 == "D":
                return 0.5
            elif player1 == "1":
                return 1
            else:
                winner = False
                if not winner:
                    print(f"Input error")

    def result_player2(self):
        """Define the result of the player1."""
        while True:
            player2 = input("Select the player2 score 0 / D / 1 : ")
            if player2 == "0":
                return 0
            elif player2 == "D":
                return 0.5
            elif player2 == "1":
                return 1
            else:
                winner = False
                if not winner:
                    print(f"Input error")
                    
    def results(self):
        score1 = self.result_player1()
        score2 = self.result_player2()
        return [score1, score2]
