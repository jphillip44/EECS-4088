from games import *
from singleton import Singleton

class GameList(Singleton):
    
    def select_game(type):
        return eval(type)

    def list_games(self):
        return [game.__name__ for game in Game.__subclasses__()]

        
