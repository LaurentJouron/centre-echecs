"""Information for participants in chess tournaments."""


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    
    def __init__(self, first_name, last_name, birthday, gender, ranking):
        """Builder of the model player."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} is a {self.gender} born " \
               f"on {self.birthday}, Currently, {self.ranking} in the " \
               f"national ranking.\n " \
               f"Registration is validated have a good luck!\n"
