"""Information for participants in chess tournaments."""
from tinydb import TinyDB, where


class PlayerModel:
    db = TinyDB(f"data/players.json", indent=4)
    
    """Builder of the model player."""
    def __init__(self, first_name, last_name, birthday, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
    
    def __str__(self):
        return f"\n{self.first_name} {self.last_name} is a {self.gender} " \
               f"born " \
               f"on {self.birthday}, Currently, {self.ranking} in the " \
               f"national ranking.\n" \
               f"Registration is validated have a good luck!\n"
    
    def save(self):
        PlayerModel.db.insert({"first-name": self.first_name,
                               "last-name": self.last_name,
                               "birthday": self.birthday,
                               "gender": self.gender,
                               "ranking": self.ranking})
    
    @staticmethod
    def get_all():
        return PlayerModel.db.all()
    
    def modify(self):
        pass

    @staticmethod
    def remove():
        player = PlayerModel.db.all()
        player = player.doc_id
        return PlayerModel.db.remove(doc_id=player)


        # PlayerModel.db.remove(where("ID:") == self.ident)
