"""Tournament player registration management"""


class PlayerController:
    """The player information you need to organize a tournament."""

    def define_name(self):
        """Define the name of participants."""
        name = input("Saisissez le nom du joueur: ")
        if not isinstance(name, str):
            raise ValueError("Les noms ne doivent contenir que des lettres!")
        if name in self:
            print(f"{name} est déjà inscrit.")
            return False
        # self.appends(name)
        return name

    def define_first_name(self):
        """Define the first-name of participants."""
        first_name = input("Saisissez le prénom du joueur: ")
        if not isinstance(first_name, str):
            raise ValueError("Les prénoms ne doivent contenir que des lettres!")
        # self.appends(first_name)
        return first_name

    def define_birthday(self):
        """Define the birthday of participants."""
        birthday = input("Saisissez la date de naissance du joueur: ")
        return birthday

    def define_gender(self):
        """Define the gender of participants."""
        gender = input("H / F: ")
        return gender

    def define_ranking(self):
        """Define the gender of participants."""
        ranking = input("Saisissez la place au classement national du joueur: ")
        return ranking

    def remove(self, name):
        if name in self:
            self.remove(name)
            return True
        return False

    name = define_name("name")
    first_name = define_first_name("first_name")
    birthday = define_birthday("birthday")
    gender = define_gender("gender ")
    ranking = define_ranking("ranking")


    print(f"Bienvenue {first_name} {name}, vous êtes {gender}, né le {birthday}.")
    print(f"Actuellement, vous êtes {ranking}ème au classement national.")
    print(f"Nous validons votre inscription et vous souhaitons bonne chance")
