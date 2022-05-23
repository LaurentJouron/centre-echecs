"""Management of the tournament organization"""
from view.tournament import TournamentView
from model.tournament import TournamentModel


class TournamentController:
        
    @staticmethod
    def new_tournament():
        """
        imports the data of the views
        and passes these data parameters in the models.
        """
        name = TournamentView.name()
        place = TournamentView.place()
        start_date = TournamentView.start_date()
        end_date = TournamentView.end_date()

        tournament = TournamentModel(name=name,
                                     place=place,
                                     start_date=start_date,
                                     end_date=end_date)
        print(str(tournament))
        return tournament

    @staticmethod
    def number_players():
        """Get the number of players of this tournament."""
        number_of_players = TournamentView.number_players()
        return number_of_players

    @staticmethod
    def number_rounds():
        """Get the number of rounds of this tournament."""
        number_of_rounds = TournamentView.number_rounds()
        return number_of_rounds
