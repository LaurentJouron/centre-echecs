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
            tournament_reception = True
            while tournament_reception:
                tournament_reception = TournamentController.tournament_reception()
                if tournament_reception >= 5:
                    print("Value error.")
                if tournament_reception == 1:
                    TournamentController.new_tournament()
                if tournament_reception == 2:
                    TournamentController.append_player(global_tournament)
                if tournament_reception == 3:
                    TournamentController.display_players_list(global_tournament)
                if tournament_reception == 4:
                    break
        # if reception == 3:
        #     pass
        if reception == 4:
            exit()
