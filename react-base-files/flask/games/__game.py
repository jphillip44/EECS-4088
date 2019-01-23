#!/usr/bin/python3
from copy import deepcopy, copy
from abc import ABC, abstractmethod
from queue import Queue, PriorityQueue
from collections import OrderedDict

class Game(ABC):
    class Ranks():
        def __init__(self, start=0):
            self.__ranks = []

        def append(self, player):
            self.__ranks.append(player)

        def __iter__(self):
            for item in self.__ranks:
                yield item

        @property
        def ranks(self):
            return self.__ranks

    def __init__(self, players, default, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        self.__state = {}
        super().__init__()
        self.nocopy = list(kwargs.keys())
        self.socketio = kwargs.get('socketio', None)
        self.display_game = kwargs.get('display_game', None)
        self.__players = players
        self.__name__ = self.__class__.__name__
        print("New "+self.__name__+" Started")
        self.__active_game = True
        self.ranks = self.Ranks()
        self.state['players'] = OrderedDict()
        for player in players:
            self.state['players'][player] = copy(default)

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in self.nocopy:
                setattr(result, k, deepcopy(v, memo))
        return result

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def run_game(self):
        pass

    def end_game(self):
        '''
        Signal for ending a game.
        '''
        self.active = False

    @property
    def active(self):
        '''
        Query to determine if a game is active.
        '''
        return self.__active_game

    @active.setter
    def active(self, value):
        self.__active_game = value

    @active.deleter
    def active(self):
        del self.__active_game

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @state.deleter
    def state(self):
        del self.__state

    @property
    def players(self):
        return self.__players

    @property
    def deepcopy(self):
        return deepcopy(self)

    def print_standings(self):
        '''
        Prints standings.
        '''
        print("Standings")
        for i, item in enumerate(self.ranks, 1):
            print(str(i) + ": " + str(item))

    def rank_players(self):
        results = PriorityQueue()
        for player, stats in self.state['players'].items():
            results.put((stats['score'], player))
        while not results.empty():
            # self.add_ranks(results.get()[1])
            self.ranks.append(results.get()[1])

    def remove_player(self, player):
        if player in self.state['players']:
            self.state['players'].pop(player)
