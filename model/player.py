"""Information for participants in chess tournaments."""
from tinydb import TinyDB
# from tinydb.storages import MemoryStorage


class PlayerModel:
    """Entering information of the différent players of the tournament."""
    
    def __init__(self, first_name, last_name, date_of_birth, gender,
                 ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
    
    def get_full_name(self):
        """Get the information of a participant."""
        return self.first_name + " " + \
               self.last_name + " " + \
               self.gender + " " + \
               self.date_of_birth + " " + \
               self.ranking
    
    def create_data_base_in_file(self):
        data_base = TinyDB('data.player.json', indent=4)
        data_base.insert({"Prénom": PlayerModel.get_full_name(
            self.first_name),
            "Nom": PlayerModel.get_full_name(self.last_name),
            "Date de naissance": PlayerModel.get_full_name(
                self.date_of_birth),
            "Genre": PlayerModel.get_full_name(self.gender),
            "Classement": PlayerModel.get_full_name(
                self.ranking)})
    
    # def create_data_base_in_memory(self):
    #     data_base = TinyDB(storage=MemoryStorage)
    #     data_base.insert({"Prénom": PlayerModel.get_full_name(
    #         self.first_name),
    #                       "Nom": PlayerModel.get_full_name(self.last_name),
    #                       "Date de naissance": PlayerModel.get_full_name(
    #                           self.date_of_birth),
    #                       "Genre": PlayerModel.get_full_name(self.gender),
    #                       "Classement": PlayerModel.get_full_name(
    #                           self.ranking)})
