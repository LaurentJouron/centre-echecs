"""Entry point."""
from controller.tournament import TournamentController as TC
from controller.player import PlayerController as PC

global_tournament = None


class GlobalAppli:
    @staticmethod
    def start_app():
        welcome = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome.center(106, ' ')}")
        instruction = " Please follow the instructions below "
        print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def input():
        order = input(f"Please enter an order : ").capitalize()
        order = int(order)
        return order

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def information():
        choice = " Enter information "
        print(f"{choice.center(106, '*')}")


class Reception:
    @staticmethod
    def reception():
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, '~')}")
        GlobalAppli.choice()
        to_do = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
        print(f"\n{to_do.center(106, '-')}")
        order = GlobalAppli.input()
        return order


class Player:
    @staticmethod
    def player_reception():
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, '~')}")
        GlobalAppli.choice()
        list_of_choice = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")
        order = GlobalAppli.input()
        return order

    @staticmethod
    def create():
        player_reception = " PLAYER CREATION "
        print(f"\n{player_reception.center(106, '~')}")
        GlobalAppli.information()
        create = PC.create()
        print(repr(create))

    @staticmethod
    def all():
        player_reception = " GET ALL PLAYERS "
        print(f"\n{player_reception.center(106, '~')}")
        PC.get_all()

    @staticmethod
    def remove():
        player_reception = " PLAYER REMOVED "
        print(f"\n{player_reception.center(106, '~')}")
        GlobalAppli.information()
        PC.remove()


class Tournament:
    @staticmethod
    def tournament_reception():
        """Management tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.choice()
        list_of_choice = "> [1]Create  [2]Add player  [3]Join  [4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")
        order = GlobalAppli.input()
        return order

    @staticmethod
    def tournament_validation():
        tournament_reception = " TOURNAMENT VALIDATION "
        print(f"\n{tournament_reception.center(106, '~')}")
        validate = "> [1]Modify  [2]Validate <"
        print(f"{validate.center(106, '-')}")
        order = GlobalAppli.input()
        return order

    @staticmethod
    def new_tounament():
        tournament_reception = " TOURNAMENT CREATION "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.information()
        tournament_controller = TC.new_tournament()
        print(str(tournament_controller))

    @staticmethod
    def player_tournament():
        tournament_reception = " REGISTER TOURNAMENT PLAYERS "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.information()
        TC.append_player(global_tournament)


if __name__ == '__main__':

    GlobalAppli.start_app()
    reception = None
    while reception == 1 or 2 or 3 or 4:
        reception = Reception.reception()
        reception = int(reception)
        if reception == 1:
            order = None
            while order == 1 or 2 or 3:
                order = Player.player_reception()
                if order == 1:
                    Player.create()
                if order == 2:
                    Player.all()
                if order == 3:
                    Player.remove()
                if order == 4:
                    continue
        if reception == 2:
            tournament = Tournament.tournament_reception()
            tournament = int(tournament)
            while tournament == 1:
                Tournament.new_tounament()
                validation = Tournament.tournament_validation()
                while validation == 1:
                    tournament_controller = TC.new_tournament()
                    print(str(tournament_controller))
                    validation = Tournament.tournament_validation()
                if validation == 2:
                    continue
            if tournament == 2:
                Tournament.player_tournament()
