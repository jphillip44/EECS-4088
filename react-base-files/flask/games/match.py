#!/usr/bin/python3
import itertools
import random
import numpy

from collections import OrderedDict
from __game import Game


class Match(Game):
    __next = None
    __p1 = None
    __p2 = None
    __waiting = True

    def __init__(self, players, rows=4, columns=10, shuffle=True, **kwargs):
        def init_state(players, rows, columns, shuffle):
            self.state['players'] = OrderedDict()
            for player in players:
                self.state['players'][player] = {'score': 0}
            self.state['next'] = (self.__get_turn(), self.__get_turn())
            board = [format(x, '02d') for x in range(rows*columns//2) for _ in range(2)]
            if shuffle:
                random.shuffle(board)
            self.rows = rows
            self.columns = columns
            self.state['board'] = numpy.asarray([board[i*columns:i*columns+columns] for i in range(rows)])
            self.state['gameBoard'] = numpy.asarray([['XX'] * columns for _ in range(rows)])
            self.state['cursor'] = (0,0)
            self.state['timer'] = 15

        super().__init__(players, **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('select', self.action)
            self.socketio.on_event('up', self.up)
            self.socketio.on_event('down', self.down)
            self.socketio.on_event('left', self.left)
            self.socketio.on_event('right', self.right)
        init_state(self.players, rows, columns, shuffle)

    def display(self):
        if self.active:
            print("Board")
            print(*self.state['board'], sep='\n')
            print("Game Board")
            print(*self.state['gameBoard'], sep='\n')
            print('next: ' + str(self.state['next']))
            print('cursor: ' + str(self.state['cursor']))
            print(self.state['players'])
        else:
            print(self.state['players'])
            self.print_standings()

    def run_game(self):
        while self.active:
            self.state['board'] = self.state['board'].tolist()
            self.state['gameBoard'] = self.state['gameBoard'].tolist()
            self.socketio.emit('turn', self.state, broadcast=True)
            self.state['board'] = numpy.asarray(self.state['board'])
            self.state['gameBoard'] = numpy.asarray(self.state['gameBoard'])
            while self.__waiting and self.state['timer'] > 0:
                self.socketio.sleep(1)
                print(self.state['timer'])
                self.state['timer'] -= 1
                self.socketio.emit('timeout', room=self.state['next'][0])
                self.state['next'] = (self.state['next'][1], self.__get_turn())
            else:
                self.__waiting = True
                self.state['timer'] = 15
                self.display_game.update(self.deepcopy)



    def action(self, data=None):
        def is_match():
            if self.socketio is not None:
                self.socketio.emit('flip', broadcast=True)
            if self.state['board'][self.__p1[1]] == self.state['board'][self.__p2[1]]:
                self.state['gameBoard'][self.__p1[1]] = self.state['board'][self.__p1[1]]
                self.state['gameBoard'][self.__p2[1]] = self.state['board'][self.__p2[1]]
                self.state['players'][self.__p1[0]]['score'] +=1
                self.state['players'][self.__p2[0]]['score'] +=1
            self.__p1 = None
            self.__p2 = None
            if self.display_game is not None:
                self.display_game.update(self.deepcopy)
            self.check_end()

        if data is None:
            data = self.state['cursor']
            
    
        print("value: " + self.state['board'][data])
        self.__waiting = False
        if self.__p1 is None:
            self.__p1 = self.state['next'][0], data
            self.state['gameBoard'][self.__p1[1]] = 'ZZ'
        else:
            self.__p2 = self.state['next'][0], data
            self.state['gameBoard'][self.__p1[1]] = 'XX'    
            is_match()
        self.state['next'] = (self.state['next'][1], self.__get_turn())
        self.display() 


    def check_end(self):
        if list(self.state['gameBoard'].flatten()).count('XX') == 0:
            self.end_game()
            self.rank_players()

    def left(self):
        if self.state['cursor'][1] > 0:
            self.state['cursor'] = (self.state['cursor'][0], self.state['cursor'][1] - 1)
        else:
            self.state['cursor'] = (self.state['cursor'][0], self.columns - 1)
        # if self.state['gameBoard'][self.state['cursor']] == 'ZZ':
        #     self.left()
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])

    def right(self):
        if self.state['cursor'][1] < self.columns - 1:
            self.state['cursor'] = (self.state['cursor'][0], self.state['cursor'][1] + 1)
        else:
            self.state['cursor'] = (self.state['cursor'][0], 0)
        # if self.state['gameBoard'][self.state['cursor']] == 'ZZ':
        #     self.right()
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])

    def up(self):
        if self.state['cursor'][0] > 0:
            self.state['cursor'] = (self.state['cursor'][0] - 1, self.state['cursor'][1])
        else:
            self.state['cursor'] = (self.rows - 1, self.state['cursor'][1])
        # if self.state['gameBoard'][self.state['cursor']] == 'ZZ':
        #     self.up()
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])

    def down(self):
        if self.state['cursor'][0] < self.rows - 1:
            self.state['cursor'] = (self.state['cursor'][0] + 1, self.state['cursor'][1])
        else:
            self.state['cursor'] = (0, self.state['cursor'][1])
        # if self.state['gameBoard'][self.state['cursor']] == 'ZZ':
        #     self.down()
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])       

    # def selected(self, data):
    #     return self.state['cursor'] != 'XX'

    def __get_turn(self):
        if self.__next is None:
            self.__next = itertools.cycle(self.state['players'].keys())
        return next(self.__next)

if __name__ == '__main__':
    game = Match(['A', 'B', 'C'])
    game.display()
    game.action()
    game.down()
    game.up()
    game.action()
    game = Match(['A', 'B', 'C'], shuffle=False)
    game.display()
    [game.action((i, j)) for i in range(4) for j in range(10)]
