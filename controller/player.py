"""Tournament player registration management"""


class PlayerController:
    """The player information you need to organize a tournament."""

    def define_name():
        """Define the name of participants."""
        name = input("Saisissez le nom du joueur: ")
        return name

    def define_first_name():
        """Define the first-name of participants."""
        first_name = input("Saisissez le prénom du joueur: ")
        return first_name

    def define_birthday():
        """Define the birthday of participants."""
        birthday = input("Saisissez la date de naissance du joueur: ")
        return birthday

    def define_gender():
        """Define the gender of participants."""
        gender = (input("H / F: "))
        if gender == "F" or "f":
            gender = "une femme"
        if gender == "H" or "h":
            gender = "un homme"
        return gender

    def define_ranking():
        """Define the gender of participants."""
        ranking = input("Saisissez la place au classement national du joueur: ")
        return ranking

    name = define_name()
    first_name = define_first_name()
    birthday = define_birthday()
    gender = define_gender()
    ranking = define_ranking()

    print(f"Bienvenue {first_name} {name}, vous êtes {gender}, né le {birthday}.")
    print(f"Actuellement, vous êtes {ranking}ème au classement national.")
    print(f"Nous validons votre inscription et vous souhaitons bonne chance")