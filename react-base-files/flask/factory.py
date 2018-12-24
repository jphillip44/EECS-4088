from games import *

class Factory(Game):

    def set_game(self, type):
        if type == "Game1": return Game1()
        if type == "Game2": return Game2()

    def foo(self):
        pass