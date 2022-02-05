"""Enter the information of the players who will participate."""

from datetime import datetime


class PlayerView:
    """The player information you need to organize a tournament."""
    def __init__(self):
        pass
    
    def define_first_name(self):
        """Define the first-name of participants."""
        while True:
            first_name = input("Veuillez saisir le prénom du joueur: ")
            if not first_name.isalpha():
                print("Prénom invalide")
            else:
                return first_name.capitalize()
    
    def define_last_name(self):
        """Define the last_name of participants."""
        while True:
            last_name = input("Saisissez le nom de famille: ")
            if not last_name.isalpha():
                print("Nom invalide")
            else:
                return last_name.capitalize()
    
    def define_date_of_birth(self):
        """Define the birthday of participants."""
        date_of_birth = input("Indiquez sa date de naissance: ")
        date_of_birth = datetime.strptime(date_of_birth,
                                          "%d%m%Y").strftime("%A %d %B %Y")
        return date_of_birth
    
    def define_gender(self):
        """Define the gender of participants."""
        while True:
            gender = input("Sélectionnez H pour homme ou F pour femme: ")
            gender = gender.upper()
            if gender == "F":
                return "une femme"
            elif gender == "H":
                return "un homme"
            else:
                gender = False
                if not gender:
                    print(f"Erreur de saisie")
    
    def define_ranking(self):
        """Define the ranking of participants."""
        while True:
            ranking = input("Indiquez sa place au classement national: ")
            if ranking == "1":
                return f"{ranking}er"
            if ranking >= "1":
                return f"{ranking}ème"
            else:
                ranking = False
                if not ranking:
                    print(f"Erreur de saisie")

    def get_player_information(self):
        """Compilation of information."""
        first_name = self.define_first_name()
        last_name = self.define_last_name()
        date_of_birth = self.define_date_of_birth()
        gender = self.define_gender()
        ranking = self.define_ranking()
        return [first_name, last_name, date_of_birth, gender, ranking]

    def display_player(self, player):
        confirmation = " Confirmation "
        print(f"\n {confirmation.center(90,'-')}")
        print(f"\n{player.first_name} {player.last_name} est {player.gender}, "
              f"né le {player.date_of_birth}.\n"
              f"Il est actuellement, {player.ranking} au classement "
              f"national.\n"
              f"Son inscription est validée.\n"
              f"Bonne chance!")
