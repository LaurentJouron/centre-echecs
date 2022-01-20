"""Enter the information of the players who will participate in the tournament."""


class PlayerView:
    """The player information you need to organize a tournament."""

    def define_name(self):
        """Define the last_name of participants."""
        last_name = input("Saisissez le nom du joueur: ")
        if not isinstance(last_name, str):
            raise ValueError("Les noms doivent contenir uniquement des lettres!")
        return last_name

    def define_first_name(self):
        """Define the first-name of participants."""
        first_name = input("Saisissez le prénom du joueur: ")
        if not isinstance(first_name, str):
            raise ValueError("Les prénoms doivent contenir uniquement des lettres!")
        return first_name

    def define_birthday(self):
        """Define the birthday of participants."""
        birthday = input("Saisissez la date de naissance du joueur: ")
        return birthday

    def define_gender(self):
        """Define the gender of participants."""
        gender = input("Saisissez le sexe du joueur, H ou F: ")
        if gender == "F" or "f":
            return "une femme"
        if gender == "H" or "h":
            return "un homme"
        else:
            return False

    def define_ranking(self):
        """Define the gender of participants."""
        ranking = input("Saisissez la place au classement national du joueur: ")
        return ranking

    def get_input_player(self):
        last_name = self.define_last_name()
        first_name = self.define_first_name()
        birthday = self.define_birthday()
        gender = self.define_gender()
        ranking = self.define_ranking()
        return [last_name, first_name, birthday, gender, ranking]
