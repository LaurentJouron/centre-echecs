"""Enter the information of the players who will participate."""
from datetime import datetime


class PlayerView:
    """The player information you need to organize a tournament."""

    @staticmethod
    def define_first_name():
        """Define the first-name of participants."""
        while True:
            first_name = input("Please enter the player’s first name: ")
            if not first_name.isalpha():
                print("Invalid first name")
            return first_name.capitalize()

    @staticmethod
    def define_last_name():
        """Define the last_name of participants."""
        while True:
            last_name = input("Enter the last name: ")
            if not last_name.isalpha():
                print("Invalid name")
            return last_name.capitalize()

    @staticmethod
    def define_birthday():
        """Define the birthday of participants."""
        birthday = input("Enter his date of birth: ")
        birthday = datetime.strptime(birthday, "%d%m%Y").\
            strftime("%A %d %B %Y")
        return birthday

    @staticmethod
    def define_gender():
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

    @staticmethod
    def define_ranking():
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

    @staticmethod
    def get_all_information():
        first_name = PlayerView.define_first_name()
        last_name = PlayerView.define_last_name()
        birthday = PlayerView.define_birthday()
        gender = PlayerView.define_gender()
        ranking = PlayerView.define_ranking()
        return first_name, last_name, birthday, gender, ranking
