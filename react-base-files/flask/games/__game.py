#!/usr/bin/python3
from copy import deepcopy, copy
from abc import ABC, abstractmethod
from queue import Queue, PriorityQueue
from collections import OrderedDict, deque

class Game(ABC):
    
    class Ranks():
        '''
        The ranks object is used by the display_game class to display standings.
        Its functionally a wrapper for a deque but exists as to define a function that
        expects a "Rank" object vs a "deque" object which is a common class.
        '''
        def __init__(self):
            '''
            Initializes Ranks as a deque().
            '''
            self.__ranks = deque()

        def prepend(self, player):
            '''
            Prepends player to ranks.
            '''
            self.__ranks.appendleft(player)

        def append(self, player):
            '''
            Appends player to ranks.
            '''
            self.__ranks.append(player)

        def __iter__(self):
            '''
            Makes ranks iterable.
            '''
            for item in self.__ranks:
                yield item

        @property
        def ranks(self):
            '''
            Public accessor for private object __ranks
            '''
            return self.__ranks

    def __init__(self, players, default, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        self.state = {}
        super().__init__()
        self.nocopy = list(kwargs.keys())
        self.socketio = kwargs.get('socketio', None)
        self.display_game = kwargs.get('display_game', None)
        self.__players = players
        self.__name__ = self.__class__.__name__
        print("New "+self.__name__+" Started")
        self.active = True
        self.ranks = self.Ranks()
        self.state['players'] = OrderedDict()
        for player in players:
            self.state['players'][player] = copy(default)
        self.__active_players = len(list(players))

    def __deepcopy__(self, memo):
        '''
        Redefines deepcopy to not include to not deepcopy private objects
        and items produced by optional arguments.
        '''
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in self.nocopy and not k.startswith('_'):
                setattr(result, k, deepcopy(v, memo))
        return result

    @abstractmethod
    def display(self):
        '''
        Abstract method display forces the child to redefine it.
        Used to display data to the console.
        '''
        pass

    @abstractmethod
    def run_game(self):
        '''
        Abstract method run_game forces the child to redefine it.
        Current version is only usable by calling super from child.
        '''
        if self.__active_players < 1:
            self.end_game()   

    def end_game(self):
        '''
        Signal for ending a game.
        '''
        self.active = False
        self.rank_players()
        self.display()
        if self.display_game is not None:
            self.display_game.update(self.ranks)
        print("Game Over")
        if self.socketio is not None:
            self.socketio.emit('gameOver', broadcast=True)

    @property
    def players(self):
        '''
        Public accessor for __players
        '''
        return self.__players

    @property
    def deepcopy(self):
        '''
        Allows functions in game to call obj.deepcopy without importing deepcopy.
        '''
        return deepcopy(self)

    def print_standings(self):
        '''
        Prints standings.
        '''
        print("Standings")
        for i, item in enumerate(self.ranks, 1):
            print(str(i) + ": " + str(item))

    def rank_players(self):
        '''
        Function for ranking players. Stores data in a priority queue to heapsort it.
        '''
        results = PriorityQueue()
        for player, stats in self.state['players'].items():
            results.put((stats['score'], player))
        while not results.empty():
            self.ranks.prepend(results.get()[1])

    def remove_player(self, player=None):
        '''
        Decrements player count if a player drops from a game.
        '''
        if self.check_alive(player):
            self.__active_players -= 1
        print("players left: " + str(self.__active_players))

    def add_player(self, player=None):
        '''
        Increments player if a player rejoins game.
        '''
        if self.check_alive(player):
            self.__active_players += 1
        print("players left: " + str(self.__active_players))

    def check_alive(self, player):
        '''
        Checks if a player is alive in the current game.
        '''
        if player is not None:
            hp = self.state['players'][player].get("hp")
            print(hp)
            if hp is not None and hp == "dead":
                return False
        return True

