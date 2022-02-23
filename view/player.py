"""Enter the information of the players who will participate."""

from datetime import datetime


class PlayerView:
    """The player information you need to organize a tournament."""
    new_player = 0

    def __init__(self):
        PlayerView.new_player += 1

    def define_first_name(self):
        """Define the first-name of participants."""
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                print("Invalid first name")
            else:
                return first_name.capitalize()

    def define_last_name(self):
        """Define the last_name of participants."""
        while True:
            last_name = input("Enter the last name: ")
            if not last_name.isalpha():
                print("Invalid name")
            else:
                return last_name.capitalize()

    def define_date_of_birth(self):
        """Define the birthday of participants."""
        birthday = input("Enter his date of birth: ")
        birthday = datetime.strptime(birthday, "%d%m%Y").\
            strftime("%A %d %B %Y")
        return birthday

    def define_gender(self):
        """Define the gender of participants."""
        while True:
            gender = input("Select M for men or F for women: ")
            gender = gender.upper()
            if gender == "F":
                return "a woman"
            elif gender == "M":
                return "a man"
            else:
                gender = False
                if not gender:
                    print(f"Input error")

    def define_ranking(self):
        """Define the ranking of participants."""
        while True:
            ranking = input("Indicate its place in the national ranking: ")
            if ranking == "1":
                return f"{ranking}st"
            if ranking == "2":
                return f"{ranking}nd"
            if ranking == "3":
                return f"{ranking}rd"
            if ranking >= "4":
                return f"{ranking}th"
            else:
                ranking = False
                if not ranking:
                    print(f"Input error")

    def get_player_information(self):
        """Compilation of information."""
        first_name = self.define_first_name()
        last_name = self.define_last_name()
        birthday = self.define_date_of_birth()
        gender = self.define_gender()
        ranking = self.define_ranking()
        return [first_name, last_name, birthday, gender, ranking]

    def display_player(self, player):
        confirmation = " Confirmation "
        print(f"\n {confirmation.center(90,'-')}")
        print(f"{player.first_name} {player.last_name} is {player.gender}, "
              f"born on {player.birthday}.\n"
              f"He is currently {player.ranking} in national ranking. \n"
              f"His registration is validated.\n"
              f"Good luck!\n")
        print(f"Il y a {PlayerView.new_player} joueur enregistré.")
