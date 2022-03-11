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
        """Get the information of a participant."""
        return f"{self.first_name} {self.last_name} est {self.gender}, " \
               f"né le {self.birthday}.\n" \
               f"Actuellement, {self.ranking} au classement national.\n" \
               f"Son inscription est validée.\n" \
               f"Bonne chance!"
