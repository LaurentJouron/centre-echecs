"""Enter information for the tournament organization."""

from datetime import date
from datetime import timedelta


class TournamentView:
    """What information is needed for the tournament."""
    
    def __init__(self, number_of_day=0, number_of_round=4, number_players=8):
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
        if end_date == self.get_tournament_start_date():
            return "même jour"
        else:
            return end_date
    
    def get_number_of_round(self):
        """Number of turns."""
        while True:
            oui_non = input(f"Y a-t-il {self.number_of_round} tours? O/N: ")
            oui_non = oui_non.upper()
            if oui_non == "O":
                return self.number_of_round
            elif oui_non == "N":
                self.number_of_round = input("Combien y a-t-il de tours: ")
                return self.number_of_round
            else:
                oui_non = False
                if not oui_non:
                    print("Erreur de saisie")
    
    def get_number_of_player(self):
        """Number of players."""
        while True:
            oui_non = input(f"Y a-t-il {self.number_players} joueurs? O/N: ")
            oui_non = oui_non.upper()
            if oui_non == "O":
                return self.number_players
            elif oui_non == "N":
                self.number_players = input("Combien y a-t-il de joueurs: ")
                return self.number_players
            else:
                oui_non = False
                if not oui_non:
                    print("Erreur de saisie")
    
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
        print(f"\n {start_of_tournament.center(90, '-')}")
        print(f"\n Le tournoi d'échec {tournament.name} commence le "
              f"{tournament.start_date} à 9h00 pour finir le"
              f" {tournament.end_date} à 18h00.\n "
              f"Il se déroule {tournament.place} avec {tournament.players} "
              f"joueurs en {tournament.rounds} tours.\n")
