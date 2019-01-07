#!/usr/bin/python3
import random

from collections import OrderedDict
from queue import Queue
from __game import Game

class Fragments(Game):
    __move_queue = Queue()
    __pool = None

    def __init__(self, players, images=50, **kwargs):
        def init_state(players, images):
            self.state['players'] = {}
            for player in players:
                self.state['players'][player] = {'score': 0}
            self.__pool = [format(x, '02d') + ".fragment.jpg" for x in range(images)] 
            self.reset_state()
 
        super().__init__(players, **kwargs)
        if self.socketio:
            self.socketio.on_event('select', self.action)
        init_state(self.players, images)

    def reset_state(self):
            self.state['fragments'] = random.sample(self.__pool, 9)
            self.state['selection'] = random.choice(self.state['fragments'])
            self.state['display'] = self.state['selection'].replace('.fragment', '')
            self.state['timer'] = 30

    def display(self):
        if self.active:
            print(self.state['players'])
            print("Fragments: " + str(self.state['fragments']))
            print("Selection: "+ self.state['selection'])
            print("Display: " + self.state['display'])
        else:
            self.print_standings()

    def action(self, data, timer=None):
        print(data)
        if timer is None:
            timer = round(self.state['timer'], 2)
        if data['selection'] == self.state['selection']:
            self.state['players'][data['player']]['score'] += timer
        else:
            self.state['players'][data['player']]['score'] -= min(self.state['players'][data['player']]['score'], timer)

    def run_game(self):
        count = 0
        while self.active:
            self.display_game.update(self.deepcopy)
            self.socketio.emit('turn', self.state, broadcast=True)
            while self.state['timer'] > 0:
                print(round(self.state['timer']))
                for _ in range(100):
                    self.socketio.sleep(0.01)
                    self.state['timer'] -= 0.01
            else:
                self.display()
                self.state['timer'] = 30
                self.reset_state()
                count += 1
                if count == 5:
                    self.end_game()
                    self.rank_players()


if __name__ == '__main__':
    game = Fragments(['A', 'B', 'C'])
    game.display()
    game.action({'player': 'A', 'selection': game.state['selection']}, 25.77)
    game.action({'player': 'B', 'selection': game.state['selection']}, 19.31)
    game.action({'player': 'C', 'selection': "XX"}, 11.64)
    game.display()
    game.action({'player': 'A', 'selection': "XX"}, 5.61)
    game.action({'player': 'B', 'selection': "XX"}, 22.5)
    game.action({'player': 'C', 'selection': game.state['selection']}, 17.44)
    game.display()
    game.end_game()
    game.rank_players()
    game.display()