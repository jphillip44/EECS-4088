from __game import Game
from collections import OrderedDict
from random import randint
from itertools import cycle

class Hot_Potato(Game):
    __potato_timer = 0
    __next = None
    
    def __init__(self, players):
        super().__init__(players)
        self.__new_potato_timer()
        self.__set_state(self._Game__players)

    def action(self, data):
        self.__hold(data['player'], data['time'])
        return True

    def end_round(self):
        return self.__state['next']

    def display(self):
        print("timer: " + str(self.__state['timer']), end = ", ")
        print("next: " + self.__state['next'], end=', ')
        print(*self.__state['players'].items())

    def run_game(self, socketio):
        emit('state', self.get_state())

    def __set_state(self, players):
        self.__state = {}
        self.__state['timer'] = self.__potato_timer
        self.__state['players'] = OrderedDict()
        for player in players:
            self.__state['players'][player] = {'score': 0}
        self.__state['next'] = self.__get_turn()

    def __hold(self, player, time):
        if time < self.__potato_timer:
            self.__state['players'][player]['score'] += time
            self.__potato_timer -= time
        else:
            self.__state['players'][player]['score'] = 0
            self.__new_potato_timer()
        self.__state['timer'] = self.__potato_timer
        self.__state['next'] = self.__get_turn()

    def __get_turn(self):
        if self.__next is None:
            self.__next = cycle(self.__state['players'].keys())
        return next(self.__next)

    def __new_potato_timer(self):
        self.__potato_timer = randint(10, 20)

if __name__ == '__main__':
    game = Hot_Potato(['A', 'B', 'C'])
    game.display()
    game.action({'player': game.end_round(), 'time': 5})
    game.display()
    game.action({'player': game.end_round(), 'time': 9})
    game.display()
    game.action({'player': game.end_round(), 'time': 1})
    game.display()
    game.action({'player': game.end_round(), 'time': 6})
    game.display()
    game.action({'player': game.end_round(), 'time': 3})
    game.display()
    game.action({'player': game.end_round(), 'time': 8})
    game.display()
    game.action({'player': game.end_round(), 'time': 2})
    game.display()
    game.action({'player': game.end_round(), 'time': 9})
    game.display()
    game.action({'player': game.end_round(), 'time': 3})
    game.display()
    if game.timed_event():
        print("foo")
    game = Hot_Potato(map(chr, range(ord('a'),ord('z')+1)))
    game.display()


