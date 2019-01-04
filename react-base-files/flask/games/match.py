from __game import Game, emit
from collections import OrderedDict
from random import shuffle
from itertools import cycle

class Match(Game):
    __next = None
    __p1 = None
    __p2 = None

    def __init__(self, players, pairs=20, **kwargs):
        super().__init__(players, **kwargs)
        if self.__dict__.get('socketio'):
            self.socketio.on_event('player1_return', self.set_p1)
            self.socketio.on_event('player2_return', self.set_p2)
        self.__set_state(super().get_players(), pairs)

    def __set_state(self, players, pairs):
        self.state['players'] = OrderedDict()
        for player in players:
            self.state['players'][player] = {'score': 0}
        self.state['next'] = (self.__get_turn(), self.__get_turn())
        self.state['board'] = [format(x, '02d') for x in range(pairs) for _ in range(2)]
        self.state['gameBoard'] = ['XX' for x in range(pairs*2)]
        shuffle(self.state['board'])

    def display(self):
        print("Board")
        for i in range(4):
            print(self.state['board'][i*10:i*10+10])
        print("Game Board")
        for i in range(4):
            print(self.state['gameBoard'][i*10:i*10+10])
        print('next: ' + str(self.state['next']))

    def set_p1(self, data):
        self.__p1 = data
        print(self.state['board'][self.__p1])
        if self.__dict__.get('socketio'):
            self.socketio.emit('player1_move', data)        

    def set_p2(self, data):
        self.__p2 = data
        print(self.state['board'][self.__p2])
        if self.__dict__.get('socketio'):
            self.socketio.emit('player2_move', data)        
        self.is_match()

    def is_match(self):
        if self.state['board'][self.__p1] == self.state['board'][self.__p2]:
            self.state['gameBoard'][self.__p1] = self.state['board'][self.__p1]
            self.state['gameBoard'][self.__p2] = self.state['board'][self.__p2]
            self.state['players'][self.state['next'][0]]['score'] +=1
            self.state['players'][self.state['next'][1]]['score'] +=1
        self.__p1 = None
        self.__p2 = None
        self.state['next'] = (self.__get_turn(), self.__get_turn())
        self.display()
        if self.__dict__.get('display_game'):
            self.display_game.update(self)
    
    def run_game():
        pass

    def __get_turn(self):
        if self.__next is None:
            self.__next = cycle(self.state['players'].keys())
        return next(self.__next)

if __name__ == '__main__':
    game = Match(['A'])
    game.display()
    game = Match(['A', 'B', 'C'])
    game.display()
    game.set_p1(4)
    game.set_p2(5)