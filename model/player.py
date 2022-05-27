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
        return f"\n{self.first_name}\n" \
               f"{self.last_name}\n" \
               f"{self.birthday}\n" \
               f"{self.gender}\n" \
               f"{self.ranking}\n"
    
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
        """Checks if the player’s characters are correct and completed"""
        if not (self.first_name and self.first_name):
            raise ValueError("First and last name cannot be blank.")
        special_characters = string.punctuation + string.digits
        for character in self.first_name + self.last_name + self.gender:
            if character in special_characters:
                raise ValueError(f"Value error {self.full_name}.")

    def exists(self):
        """Check if the player is already registered"""
        return bool(self.db_instance)

    def remove(self) -> list[int]:
        """Removes an item from the list"""
        if self.exists():
            return PlayerModel.players.remove(doc_ids=[self.db_instance.doc_id])
        return []

    @staticmethod
    def get_all():
        """
        Returns all Players file elements with unpacking in
        comprehension list.
        """
        return [PlayerModel(**player) for player in PlayerModel.players.all()]

    @staticmethod
    def get_one_player(first_name, last_name):
        """Return all information of player by name"""
        return PlayerModel.players.get((where('first_name') == first_name)
                                       & (where('last_name') == last_name))

    def alphabetical_order(self):
        sorted(self.get_all, key=lambda PlayerModel: PlayerModel.last_name)

    def ranking_order(self):
        sorted(self.get_all, key=lambda PlayerModel: PlayerModel.ranking)