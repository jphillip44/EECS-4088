#!/usr/bin/python3
from copy import copy, deepcopy
from abc import ABC, abstractmethod
from queue import Queue, PriorityQueue

class Game(ABC):
    __active_game = False

    def __init__(self, players, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        self.__state = {}
        super().__init__()
        self.nocopy = list(kwargs.keys())
        self.nocopy.append('_Game__ranks')
        self.socketio = kwargs.get('socketio', None)
        self.display_game = kwargs.get('display_game', None)
        self.__players = players
        self.__name__ = self.__class__.__name__
        print("New "+self.__name__+" Started")
        self.__active_game = True
        self.__ranks = Queue()

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
        for i, item in enumerate(self.get_standings(), 1):
            print(str(i) + ": " + item)

    def get_standings(self):
        for item in reversed(self.__ranks.queue):
            yield item

    def add_ranks(self, data):
        self.__ranks.put(data)

    def rank_players(self):
        results = PriorityQueue()
        for player, stats in self.state['players'].items():
            results.put((stats['score'], player))
        while not results.empty():
            self.add_ranks(results.get()[1])
