"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController

global_tournament = None


class GlobalAppli:
    # @staticmethod
    # def start_app():
    #     welcome = " Welcome to the << CHESS-CENTER >> application "
    #     print(f"\n{welcome.center(106, ' ')}")
    #     instruction = " Please follow the instructions below "
    #     print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def input():
        choice = input(f"Please enter an order : ").capitalize()
        choice = int(choice)
        return choice

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def information():
        choice = " Enter information "
        print(f"{choice.center(106, '*')}")


class Reception:
    pass
    # @staticmethod
    # def reception():
    #     reception_name = " RECEPTION "
    #     print(f"\n{reception_name.center(106, '~')}")
    #     GlobalAppli.choice()
    #     to_do = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
    #     print(f"\n{to_do.center(106, '-')}")
    #     order = GlobalAppli.input()
    #     return order


class Player:
    @staticmethod
    def reception():
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
        create = PlayerController.create()
        print(repr(create))

    @staticmethod
    def all():
        player_reception = " GET ALL PLAYERS "
        print(f"\n{player_reception.center(106, '~')}")
        PlayerController.get_all()

    @staticmethod
    def remove():
        player_reception = " PLAYER REMOVED "
        print(f"\n{player_reception.center(106, '~')}")
        GlobalAppli.information()
        PlayerController.remove()


class Tournament:
    @staticmethod
    def reception():
        """Management tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.choice()
        list_of_choice = "> [1]Create  [2]Add player  [3]Display player  " \
                         "[4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")
        order = GlobalAppli.input()
        return order

    @staticmethod
    def validation():
        tournament_reception = " TOURNAMENT VALIDATION "
        print(f"\n{tournament_reception.center(106, '~')}")
        validate = "> [1]Modify  [2]Validate <"
        print(f"{validate.center(106, '-')}")
        order = GlobalAppli.input()
        return order

    @staticmethod
    def create():
        tournament_reception = " TOURNAMENT CREATION "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.information()
        tournament_controller = TournamentController()
        tournament = tournament_controller.new_tournament()
        print(str(tournament))
        global_tournament = tournament
        return global_tournament

    @staticmethod
    def append_player():
        tournament_reception = " REGISTER TOURNAMENT PLAYERS "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.information()
        TournamentController.append_player(global_tournament)

    @staticmethod
    def display_player():
        tournament_reception = " DISPLAY TOURNAMENT PLAYERS "
        print(f"\n{tournament_reception.center(106, '~')}")
        GlobalAppli.information()
        TournamentController.display_players_list(global_tournament)


if __name__ == '__main__':

    GlobalAppli.start_app()
    reception = None
    while reception == 1 or 2 or 3 or 4:
        reception = Reception.reception()
        reception = int(reception)
        if reception == 1:
            order = None
            while order == 1 or 2 or 3:
                order = Player.reception()
                if order == 1:
                    Player.create()
                if order == 2:
                    Player.all()
                if order == 3:
                    Player.remove()
                if order == 4:
                    continue
        if reception == 2:
            tournament = Tournament.reception()
            tournament = int(tournament)
            while tournament == 1:
                Tournament.create()
                validation = Tournament.validation()
                while validation == 1:
                    Tournament.create()
                if validation == 2:
                    continue
            if tournament == 2:
                Tournament.append_player()
            if tournament == 3:
                Tournament.display_player()
            if tournament == 4:
                continue
