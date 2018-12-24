#!/usr/bin/python3
from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self):
        # self.value = values
        super().__init__()

    def factory(type):
        if type == "Game1": return Game1()

    @abstractmethod
    def foo(self):
        pass
