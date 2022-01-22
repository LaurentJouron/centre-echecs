"""Enter the information of the players who will participate in the tournament."""


class PlayerView:
    """The player information you need to organize a tournament."""

    def __init__(self, name, surname, date_of_birth, sexe, classification):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.classification = classification

        print(f"Bienvenue {last_name} {first_name},")
        print(f"vous êtes {gender}, né le {birthday}.")
        print(f"Actuellement, vous êtes {ranking}ème au classement national.")
        print(f"Nous validons votre inscription et vous souhaitons bonne chance")


last_name = input("Veuillez saisir le nom de famille: ")
first_name = input("Veuillez saisir le prénom du joueur: ")
birthday = input("Veuillez saisir la date de naissance du joueur: ")
gender = input("Veuillez saisir le sexe du joueur: ")
ranking = input("Saisissez la place au classement national du joueur: ")
