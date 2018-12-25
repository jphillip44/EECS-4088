#!/usr/bin/python3
from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, players):
        self.__players = players
        super().__init__()
        self.play()

    @classmethod
    def name(self):
        '''
        This function returns the name of the current function.
        '''
        return self.__name__

    @abstractmethod
    def play(self):
        '''
        The play function is meant to be a generic function to start the game.
        Each game defines its own play function and calls the necessary startup functions as needed.
        Is called at __init__.
        '''
        pass

    @abstractmethod
    def action(self, data):
        '''
        The action function represents a generic construct for handling inputs from a controller.
        Each game can defines its own action function and parses `data' specifically as needed.
        The `data' field is a dictionary that can be loaded as json data.
        '''
        pass
