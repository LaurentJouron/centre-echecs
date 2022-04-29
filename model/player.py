"""Information for participants in chess tournaments."""
from tinydb import TinyDB, where
from dataclasses import dataclass


@dataclass
class PlayerModel:
    db = TinyDB(f"data/players.json", indent=4)
    players = db.table('players')
    
    """Builder of the model player."""
    first_name: str
    last_name: str
    birthday: float
    gender: str
    ranking: int
        
    def __str__(self):
        """Displays all items in the TinyDB file"""
        return f"\nFirst-name: {self.first_name}\n" \
               f"Last-name: {self.last_name}\n" \
               f"Born: {self.birthday}\n" \
               f"Gender: {self.gender}\n" \
               f"Ranking: {self.ranking}"
    
    def __repr__(self):
        return f"Player({self.first_name}, {self.last_name})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self):
        """Saves items in the TinyDB file"""
        PlayerModel.players.insert({"first-name": self.first_name,
                                    "last-name": self.last_name,
                                    "birthday": self.birthday,
                                    "gender": self.gender,
                                    "ranking": self.ranking})
    
    @staticmethod
    def get_all():
        """Returns all TinyDB file elements."""
        return PlayerModel.players.all()

    @staticmethod
    def remove(first_name):
        """Removes an item from the list"""
        PlayerModel.players.remove(where('first-name') == first_name)
        
    @staticmethod
    def get_one_player(first_name):
        """Return just one item from the list"""
        return PlayerModel.players.get(where('first-name') == first_name)
