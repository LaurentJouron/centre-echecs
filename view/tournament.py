"""Enter information for the tournament organization."""
import constant
from datetime import date
from datetime import timedelta

number_of_players = constant.NUMBER_OF_PLAYERS
number_of_round = constant.NUMBER_OF_ROUND
number_of_day = constant.NUMBER_OF_DAY


class TournamentView:
    """What information is needed for the tournament."""
    def __init__(self):
        pass
        
    def name_of_tournament(self):
        """Name the tournament."""
        name: str = input("Enter the name of the tournament: ")
        return name.capitalize()
    
    def tournament_venue(self):
        """Where the tournament goes."""
        place: str = input("Venue of the tournament: ")
        return place.capitalize()
    
    def get_tournament_start_date(self):
        """On what date the tournament begins."""
        return date.today()
    
    def get_tournament_end_date(self):
        """Tournament end date."""
        end_date = self.get_tournament_start_date() + timedelta(
            days=number_of_day)
        if end_date == self.get_tournament_start_date():
            return "same day"
        else:
            return end_date

    def organize_new_tournament(self):
        """Gathering of elements of the tournament class."""
        name = self.name_of_tournament()
        place = self.tournament_venue()
        start_date = self.get_tournament_start_date()
        end_date = self.get_tournament_end_date()
        number_round = number_of_round
        number_players = number_of_players
        return [name, place, start_date, end_date, number_round,
                number_players]
    
    def display_tournament_organization(self, tournament):
        """Confirmation phrase of the tournament class."""
        start_of_tournament = " Start of the tournament "
        print(f"\n {start_of_tournament.center(90, '-')}")
        print(f"The {tournament.name} chess tournament starts on "
              f"{tournament.start_date} at 9:00 am and end on"
              f" {tournament.end_date} at 6:00 pm.\n"
              f"He takes place {tournament.place} with"
              f" {number_of_players} "
              f"players in {number_of_round} rounds.\n")
