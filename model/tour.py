"""Management of tournament organization."""
from tinydb import TinyDB


class TourModel:
    """Manages the results of the chess tournament."""
    db = TinyDB(f"data/tour.json", indent=4)
    
    def __init__(self):
        self.matchs = []


"""algorithme Suisse"""
"""une fonction qui permet d'ajouter un match dans le tableau"""
