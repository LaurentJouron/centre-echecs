"""Information for participants in chess tournaments."""
from tinydb import TinyDB, where, table
import string


class PlayerModel:
    """Class attribut for players file"""
    db = TinyDB(f"data/players.json", indent=4)
    players = db.table('players')
    
    """Builder of the model player."""
    def __init__(self, first_name: str, last_name: str, birthday: str ="",
                 gender: str ="", ranking: int =""):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking

    def __repr__(self):
        """Displays all items in the players file"""
        return f"\nFirst-name: {self.first_name}\n" \
               f"Last-name: {self.last_name}\n" \
               f"Born: {self.birthday}\n" \
               f"Gender: {self.gender}\n" \
               f"Ranking: {self.ranking}\n"
    
    def __str__(self):
        """Display confirmation when the player is register in players file"""
        return f"\n{self.full_name} is register"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return PlayerModel.players.get((where('first_name') == self.first_name)
                                    & (where('last_name') == self.last_name))

    def save(self, validate_data: bool = False) -> int:
        """Saves items in the TinyDB file"""
        if validate_data:
            self._checks()
        if self.exists():
            return -1
        return PlayerModel.players.insert(self.__dict__)

    def _checks(self):
        self._check_names()

    def _check_names(self):
        if not (self.first_name and self.first_name):
            raise ValueError("First and last name cannot be blank.")
        special_characters = string.punctuation + string.digits
        for character in self.first_name + self.last_name + self.gender:
            if character in special_characters:
                raise ValueError(f"Value error {self.full_name}.")

    def exists(self):
        return bool(self.db_instance)
    
    @staticmethod
    def remove(self) -> list[int]:
        """Removes an item from the list"""
        if self.exists():
            return PlayerModel.players.remove(doc_ids=[self.db_instance.doc_id])
        return []

    @staticmethod
    def get_all():
        """Returns all TinyDB file elements."""
        return [PlayerModel(**player) for player in PlayerModel.players.all()]
        
    @staticmethod
    def get_one_player(first_name):
        """Return just one item from the list"""
        return PlayerModel.players.get(where('first-name') == first_name)
