from __game import Game, emit
from collections import OrderedDict
from random import shuffle
from itertools import cycle

class Match(Game):
    __state = {}
    __next = None

    def __init__(self, players, pairs=20):
        super().__init__(players)
        self.__set_state(super().get_players(), pairs)

    def __set_state(self, players, pairs):
        self.__state['players'] = OrderedDict()
        for player in players:
            self.__state['players'][player] = {'score': 0}
        self.__state['next'] = (self.__get_turn(), self.__get_turn())
        self.__state['board'] = [format(x, '02d') for x in range(pairs) for _ in range(2)]
        shuffle(self.__state['board'])

    def display(self):
        print('next: ' + str(self.__state['next']))
        for i in range(4):
            print(self.__state['board'][i*10:i*10+10])

    def action():
        pass

    def end_round():
        emit('state', self.__state)
    
    def run_game():
        emit('state', self.__state)

    def __get_turn(self):
        if self.__next is None:
            self.__next = cycle(self.__state['players'].keys())
        return next(self.__next)

if __name__ == '__main__':
    game = Match(['A', 'B', 'C'])
    game.display()