"""Entry point."""
from controller.tournament import TournamentController as TC
from controller.player import PlayerController as PC

global_tournament = None


def reception():
    to_do = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
    print(f"{to_do.center(106, '-')}")

    """Management of players on the national list"""
    order = input(f"Please enter an order : ").capitalize()
    order = int(order)
    return order


def player():
    """Text decoration"""
    choice = " Make your choice "
    print(f"\n{choice.center(106, '*')}")

    list_of_choice = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
    print(f"{list_of_choice.center(106, '-')}")

    """Management of players on the national list"""
    order = input(f"Please enter an order : ").capitalize()
    order = int(order)
    while order == 1 or 2 or 3 or 4:
        if order == 1:
            create = PC.create()
            print(repr(create))
        if order == 2:
            PC.get_all()
        if order == 3:
            PC.remove()
        if order == 4:
            reception()
        if order != 1 or 2 or 3 or 4:
            print("Value error.")

        list_of_choice = "> [1]Add  [2]Show  [3]Remove  [4]Quit <"
        print(f"{list_of_choice.center(106, '-')}")

        """Management of players on the national list"""
        order = input(f"Please enter an order : ").capitalize()
        order = int(order)


def tournament():
    """Text decoration"""
    choice = " Make your choice "
    print(f"{choice.center(106, '*')}")

    list_of_choice = "> [1]Create  [2]Add player  [3]Join  [4]Quit <"
    print(f"{list_of_choice.center(106, '-')}")

    """Management of players on the national list"""
    order = input(f"Please enter an order : ").capitalize()
    order = int(order)
    if order == 1:
        tournament_controller = TC.new_tournament()
        print(str(tournament_controller))

        # global_tournament = tournament_controller

        validate = "> [1]Modify  [2]Validate <"
        print(f"{validate.center(106, '-')}")
        validate = input(f"Please enter an order : ")
        validate = int(validate)
        while validate == 1:
            tournament_controller = TC.new_tournament()
            print(str(tournament_controller))

            validate = "> [1]Modify  [2]Validate <"
            print(f"{validate.center(106, '-')}")
            validate = input(f"Please enter an order : ")
            validate = int(validate)

    if order == 2:
        tournament_player = " Register tournament players "
        print(f"{tournament_player.center(106, '-')}")
        TC.append_player(global_tournament)


if __name__ == '__main__':
    """Decoration text"""
    welcome = " Welcome to the << CHESS-CENTER >> application "
    print(f"\n{welcome.center(106, ' ')}\n")

    instruction = " Please follow the instructions below "
    print(f"{instruction.center(106, ' ')}\n")

    choice = " Make your choice "
    print(f"{choice.center(106, '*')}")

    reception = reception()
    while reception == 1 or 2 or 3 or 4:
        int(reception)
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

    #
    #             if tournament_start == 2:
    #                 players_tournament = " Select players for this tournament "
    #                 print(f"\n{players_tournament.center(106, '*')}\n")
    #
    #                 tournament_player = "> 1 = add player / " \
    #                                     "2 = Display players / 3 = play <"
    #                 print(f"{tournament_player.center(106, '-')}")
    #
    #                 tournament_player = input(f"Select : ")
    #                 tournament_player = int(tournament_player)
    #
    #                 while tournament_player != 3:
    #                     if tournament_player == 1:
    #                         tournament_player = " Register tournament players "
    #                         print(f"{tournament_player.center(106, '-')}")
    #
    #                         append_player = TournamentController.\
    #                             append_player(global_tournament)
    #
    #                     if tournament_player == 2:
    #                         display_players_list = TournamentController.display_players_list(global_tournament)
    #                         print(display_players_list)
    #
    #                     # if tournament_player == 3:
    #                     #     pass
