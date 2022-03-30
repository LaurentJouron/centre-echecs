"""Information for participants in chess tournaments."""
from tinydb import TinyDB, where


class PlayerModel:
    db = TinyDB(f"data/players.json", indent=4)
    
    """Builder of the model player."""
    def __init__(self, first_name, last_name, birthday, gender, ranking):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.birthday = birthday
        self.gender: str = gender
        self.ranking: int = ranking

    def __str__(self):
        """Displays all items in the TinyDB file"""
        return f"\n{self.first_name} {self.last_name}\n" \
               f"Born: {self.birthday}\n" \
               f"Gender: {self.gender}\n" \
               f"Ranking: {self.ranking}"
    
    def save(self):
        """Saves items in the TinyDB file"""
        PlayerModel.db.insert({"first-name": self.first_name,
                               "last-name": self.last_name,
                               "birthday": self.birthday,
                               "gender": self.gender,
                               "ranking": self.ranking})
    
    @staticmethod
    def get_all():
        """Returns all TinyDB file elements."""
        return PlayerModel.db.all()
    
    def modify(self):
        pass

    @staticmethod
    def remove(first_name):
        """Removes an item from the list"""
        PlayerModel.db.remove(where('first-name') == first_name)
