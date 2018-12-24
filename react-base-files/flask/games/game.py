#!/usr/bin/python3
from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self):
        # self.value = values
        super().__init__()

    @abstractmethod
    def foo():
        pass

    def eval(self):
        return eval(self)
