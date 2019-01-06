import random

from collections import OrderedDict
from queue import Queue
from __game import Game

class Fragments(Game):

    def __init__(self, players, images=50, **kwargs):
        def init_state(players, images):
            pass

        super().__init__(players, **kwargs)
        if self.__dict__.get('socketio'):
            self.socketio.on_event('select', self.action)
        init_state(self.players, images)

    def display(self):
        pass

    def run_game(self):
        pass