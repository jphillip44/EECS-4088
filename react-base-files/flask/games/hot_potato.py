#!/usr/bin/python3
import random
import itertools
import copy

from __game import Game

class Hot_Potato(Game):
    __next = None
    __hold_potato = False

    def __init__(self, players, **kwargs):
        super().__init__(players, {'score': 0},  **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('endOfTurn', self.action)
        self.state['timer'] = self.__new_potato_timer()
        self.state['next'] = self.__get_turn()

    def action(self, data):
        self.__hold_potato = False
        if self.active:
            print(data)
            self.__hold(data['player'], data.get('time'))
            if self.state['players'][data['player']]['score'] > 20:
                self.end_game()
                self.rank_players()
            self.display()
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)

    def display(self):
        if self.active:
            print("timer: " + str(self.state['timer']), end = ", ")
            print("penalty: " + str(self.state['penalty']), end=", ")
            print("next: " + self.state['next'], end=', ')
            print(*self.state['players'].items())
        else:
            print(*self.state['players'].items())
            self.print_standings()

    def run_game(self):
        self.display_game.update(self.deepcopy)
        while self.active:
            self.socketio.emit('state', self.state, broadcast=True)
            self.__hold_potato = True
            while self.__hold_potato:
                if self.state['timer'] >= 0:
                    self.socketio.sleep(1)
                    print(self.state['timer'])
                    self.state['timer'] -= 1
                else:
                    self.socketio.emit('explode', room=self.state['next'])
                    self.__hold_potato = False
                    self.socketio.sleep(1)
        else:
            print("Game Over")
            self.socketio.emit('gameOver', broadcast=True)

    def __hold(self, player, time):
        self.state['next'] = self.__get_turn()
        if time is not None:
            self.state['players'][player]['score'] += time
        else:
            self.state['players'][player]['score'] -= min(self.state['players'][player]['score'], self.state['penalty'])
            self.state['timer'] = self.__new_potato_timer()

    def __get_turn(self):
        if self.__next is None:
            self.__next = itertools.cycle(self.state['players'].keys())
        return next(self.__next)

    def __new_potato_timer(self):
        self.state['penalty'] = random.randint(1, 20)
        return self.state['penalty']

if __name__ == '__main__':
    game = Hot_Potato(['A', 'B', 'C'])
    game.display()
    game.action({'player': game.state['next'], 'time': 5})
    game.action({'player': game.state['next'], 'time': 9})
    game.action({'player': game.state['next'], 'time': 1})
    game.action({'player': game.state['next'], 'time': 6})
    game.action({'player': game.state['next'], 'time': 3})
    game.action({'player': game.state['next'], 'time': 8})
    game.action({'player': game.state['next'], 'time': 2})
    game.action({'player': game.state['next'], 'time': 9})
    game.action({'player': game.state['next'], 'time': 3})
    game = Hot_Potato(map(chr, range(ord('a'),ord('z')+1)))
    game.display()


