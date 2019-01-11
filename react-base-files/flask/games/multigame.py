#!/usr/bin/python3

import inspect
import operator
import numpy as np

from __game import Game

class MultiGame(Game):
    class Simon():
        def __init__(self, game, level):
            choices = ['red', 'blue', 'green', 'yellow']
            self.valid = list(np.random.choice(choices, level + 4))
            self.timer = 20
            game.init(self)

    class MultiTap():
        def __init__(self, game, level):
            self.valid = np.random.randint(level + 2, 2*level + 4)
            self.timer = 20
            game.init(self)

    class QuickMaff():
        def __init__(self, game, level):
            ops = {
                '+': operator.add, 
                '*': operator.mul,
            }
            val1 = np.random.randint(1, 10)
            val2 = np.random.randint(1, 10)
            op = list(ops.keys())[level % 2]
            self.valid = ops.get(op)(val1, val2)
            self.timer = 20 - level
            print("{} {} {} = ?".format(val1, op, val2))
            game.init(self)

    def __init__(self, players, lives=5, **kwargs):
        super().__init__(players, {'hp' : lives}, **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('action', self.action)

    def init(self, game):
        self.state['timer'] = game.timer
        self.state['valid'] = game.valid
        self.state['name'] = game.__class__.__name__
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        self.display()

    def run_game(self):
        level = 0
        timer = self.state['timer']
        while self.active:
            for d in dir(MultiGame):
                self.display_game.update(self.deepcopy)
                self.socketio.emit('state', self.state, broadcast=True)
                if inspect.isclass(getattr(MultiGame, d)) and d !='__class__':
                    getattr(self, d)(self, level)
                    while self.state['timer'] > 0:
                        self.socketio.sleep(1)
                        print(self.state['timer'])
                        self.state['timer'] -= 1
                    self.state['timer'] = timer
                    self.socketio.emit('timerExpired', self.state, broadcast=True)
                    self.socketio.sleep(1)
                    self.display()
                    self.rank_players()
                    del self.state['name']
                    del self.state['valid']
            level += 1

    def rank_players(self):
        def check_dead():
            for player, stats in self.state['players'].items():
                if stats['hp'] != 'dead' and stats['hp'] <= 0:
                    stats['hp'] = 'dead'
                    self.add_ranks(player)

        def check_alive():
            for player, stats in self.state['players'].items():
                if stats['hp'] != 'dead':
                    yield player

        check_dead()
        alive = list(check_alive())
        if len(alive) < 2:
            for player in alive:
                self.add_ranks(player)
            self.end_game()
            

    def display(self):
        print(self.state)

    def action(self, data):
        if data['valid'] != self.state['vaild']:
            self.state['player'][data['player']]['lives'] -= 1


if __name__ == '__main__':
    game = MultiGame(['A', 'B', 'C'])
    game.display()
    level = 0
    while level < 4:
        game.MultiTap(game, level)
        game.QuickMaff(game, level)
        game.Simon(game, level)
        level += 1
        game.rank_players()

