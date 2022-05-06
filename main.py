"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController
from controller import global_app

global_tournament = None


if __name__ == '__main__':

    global_app.first_run()
    reception = True
    while reception:
        if reception == 1:
            players = True
            while players:
                players = PlayerController.start_player_menu()
                if players == 1:
                    PlayerController.create()
                if players == 2:
                    PlayerController.get_all()
                if players == 3:
                    PlayerController.remove()
                if players == 4:
                    players = False

        if reception == 2:
            tournament = True
            while tournament:
                if tournament == 1:
                    tournament_controller = TournamentController()
                    tournament = tournament_controller.new_tournament()
                    print(str(tournament))
                    global_tournament = tournament
                    validation = True
                    while validation:
                        validation = TournamentController.tournament_validate()
                        if validation == 1:
                            pass

                            # if tournament == 2:
                    pass

        # if reception == 3:
        #     pass
        if reception == 4:
            exit()
