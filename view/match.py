"""Enter the results of the players participating in the tournament."""


class MatchView:
    """Generate the elements for the organisation of the tournament."""

    number_players = 8
    player_1 = ["Laurent", "Virginie", "Louis", "Antoine"]
    player_2 = ["Thierno", "Marc", "Julia", "Felix"]
    
    def __init__(self):
        pass
        
    def create_a_match(self):
        for player_1 in range(1, self.number_players+1):
            for player_2 in range(1, self.number_players+1):
                if player_1 != player_2:
                    return "Joueur:", player_1, "VS Joueur:", player_2
