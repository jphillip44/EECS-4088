import games
import os

class Factory():

    def set_game(self, type):
        if type == "Game1": return games.Game1()
        if type == "Game2": return games.Game2()

    def list_games(self):
        games_list = []
        for file in os.listdir('games'):
            if file != 'game.py' and file[0] != '_':
                games_list.append(file.split('.')[0])
        return games_list
        
