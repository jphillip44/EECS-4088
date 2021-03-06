#!/usr/bin/python3
import itertools
import numpy

from __game import Game

class Match(Game):
    def __init__(self, players, rows=3, columns=6, shuffle=True, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        def init_state(players, rows, columns, shuffle):
            self.__next = itertools.cycle(list(self.state['players'].keys()))
            self.state['next'] = (next(self.__next), next(self.__next))
            board = [format(x, '02d') for x in range(rows*columns//2) for _ in range(2)]
            if shuffle:
                numpy.random.shuffle(board)
            self.rows = rows
            self.columns = columns
            self.state['board'] = numpy.array(board).reshape(rows, columns)
            self.state['gameBoard'] = numpy.full((rows, columns), 'XX')
            self.state['cursor'] = [0,0]
            self.state['timer'] = 30
            self.__p1 = None
            self.__p2 = None
            self.__waiting = True

        super().__init__(players, {'score': 0},  **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('select', self.action)
            self.socketio.on_event('up', self.up)
            self.socketio.on_event('down', self.down)
            self.socketio.on_event('left', self.left)
            self.socketio.on_event('right', self.right)
        init_state(self.players, rows, columns, shuffle)

    def display(self):
        '''
        Displays the game state to the console.
        '''
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
        '''
        Function that runs the gameloop from the server.
        '''
        timer = self.state['timer']
        while self.active:
            self.display_game.update(self.deepcopy)
            self.state['board'] = self.state['board'].tolist()
            self.state['gameBoard'] = self.state['gameBoard'].tolist()
            self.socketio.emit('turn', self.state, broadcast=True)
            self.state['board'] = numpy.array(self.state['board'])
            self.state['gameBoard'] = numpy.array(self.state['gameBoard'])
            while self.__waiting and self.state['timer'] > 0:
                self.socketio.sleep(1)
                self.state['timer'] -= 1
                print(self.state['timer'])
                self.display_game.update(self.deepcopy)
            else:
                if self.state['timer'] == 0:
                    self.socketio.emit('timeout', room=self.state['next'][0])
                    self.state['next'] = (self.state['next'][1], next(self.__next))
                self.__waiting = True
                self.state['timer'] = timer
            super().run_game()


    def action(self, data=None):
        '''
        Handles input logic for card selection.
        '''
        def is_match():
            '''
            Handles logic for matching cards.
            '''
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
            data = tuple(self.state['cursor'])
            
        print("value: " + self.state['board'][data])
        self.__waiting = False
        if self.__p1 is None:
            self.__p1 = self.state['next'][0], data
            self.state['gameBoard'][self.__p1[1]] = 'ZZ'
        else:
            self.__p2 = self.state['next'][0], data
            self.state['gameBoard'][self.__p1[1]] = 'XX'    
            is_match()
        self.state['next'] = (self.state['next'][1], next(self.__next))
        self.display() 
        if self.socketio is not None:
            self.socketio.sleep(5)


    def check_end(self):
        '''
        checks if the game is over.
        '''
        if list(self.state['gameBoard'].flatten()).count('XX') == 0:
            self.end_game()

    def left(self):
        '''
        Handles logic for left on the controller including wraparound.
        '''
        if self.state['cursor'][1] > 0:
            self.state['cursor'][1] -= 1
        else:
            self.state['cursor'][1] = self.columns - 1
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        print(self.state['cursor'])

    def right(self):
        '''
        Handles logic for right on the controller including wraparound.
        '''
        if self.state['cursor'][1] < self.columns - 1:
            self.state['cursor'][1] += 1
        else:
            self.state['cursor'][1] = 0
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        print(self.state['cursor'])

    def up(self):
        '''
        Handles logic for up on the controller including wraparound.
        '''
        if self.state['cursor'][0] > 0:
            self.state['cursor'][0] -= 1
        else:
            self.state['cursor'][0] = self.rows - 1
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        print(self.state['cursor'])

    def down(self):
        '''
        Handles logic for down on the controller including wraparound.
        '''
        if self.state['cursor'][0] < self.rows - 1:
            self.state['cursor'][0] += 1
        else:
            self.state['cursor'][0] = 0
        if self.socketio is not None:
            self.socketio.emit('cursor', self.state['cursor'], room=self.state['next'][0])
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        print(self.state['cursor'])

    def __get_turn(self):
        '''
        Gets the next players turn.
        '''
        return next(self.__next)

if __name__ == '__main__':
    game = Match(['A', 'B', 'C'])
    game.display()
    game.action()
    game.down()
    game.up()
    game.action()
    # game = Match(['A', 'B', 'C'], shuffle=False)
    # game.display()
    # [game.action((i, j)) for i in range(4) for j in range(10)]
