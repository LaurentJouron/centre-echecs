"""Information for participants in chess tournaments."""


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    def __init__(self, last_name, first_name, birthday, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    def get_full_name(self):
        """Get the information of a participant."""
        return self.first_name + " " + self.last_name + " " + self.gender + " " + self.birthday

    def get_ranking(self):
        """Get the classement of a participant."""
        return self.ranking

