import random
import itertools

from collections import OrderedDict
from queue import PriorityQueue
from __game import Game


class Hot_Potato(Game):
    __next = None
    __hold_potato = False

    def __init__(self, players, **kwargs):
        def init_state(players):
            self.state['timer'] = self.__new_potato_timer()
            self.state['players'] = OrderedDict()
            for player in players:
                self.state['players'][player] = {'score': 0}
            self.state['next'] = self.__get_turn()

        super().__init__(players, **kwargs)
        if self.__dict__.get('socketio'):
            self.socketio.on_event('endOfTurn', self.action)
        init_state(self.players)

    def action(self, data):
        self.__hold_potato = False
        if self.active:
            print(data)
            self.__hold(data['player'], data.get('time'))
            if self.state['players'][data['player']]['score'] > 20:
                self.end_game()
                self.rank_players()
            self.display()
        if self.__dict__.get('display_game'):
            self.display_game.update(self)

    def display(self):
        if self.active:
            print("timer: " + str(self.state['timer']), end = ", ")
            print("penalty: " + str(self.state['penalty']), end=", ")
            print("next: " + self.state['next'], end=', ')
            print(*self.state['players'].items())
        else:
            self.print_standings()

    def run_game(self):
        while self.active:
            self.socketio.emit('state', self.state, broadcast=True)
            self.__hold_potato = True
            while self.__hold_potato:
                if self.state['timer'] > 0:
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
        if time and self.state['timer'] > 0:
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

    # def __rank_players(self):
    #     results = PriorityQueue()
    #     for player, stats in self.state['players'].items():
    #         results.put((stats['score'], player))
    #     while not results.empty():
    #         self.add_ranks(results.get()[1])

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


