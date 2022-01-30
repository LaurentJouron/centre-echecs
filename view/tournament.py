"""Enter information for the tournament organization."""

from datetime import date

from main import NUMBER_OF_ROUNDS
from main import NUMBER_OF_DAYS


class TournamentView:
    """What information is needed for the tournament."""

    @staticmethod
    def name_of_tournament():
        """Name the tournament."""
        name = input("Saisissez le nom du tournoi: ")
        return name

    @staticmethod
    def tournament_venue():
        """Where the tournament goes."""
        place = input("Lieu du tournoi: ")
        return place

    @staticmethod
    def tournament_start_date():
        """On what date the tournament begins."""
        start_date = date.today()
        return start_date

    @staticmethod
    def tournament_end_date():
        """Tournament end date."""
        end_date = TournamentView.tournament_start_date() + NUMBER_OF_DAYS
        return end_date

    @staticmethod
    def number_of_round():
        """Number of turns."""
        number_round = NUMBER_OF_ROUNDS
        return number_round

    @staticmethod
    def organize_new_tournament():
        name = TournamentView.name_of_tournament()
        place = TournamentView.tournament_venue()
        start_date = TournamentView.tournament_start_date()
        end_date = TournamentView.tournament_end_date()
        number_round = TournamentView.number_of_round()
        return [name, place, start_date, end_date, number_round]

    @staticmethod
    def display_tournament_organization(tournament):
        start_of_tounrament = " Démarrage "
        print(f"\n {start_of_tounrament.center(56 , '-')}")
        print(f"Le tournoi {tournament.name} se commence le "
              f"{tournament.start_date} à {tournament.place} et finira le "
              f"{tournament.end_date}.\n"
              f"Il y aura {tournament.number_round} tour.")
