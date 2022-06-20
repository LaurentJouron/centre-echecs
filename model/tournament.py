"""Information of the chess tournament."""
import csv
import json
import os

from tinydb import TinyDB


class TournamentModel:
    """Builder of the model tournament."""
    def __init__(self, name, place, start_date, end_date, nb_rounds,
                 nb_players):
        self.name: str = name
        self.place: str = place
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.nb_rounds: int = nb_rounds
        self.nb_players: int = nb_players
        self.players: list = []
        self.rounds: list = []

    def __str__(self):
        """Confirmation phrase of the tournament class."""
        return f"\nThe {self.name} chess tournament starts on " \
               f"{self.start_date} at 9:00 am, and end on " \
               f"{self.end_date} at 6:00 pm.\n" \
               f"He takes place in {self.place}.\n" \
               f"It will be played with {self.nb_players} players in " \
               f"{self.nb_rounds} rounds."

    def append_player(self, player):
        """Adds players to the tournament list."""
        len_players = len(self.players)
        if len_players < self.nb_players:
            self.players.append(player)
            print(f"\nThere are {len_players  + 1} remains place.")
            remains_place = self.nb_players - len_players
            print(f"There are {remains_place - 1} places left.")
        else:
            print("This tournament is completed")

    def get_players_list(self):
        """Display players from tournament list."""
        return self.players[:]

    def remove_player(self, player):
        """Remove player in tournament list."""
        self.players.remove(player)

# New script
    def tournament_table(self):
        """Create a file for each new tournament."""
        name_table = self.name.lower()
        db = TinyDB(f"data/{name_table}.json", indent=4)
        return db.table(f'{name_table}')

    def openning_tournament_table(self):
        """Open the file that corresponds to a tournament."""
        name_table = self.name.lower()
        with open(f"data/{name_table}.json") as tournament_file:
            return json.load(tournament_file)

    def first_rounds(self):
        players = self.players
        len_players = len(players)
        if len_players == self.nb_players:
            for rounds in range(self.nb_players//2):
                self.rounds.extend(players[rounds::4])
                rounds += 1

    # players = ["Thierno", "Laurent", "Louis", "Antoine", "Virginie", "Marie", "Stephane", "Julia"]
    # len_players = len(players)
    # if len_players == 8:
    #     for rounds in range(8 // 2):
    #         print(players[rounds::4])
    #         rounds += 1

    def alphabetical_order(self):
        players = self.players
        players.sort()
        return players

    def ranking_order(self):
        sorted(self.players, key=lambda ranking: ranking[4])

    def create_csv_files(self):
        tournament_files = "./tournament_files"
        os.makedirs(tournament_files, exist_ok=True)
        csv_name = f"{self.name}.csv"
        if not os.path.isfile(f"tournament_files/{csv_name}"):
            headers = "first_name, last_name, birthday, gender, " \
                      "ranking, score\n"
            with open(csv_name, "w", newline="", encoding="utf8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(headers)

    def write_csv_files(self):
        with open(f"{self.name}", "w", newline="", encoding="utf8") as f:
            headers = "first_name, last_name, birthday, gender, " \
                      "ranking, score\n"
            f.write(headers)

    def read_csv_files(self):
        if not os.path.isfile(f"data/{self.name}.json"):
            with open(f"{self.name}", "r", encoding="utf8") as f:
                header_line = f.readline()
                print(header_line)
                file = f.readlines()
                for players in file:
                    player = players[:-1].split(",")
                    print(player)
