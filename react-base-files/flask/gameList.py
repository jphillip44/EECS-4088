from games import *
import os

class GameList():

    def select_game(type):
        return eval(type)

    def list_games(self):
        games_list = []
        for file in os.listdir('games'):
            if file != 'game.py' and file[0] != '_':
                games_list.append(file.split('.')[0])
        return games_list
        
