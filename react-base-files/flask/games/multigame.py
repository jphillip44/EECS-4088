#!/usr/bin/python3

import inspect
import operator
import numpy as np

from __game import Game, ABC

class MultiGame(Game):
    class SubGame(ABC):
        def __init__(self, game):
            game.state['timer'] = self.timer
            game.state['valid'] = self.valid
            game.state['name'] = self.__class__.__name__
            # if game.display_game is not None:
            #     game.display_game.update(game.deepcopy)
            game.display()

    class Simon(SubGame):
        def __init__(self, game, level):
            choices = ['Red', 'Blue', 'Green', 'Yellow']
            self.valid = list(np.random.choice(choices, level + 4))
            self.timer = 20
            super().__init__(game)

    class MultiTap(SubGame):
        def __init__(self, game, level):
            self.valid = np.random.randint(level + 2, 2*level + 4)
            self.timer = 20
            super().__init__(game)

    class QuickMaff(SubGame):
        def __init__(self, game, level):
            ops = {
                '+': operator.add, 
                '-': operator.sub,
                '*': operator.mul
            }
            val1 = np.random.randint(1, 10)
            val2 = np.random.randint(1, 10)
            op = list(ops.keys())[level % len(ops)]
            self.valid = ops.get(op)(val1, val2)
            self.timer = max(20 - level, 5)
            game.state['formula'] = "{} {} {} = ?".format(val1, op, val2)
            print(game.state['formula'])
            super().__init__(game)


    def __init__(self, players, lives=5, **kwargs):
        super().__init__(players, {'hp' : lives, 'correct': False}, **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('action', self.action)

    def run_game(self):
        level = 0
        # timer = self.state['timer']
        while self.active:
            # for d in dir(MultiGame):
            for game in self.SubGame.__subclasses__():
                if self.active:
                    getattr(self, game.__name__)(self, level)
                    self.display_game.update(self.deepcopy)
                    self.socketio.emit('state', self.state, broadcast=True)
                    while self.state['timer'] > 0:
                        self.display_game.update(self.deepcopy)
                        self.socketio.sleep(1)
                        print(self.state['timer'])
                        self.state['timer'] -= 1
                    # self.state['timer'] = timer
                    self.socketio.emit('timerExpired', self.state, broadcast=True)
                    self.socketio.sleep(1)
                    self.display_game.update(self.deepcopy)
                    self.check_turns()
                    self.display()
                    self.rank_players()
                    self.state.pop('name')
                    self.state.pop('valid')
                    self.state.pop('formula')
                    super().run_game()
            level += 1
        # self.socketio.emit('gameOver', broadcast=True)

    def rank_players(self):
        def check_dead():
            for player, stats in self.state['players'].items():
                if stats['hp'] != 'dead' and stats['hp'] <= 0:
                    stats['hp'] = 'dead'
                    self.remove_player()
                    self.ranks.append(player)

        def check_alive():
            for player, stats in self.state['players'].items():
                if stats['hp'] != 'dead':
                    yield player

        check_dead()
        alive = list(check_alive())
        if len(alive) < 2 and self.active:
            for player in alive:
                self.ranks.append(player)
            self.end_game()
            

    def display(self):
        if self.active:
            print(self.state)
        else:
            self.print_standings()

    def action(self, data):
        print(data)
        if data['valid'] == self.state['valid']:
            # self.state['players'][data['player']]['turn'] = False
            self.state['players'][data['player']]['correct'] = True

    def check_turns(self):
        for player, state in self.state['players'].items():
            if state['hp'] != 'dead' and state['hp'] > 0:
                if state['correct']:
                    state['correct'] = False
                else:
                    state['hp'] -= 1
        self.rank_players()


if __name__ == '__main__':
    game = MultiGame(['A', 'B', 'C'])
    game.display()
    level = 0
    while level < 3:
        game.MultiTap(game, level)
        game.action({'player': 'A', 'valid': game.state['valid']})
        game.action({'player': 'B', 'valid': None})
        game.check_turns()
        game.QuickMaff(game, level)
        game.action({'player': 'B', 'valid': game.state['valid']})
        game.action({'player': 'A', 'valid': None})
        game.check_turns()
        game.Simon(game, level)
        game.action({'player': 'A', 'valid': game.state['valid']})
        game.check_turns()
        level += 1
        game.display()

