#!/usr/bin/python3

import inspect

from __game import Game

class MultiGame(Game):
    class Sequence():
        def __init__(self, game, level):
            self.valid = [3, 1, 0]
            game.init(self)

    class MultiTap():
        def __init__(self, game, level):
            self.valid = 9
            game.init(self)

    class QuickMaff():
        def __init__(self, game, level):
            self.valid = 5 * 5
            game.init(self)

    def __init__(self, players, lives=5, **kwargs):
        def init_state(players, lives):
            self.state['players'] = {}
            for player in players:
                self.state['players'][player] = {'lives' : lives}

        super().__init__(players, **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('action', self.action)
        init_state(self.players, lives)

    def init(self, game):
        self.state['timer'] = 20 # for now
        self.state['valid'] = game.valid
        self.state['name'] = game.__class__.__name__
        if self.display_game is not None:
            self.display_game.update(self.deepcopy)
        self.display()

    def run_game(self):
        level = 1
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
                    self.socketio.emit('timerExpired', self.state, broadcast=True)
                    self.socketio.sleep(1)
                    self.display()
                    if level == 10:
                        self.end_game()
                    del self.state['name']
                    del self.state['valid']
            level += 1

    def display(self):
        print(self.state)

    def action(self, data):
        if data['valid'] != self.state['vaild']:
            self.state['player'][data['player']]['lives'] -= 1


if __name__ == '__main__':
    game = MultiGame(['A', 'B', 'C'])
    game.display()

