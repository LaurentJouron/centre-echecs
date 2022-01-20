"""Information for participants in chess tournaments."""


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    def __init__(self, name, firstname, birthday, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    def get_name(self):
        """Get the name of a participant."""
        return self.name

    def get_firstname(self):
        """Get the firstname of a participant."""
        return self.firstname

    def get_birthday(self):
        """Get the birthday of a participant."""
        return self.birthday

    def get_gender(self):
        """Get the gender of a participant."""
        return self.gender

    def get_ranking(self):
        """Get the classement of a participant."""
        return self.ranking
