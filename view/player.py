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
    def define_date_of_birth():
        """Define the birthday of participants."""
        date_of_birthday = input("Enter his date of birth: ")
        date_of_birthday = datetime.strptime(date_of_birthday, "%d%m%Y").\
            strftime("%A %d %B %Y")
        return date_of_birthday

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

    def get_all_information(self):
        first_name = self.define_first_name()
        last_name = self.define_last_name()
        birthday = self.define_date_of_birth()
        gender = self.define_gender()
        ranking = self.define_ranking()
        return first_name, last_name, birthday, gender, ranking
