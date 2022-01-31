"""Enter information for the tournament organization."""

from datetime import date
from datetime import timedelta


class TournamentView:
    """What information is needed for the tournament."""
    
    def __init__(self, number_of_day=1, number_of_round=4, number_players=8):
        self.number_of_day = number_of_day
        self.number_of_round = number_of_round
        self.number_players = number_players
    
    def name_of_tournament(self):
        """Name the tournament."""
        name = input("Saisissez le nom du tournoi: ")
        return name.capitalize()
    
    def tournament_venue(self):
        """Where the tournament goes."""
        place = input("Lieu du tournoi: ")
        return place.capitalize()
    
    def get_tournament_start_date(self):
        """On what date the tournament begins."""
        return date.today()
    
    def get_tournament_end_date(self):
        """Tournament end date."""
        end_date = self.get_tournament_start_date() + timedelta(
            days=self.number_of_day)
        return end_date
    
    def get_number_of_round(self):
        """Number of turns."""
        return self.number_of_round
    
    def get_number_of_player(self):
        """Number of players."""
        return self.number_players
    
    def organize_new_tournament(self):
        name = self.name_of_tournament()
        place = self.tournament_venue()
        start_date = self.get_tournament_start_date()
        end_date = self.get_tournament_end_date()
        number_round = self.get_number_of_round()
        number_players = self.get_number_of_player()
        return [name, place, start_date, end_date, number_round,
                number_players]
    
    def display_tournament_organization(self, tournament):
        start_of_tournament = " Démarrage du tournoi "
        print(f"\n {start_of_tournament.center(60, '-')}")
        print(f"\n Le tournoi d'échecs {tournament.name} commencera le "
              f"{tournament.start_date} à {tournament.place}.\n"
              f" Pour finir le {tournament.end_date}.\n "
              f"Il accueillera {tournament.players} joueurs"
              f" pour {tournament.rounds} tours.\n")
