#!/usr/bin/python3
from abc import ABC, abstractmethod

class Game(ABC):

    def __init__(self, players):
        self.players = players
        super().__init__()

    @abstractmethod
    def play(self):
        pass
