#!/usr/bin/python3
from abc import ABC, abstractmethod

class Game(ABC):
    __state = {}
    __active_game = False
    __input_timer = 0

    def __init__(self, players):
        '''
        Sets up the games default parameters.
        '''
        super().__init__()
        self.__players = players
        self.__name__ = self.__class__.__name__
        print("New "+self.__name__+" Started")
        self.__active_game = True

    @abstractmethod
    def action(self, data):
        '''
        The action function represents a generic construct for handling inputs from a controller.
        Each game can defines its own action function and parses `data' specifically as needed.
        The `data' field is a dictionary that can be loaded as json data.
        WARNING: will not run if this is not defined in the child class. 
        '''

    @abstractmethod
    def end_round(self):
        pass

    @abstractmethod
    def display(self):
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

    def timed_event(self):
        '''
        Allows setting of custom timer events for a game
        '''
        return range(self.__input_timer, 0, -1)

    def get_state(self):
        '''
        Query to get game estate
        '''
        return self.__state

        
