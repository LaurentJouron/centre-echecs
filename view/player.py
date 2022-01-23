"""Enter the information of the players who will participate in the tournament."""


class PlayerView:
    """The player information you need to organize a tournament."""

    name = input("Veuillez saisir le nom de famille: ")
    surname = input("Veuillez saisir le prénom du joueur: ")
    date_of_birth = input("Veuillez saisir la date de naissance du joueur: ")
    sexe = input("Veuillez saisir le sexe du joueur: ")
    classement = input("Saisissez la place au classement national du joueur: ")

    def __init__(self, name, surname, date_of_birth, sexe, classement):
        self.last_name = name
        self.first_name = surname
        self.birthday = date_of_birth
        self.gender = sexe
        self.ranking = classement

    def welcome(self):
        print(f"Bienvenue {last_name} {first_name},")
        print(f"vous êtes {gender}, né le {birthday}.")
        print(f"Actuellement, vous êtes {ranking}ème au classement national.")
        print(f"Nous validons votre inscription et vous souhaitons bonne chance")


last_name = PlayerView.name
first_name = PlayerView.surname
birthday = PlayerView.date_of_birth
gender = PlayerView.sexe
ranking = PlayerView.classement

player = PlayerView(last_name, first_name, birthday, gender, ranking)
player.welcome()
