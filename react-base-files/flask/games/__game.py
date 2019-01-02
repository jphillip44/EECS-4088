#!/usr/bin/python3
from abc import ABC, abstractmethod
from flask_socketio import emit
from queue import LifoQueue

class Game(ABC):
    __active_game = False
    __input_timer = 0
    __ranks = LifoQueue()

    def __init__(self, players, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        super().__init__()
        self.socketio = kwargs.get('socketio')
        self.display_game = kwargs.get('display')
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
        self.__active_game = False

    def is_active(self):
        '''
        Query to determine if a game is active.
        '''
        return self.__active_game

    def get_players(self):
        return self.__players

    def set_timer(self, time):
        self.__input_timer = time

    def get_timer(self):
        return self.__input_timer

    # def timed_event(self, timer=get_timer):
    #     '''
    #     Allows setting of custom timer events for a game
    #     '''
    #     if type(timer) is not int:
    #         timer = timer(self)
    #     for i in range(timer, 0, -1):
    #         print(i)
    #         sleep(1)
    #     return timer

    
    def get_state(self):
        '''
        Query to get game estate
        '''
        return self.__state

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

        
