"""Enter the results of the players participating in the tournament."""


class MatchView:
    
    def __init__(self):
        pass
    
    def define_winner(self):
        """Define the winner of the match."""
        while True:
            winner = input("Select 1 / D / 2 : ")
            winner = winner.upper()
            if winner == "1":
                return "player 1 win"
            elif winner == "2":
                return "player 2 win"
            elif winner == "D":
                return "draw"
            else:
                winner = False
                if not winner:
                    print(f"Input error")
    
    def display_winner(self):
        winning = " The winner "
        print(f"\n {winning.center(90,'-')}")
        print(f"{self.define_winner()} wins the game and scores 1 point")
