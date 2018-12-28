from games import *
from singleton import Singleton
import sys

class GameList(Singleton):

    def select_game(type, users):
        return getattr(sys.modules[__name__], type)(users)

    def list_games(self):
        return [game.__name__ for game in Game.__subclasses__()]

if __name__ == '__main__':
    game = GameList.select_game("Double07", {"A", "B"})
    game.display()

        
