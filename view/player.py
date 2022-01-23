"""
Enter the information of the players who will participate in the tournament.
"""


class PlayerView:
    """The player information you need to organize a tournament."""

    """Information we need for the player class."""
    first_name = input("Veillez saisir le prénom du joueur: ")
    last_name = input("Merci de saisir son nom de famille: ")
    date_of_birth = input("Quelle est sa date de naissance: ")
    gender = input("Veillez précisez son sexe H or F: ")
    ranking = input("Saisissez la place au classement national du joueur: ")

    def __init__(self, first_name, last_name, birthday, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    @staticmethod
    def define_first_name(first_name):
        """Define the first-name of participants."""
        PlayerView.first_name = first_name
        if not isinstance(first_name, str):
            raise ValueError("Le prénom n'est pas valide.")
        else:
            return first_name

    @staticmethod
    def define_last_name(last_name):
        """Define the last_name of participants."""
        PlayerView.last_name = last_name
        if not isinstance(last_name, str):
            raise ValueError("Le nom n'est pas valide.")
        else:
            return last_name

    @staticmethod
    def define_date_of_birth(new_player):
        """Define the birthday of participants."""
        PlayerView.date_of_birth = new_player

    @staticmethod
    def define_gender(new_player):
        """Define the gender of participants."""
        PlayerView.gender = new_player

    @staticmethod
    def define_ranking(ranking):
        """Define the ranking of participants."""
        PlayerView.ranking = ranking
        if not isinstance(ranking, int):
            raise ValueError("Information non valide, saisissez un nombre.")
        else:
            return ranking

    @staticmethod
    def validation_participation():
        print(f"Bienvenue {PlayerView.first_name} {PlayerView.last_name},")
        print(f"Vous êtes {PlayerView.gender}, "
              f"né le {PlayerView.date_of_birth}")
        print(f"Actuellement, vous êtes {PlayerView.ranking}ème "
              f"au classement national.")
        print(f"Nous validons votre inscription "
              f"et vous souhaitons bonne chance.")


create_player = ([PlayerView.first_name,
                  PlayerView.last_name,
                  PlayerView.gender,
                  PlayerView.date_of_birth,
                  PlayerView.ranking])

PlayerView.validation_participation()
