from __game import Game, emit
from collections import OrderedDict
from random import randint
from itertools import cycle
from queue import PriorityQueue

class Hot_Potato(Game):
    __next = None
    __state = {}
    __hold_potato = False
    

    def __init__(self, players, **kwargs):
        super().__init__(players, **kwargs)
        if self.__dict__.get('socketio'):
            self.socketio.on_event('endOfTurn', self.action)
        self.__set_state(super().get_players())

    def action(self, data):
        self.__hold_potato = False
        if self.is_active():
            print(data)
            self.__hold(data['player'], data.get('time'))
            if self.__state['players'][data['player']]['score'] > 50:
                super().end_game()
                self.__rank_players()
            self.display()
        if self.__dict__.get('display_game'):
            self.display_game.update(self)

    def display(self):
        if self.is_active():
            print("timer: " + str(self.__state['timer']), end = ", ")
            print("penalty: " + str(self.__state['penalty']), end=", ")
            print("next: " + self.__state['next'], end=', ')
            print(*self.__state['players'].items())
        else:
            self.print_standings()

    def run_game(self):
        while self.is_active():
            self.socketio.emit('state', self.__state, broadcast=True)
            self.__hold_potato = True
            while self.__hold_potato:
                if self.__state['timer'] > 0:
                    self.socketio.sleep(1)
                    print(self.__state['timer'])
                    self.__state['timer'] -= 1
                else:
                    self.socketio.emit('explode', room=self.__state['next'])
                    self.__hold_potato = False
                    self.socketio.sleep(1)
        else:
            print("Game Over")
            self.socketio.emit('gameOver', broadcast=True)

    def __set_state(self, players):
        self.__state['timer'] = self.__new_potato_timer()
        self.__state['players'] = OrderedDict()
        for player in players:
            self.__state['players'][player] = {'score': 0}
        self.__state['next'] = self.__get_turn()

    def __hold(self, player, time):
        self.__state['next'] = self.__get_turn()
        if time and self.__state['timer'] > 0:
            self.__state['players'][player]['score'] += time
        else:
            self.__state['players'][player]['score'] -= min(self.__state['players'][player]['score'], self.__state['penalty'])
            self.__state['timer'] = self.__new_potato_timer()

    def __get_turn(self):
        if self.__next is None:
            self.__next = cycle(self.__state['players'].keys())
        return next(self.__next)

    def __new_potato_timer(self):
        self.__state['penalty'] = randint(1, 20)
        return self.__state['penalty']

    def __rank_players(self):
        results = PriorityQueue()
        for player, stats in self.__state['players'].items():
            results.put((stats['score'], player))
        while not results.empty():
            self.add_ranks(results.get()[1])

    def get_state(self):
        return self.__state

if __name__ == '__main__':
    game = Hot_Potato(['A', 'B', 'C'])
    game.display()
    game.action({'player': game._Hot_Potato__state['next'], 'time': 5})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 9})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 1})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 6})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 3})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 8})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 2})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 9})
    game.action({'player': game._Hot_Potato__state['next'], 'time': 3})
    game = Hot_Potato(map(chr, range(ord('a'),ord('z')+1)))
    game.display()


