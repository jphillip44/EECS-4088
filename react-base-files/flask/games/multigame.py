#!/usr/bin/python3

import inspect
import operator
import numpy as np

from __game import Game, ABC

class MultiGame(Game):
    class SubGame(ABC):
        '''
        The SubGame object is used to be the parent class of any subgames for multigame.
        It handles common default parameters for all the games.
        '''
        def __init__(self, game):
            game.state['timer'] = self.timer
            game.state['valid'] = self.valid
            game.state['name'] = self.__class__.__name__
            game.display()

    class Simon(SubGame):
        def __init__(self, game, level):
            '''
            Sets up the games default parameters.
            '''
            choices = ['Red', 'Blue', 'Green', 'Yellow']
            self.valid = list(np.random.choice(choices, level + 4))
            self.timer = 20
            super().__init__(game)

    class MultiTap(SubGame):
        def __init__(self, game, level):
            '''
            Sets up the games default parameters.
            '''
            self.valid = np.random.randint(level + 2, 2*level + 4)
            self.timer = 20
            super().__init__(game)

    class QuickMaff(SubGame):
        def __init__(self, game, level):
            '''
            Sets up the games default parameters.
            '''
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
        '''
        Sets up the games default parameters.
        '''
        super().__init__(players, {'hp' : lives, 'correct': False, 'old_correct': None}, **kwargs)
        if self.socketio is not None:
            self.socketio.on_event('action', self.action)

    def run_game(self):
        '''
        Function that runs the gameloop from the server.
        '''
        level = 0
        while self.active:
            for game in self.SubGame.__subclasses__():
                if self.active:
                    getattr(self, game.__name__)(self, level)
                    self.display_game.update(self.deepcopy)
                    self.socketio.emit('state', self.state, broadcast=True)
                    while self.state['timer'] > 0:
                        self.socketio.sleep(1)
                        self.state['timer'] -= 1
                        print(self.state['timer'])
                        self.display_game.update(self.deepcopy)
                    self.socketio.emit('timerExpired', self.state, broadcast=True)
                    self.socketio.sleep(1)
                    self.display_game.update(self.deepcopy)
                    self.check_answers()
                    self.display()
                    self.rank_players()
                    self.state.pop('name')
                    self.state.pop('valid')
                    self.state.pop('formula', None)
                    super().run_game()
            level += 1

    def rank_players(self):
        '''
        Ranks players based on order of death.
        Simultaneous deaths are broken arbitrarily.
        '''
        def check_dead():
            '''
            A local function to __rank_players().
            Adds players to ranking queue if they are dead.
            '''
            for player, stats in self.state['players'].items():
                if stats['hp'] != 'dead' and stats['hp'] <= 0:
                    stats['hp'] = 'dead'
                    self.remove_player()
                    self.ranks.append(player)

        def check_alive():
            '''
            A local function to __rank_players().
            Returns a list of living players.
            '''
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
        '''
        Displays the game state to the console.
        '''
        if self.active:
            print(self.state)
        else:
            self.print_standings()

    def action(self, data):
        '''
        Checks if controller input is valid.
        '''
        print(data)
        if data['valid'] == self.state['valid']:
            self.state['players'][data['player']]['correct'] = True

    def check_answers(self):
        '''
        Checks to make sure a players input is valid, otherwise they lose a life.
        If they didn't go, they also lose a life.
        '''
        for player, state in self.state['players'].items():
            if state['hp'] != 'dead' and state['hp'] > 0:
                state['old_correct'] = state['correct']
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
        game.check_answers()
        game.QuickMaff(game, level)
        game.action({'player': 'B', 'valid': game.state['valid']})
        game.action({'player': 'A', 'valid': None})
        game.check_answers()
        game.Simon(game, level)
        game.action({'player': 'A', 'valid': game.state['valid']})
        game.check_answers()
        level += 1
        game.display()

