"""Information for participants in chess tournaments."""


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    
    def __init__(self, first_name, last_name, birthday, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
    
    def get_full_name(self):
        """Get the information of a participant."""
        return self.first_name + " " + \
            self.last_name + " " +\
            self.gender + " " +\
            self.birthday + " " +\
            self.ranking
