from __game import Game, emit
from collections import OrderedDict
from random import shuffle
from itertools import cycle

class Match(Game):
    __state = {}
    __next = None
    __p1 = None
    __p2 = None

    def __init__(self, players, pairs=20, **kwargs):
        super().__init__(players, **kwargs)
        if self.__dict__.get('socketio'):
            self.socketio.on_event('player1', self.set_p1)
            self.socketio.on_event('player2', self.set_p2)
        self.__set_state(super().get_players(), pairs)

    def __set_state(self, players, pairs):
        self.__state['players'] = OrderedDict()
        for player in players:
            self.__state['players'][player] = {'score': 0}
        self.__state['next'] = (self.__get_turn(), self.__get_turn())
        self.__state['board'] = [format(x, '02d') for x in range(pairs) for _ in range(2)]
        self.__state['gameBoard'] = ['XX' for x in range(pairs*2)]
        shuffle(self.__state['board'])

    def display(self):
        print("Board")
        for i in range(4):
            print(self.__state['board'][i*10:i*10+10])
        print("Game Board")
        for i in range(4):
            print(self.__state['gameBoard'][i*10:i*10+10])
        print('next: ' + str(self.__state['next']))

    def set_p1(self, data):
        self.__p1 = data
        if self.__p2:
            self.is_match()           

    def set_p2(self, data):
        self.__p2 = data
        if self.__p1:
            self.is_match()

    def is_match(self):
        print(self.__state['board'][self.__p1])
        print(self.__state['board'][self.__p2])
        if self.__state['board'][self.__p1] == self.__state['board'][self.__p2]:
            self.__state['gameBoard'][self.__p1] = self.__state['board'][self.__p1]
            self.__state['gameBoard'][self.__p2] = self.__state['board'][self.__p2]
            self.__state['players'][self.__state['next'][0]]['score'] +=1
            self.__state['players'][self.__state['next'][1]]['score'] +=1
        self.__p1 = None
        self.__p2 = None
        self.__state['next'] = (self.__get_turn(), self.__get_turn())
        self.display()
        if self.__dict__.get('display_game'):
            self.display_game.update(self)
    
    def run_game():
        pass

    # def end_round():
    #     emit('state', self.__state)
    
    # def run_game():
    #     emit('state', self.__state)

    def __get_turn(self):
        if self.__next is None:
            self.__next = cycle(self.__state['players'].keys())
        return next(self.__next)

if __name__ == '__main__':
    game = Match(['A', 'B', 'C'])
    game.display()
    game.set_p1(4)
    game.set_p2(5)