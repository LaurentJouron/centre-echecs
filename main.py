"""Entry point."""
from controller.tournament import TournamentController
from controller.player import PlayerController
from controller.global_app import StartApp

global_tournament = None


if __name__ == '__main__':
    
    StartApp.first_run()
    reception = True
    while reception:
        reception = StartApp.next_run()
        if reception == 1:
            players = True
            while players:
                players = PlayerController.start_player_menu()
                if players >= 5:
                    print("Value error.")
                if players == 1:
                    PlayerController.create()
                if players == 2:
                    PlayerController.get_all()
                if players == 3:
                    PlayerController.remove()
                if players == 4:
                    break

        if reception == 2:
            TournamentController.tournament_reception()
            tournament = True
            while tournament:
                if tournament == 1:
                    tournament = TournamentController.new_tournament()
                    print(str(tournament))
                    global_tournament = tournament
                    validate = True
                    while validate:
                        validate = TournamentController.tournament_validate()
                        if validate == 1:
                            tournament = TournamentController.new_tournament()
                            print(str(tournament))
                            global_tournament = tournament
                        if validate == 2:
                            break

                if tournament == 2:
                    pass

        # if reception == 3:
        #     pass
        if reception == 4:
            exit()
