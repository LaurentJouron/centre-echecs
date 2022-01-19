

class PlayerModel:

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name


    def display(self):
        print(f"La liste de joueur dans ce tournoi est {self.first_name} {self.name}.")
        for name in self:
            print(f"  -  {name}")
