#!/usr/bin/python3
from abc import ABC, abstractmethod
from flask_socketio import emit
from queue import LifoQueue

class Game(ABC):
    __active_game = False
    __ranks = LifoQueue()
    __state = {}

    def __init__(self, players, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        super().__init__()
        self.__dict__.update(kwargs)
        self.__players = players
        self.__name__ = self.__class__.__name__
        print("New "+self.__name__+" Started")
        self.__active_game = True

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def run_game(socketio):
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
 
    def get_players(self):
        return self.__players

    def print_standings(self):
        '''
        Prints standings.
        '''
        i = 1
        print("Standings")
        while not self.__ranks.empty():
            print(str(i) + ": " + self.__ranks.get())
            i += 1

    def add_ranks(self, data):
        self.__ranks.put(data)

        
