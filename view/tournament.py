"""Enter information for the tournament organization."""

from datetime import date
from datetime import timedelta


class TournamentView:
    """What information is needed for the tournament."""

    number_of_day = 0
    number_of_round = 4
    number_players = 8

    def __init__(self):
        pass
    
    def name_of_tournament(self):
        """Name the tournament."""
        name: str = input("Saisissez le nom du tournoi: ")
        return name.capitalize()
    
    def tournament_venue(self):
        """Where the tournament goes."""
        place: str = input("Lieu du tournoi: ")
        return place.capitalize()
    
    def get_tournament_start_date(self):
        """On what date the tournament begins."""
        return date.today()
    
    def get_tournament_end_date(self):
        """Tournament end date."""
        end_date = self.get_tournament_start_date() + timedelta(
            days=self.number_of_day)
        if end_date == self.get_tournament_start_date():
            return "même jour"
        else:
            return end_date

    def organize_new_tournament(self):
        """Gathering of elements of the tournament class."""
        name = self.name_of_tournament()
        place = self.tournament_venue()
        start_date = self.get_tournament_start_date()
        end_date = self.get_tournament_end_date()
        number_round = self.number_of_round
        number_players = self.number_players
        return [name, place, start_date, end_date, number_round,
                number_players]
    
    def display_tournament_organization(self, tournament):
        """Confirmation phrase of the tournament class."""
        start_of_tournament = " Démarrage du tournoi "
        print(f"\n {start_of_tournament.center(90, '-')}")
        print(f"Le tournoi d'échec {tournament.name} commence le "
              f"{tournament.start_date} à 9h00 pour finir le"
              f" {tournament.end_date} à 18h00.\n"
              f"Il se déroule {tournament.place} avec {tournament.players} "
              f"joueurs en {tournament.rounds} tours.\n")
