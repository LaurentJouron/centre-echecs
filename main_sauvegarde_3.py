"""Entry point."""
from controller.tournament import TournamentController as TC
from controller.player import PlayerController as PC

global_tournament = None


class Reception:
    @staticmethod
    def start_app():
        welcome = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome.center(106, ' ')}")
        instruction = " Please follow the instructions below "
        print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def reception():
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, '~')}")

        Reception.choice()

        to_do = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
        print(f"\n{to_do.center(106, '-')}")

        """Management reception"""
        order = Reception.input()
        return order

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def input():
        order = input(f"Please enter an order : ").capitalize()
        order = int(order)
        return order

    @staticmethod
    def player_reception():
        player_reception = " PLAYER RECEPTION "
        print(f"\n{player_reception.center(106, '~')}")
        Reception.choice()
        list_of_choice = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")
        """Management player reception"""
        order = Reception.input()
        return order

    @staticmethod
    def tournament_reception():
        """Management tournament reception"""
        tournament_reception = " TOURNAMENT RECEPTION "
        print(f"\n{tournament_reception.center(106, '~')}")
        Reception.choice()
        list_of_choice = "> [1]Create  [2]Add player  [3]Join  [4]Quit <"
        print(f"\n{list_of_choice.center(106, '-')}")
        """Management of players on the national list"""
        order = Reception.input()
        return order

    @staticmethod
    def tournament_validation():
        validate = "> [1]Modify  [2]Validate <"
        print(f"{validate.center(106, '-')}")
        order = input(f"Please enter an order : ")
        order = int(order)
        return order


def player():
    order = None
    while order == 1 or 2 or 3 or 4:
        order = Reception.player_reception()
        if order == 1:
            create = PC.create()
            print(repr(create))
        if order == 2:
            PC.get_all()
        if order == 3:
            PC.remove()
        if order == 4:
            break


def tournament():
    order = None
    while order == 1 or 2 or 3 or 4:
        order = Reception.tournament_reception()
        if order == 1:
            tournament_controller = TC.new_tournament()
            print(str(tournament_controller))

            # global_tournament = tournament_controller

            validate = Reception.tournament_validation()
            while validate == 1:
                tournament_controller = TC.new_tournament()
                print(str(tournament_controller))
            if validate == 2:
                Reception.tournament_reception()
            else:
                print("Value error.")

        if order == 2:
            tournament_player = " Register tournament players "
            print(f"{tournament_player.center(106, '-')}")
            TC.append_player(global_tournament)

        if order == 3:
            players_tournament = " Select players for this tournament "
            print(f"\n{players_tournament.center(106, '*')}\n")
            tournament_player = "> [1]add player [2]Display players [3]play <"
            print(f"{tournament_player.center(106, '-')}")
            Reception.input()

        if order == 4:
            break


if __name__ == '__main__':

    Reception.start_app()
    reception = Reception.reception()
    int(reception)
    while reception == 1 or 2 or 3 or 4:
        if reception == 1:
            player()
        if reception == 2:
            tournament()
        if reception == 3:
            pass
        if reception == 4:
            pass
        else:
            print("Value error.")
