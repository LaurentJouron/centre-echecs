"""Information for participants in chess tournaments."""


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    
    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
    
    def get_full_name(self):
        """Get the information of a participant."""
        return self.first_name + " " + self.last_name + " " +\
            self.gender + " " + self.date_of_birth + " " + self.ranking
