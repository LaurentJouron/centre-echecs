"""
Enter the information of the players who will participate in the tournament.
"""


class PlayerView:
    """The player information you need to organize a tournament."""

    def define_first_name():
        """Define the first-name of participants."""
        first_name = input("Veillez saisir le prénom du joueur: ").capitalize()
        if not isinstance(first_name, str):
            print("Le prénom n'est pas valide.")
        else:
            return first_name

    def define_last_name():
        """Define the last_name of participants."""
        last_name = input("Saisissez son nom de famille: ").capitalize()
        if not isinstance(last_name, str):
            print("Le nom n'est pas valide.")
        else:
            return last_name

    def define_date_of_birth():
        """Define the birthday of participants."""
        date_of_birth = input("Indiquez sa date de naissance: ")
        return date_of_birth

    def define_gender():
        """Define the gender of participants."""
        gender = input("Est-ce un homme ou une femme, choisissez H ou F: ")
        return gender

    def define_ranking():
        """Define the ranking of participants."""
        ranking = input("Indiquez sa place au classement national: ")
        if not ranking.isdigit():
            print("Information non valide, saisissez un nombre.")
        else:
            return ranking


new_player = [PlayerView.define_first_name(),
              PlayerView.define_last_name(),
              PlayerView.define_date_of_birth(),
              PlayerView.define_gender(),
              PlayerView.define_ranking()]
print(new_player)

