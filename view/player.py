"""
Enter the information of the players who will participate in the tournament.
"""


class PlayerView:
    """The player information you need to organize a tournament."""
    
    @staticmethod
    def define_first_name():
        """Define the first-name of participants."""
        while True:
            first_name = input("Veillez saisir le prénom du joueur: ")
            first_name = first_name.capitalize()
            if not first_name.isalpha():
                print("Le prénom n'est pas valide.")
            else:
                return first_name
    
    @staticmethod
    def define_last_name():
        """Define the last_name of participants."""
        while True:
            last_name = input("Saisissez son nom de famille: ")
            last_name = last_name.capitalize()
            if not last_name.isalpha():
                print("Le nom n'est pas valide.")
            else:
                return last_name
    
    @staticmethod
    def define_date_of_birth():
        """Define the birthday of participants."""
        date_of_birth = input("Indiquez sa date de naissance: ")
        return date_of_birth
    
    @staticmethod
    def define_gender():
        """Define the gender of participants."""
        while True:
            gender = input("Est-ce un homme ou une femme, choisissez H ou F: ")
            if gender == "F":
                return "une femme"
            elif gender == "f":
                return "une femme"
            elif gender == "H":
                return "un homme"
            elif gender == "h":
                return "un homme"
            else:
                gender = False
                if not gender:
                    print(f"Erreur: \n"
                          f" Saisissez H pour un homme ou F pour une femme.")
    
    @staticmethod
    def define_ranking():
        """Define the ranking of participants."""
        while True:
            ranking = input("Indiquez sa place au classement national: ")
            if not ranking.isdigit():
                print("Information non valide, saisissez un nombre.")
            else:
                return ranking
    
    @staticmethod
    def new_player():
        first_name = PlayerView.define_first_name()
        last_name = PlayerView.define_last_name()
        date_of_birth = PlayerView.define_date_of_birth()
        gender = PlayerView.define_gender()
        ranking = PlayerView.define_ranking()
        return [first_name, last_name, date_of_birth, gender, ranking]

    @staticmethod
    def display_player(player):
        print(f"Bienvenue {player.first_name} {player.last_name},\n"
              f"vous êtes {player.gender}, né le "
              f"{player.date_of_birth}.\n"
              f"Actuellement, vous êtes {player.ranking}ème au classement "
              f"national.\n"
              f"Nous validons votre inscription et vous souhaitons bonne "
              f"chance")
