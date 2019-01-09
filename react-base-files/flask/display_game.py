#!/usr/bin/python3
import desktop
import games

class DisplayGame():

    def __init__(self):
        pass

    def update(self, obj):
        getattr(self, obj.__class__.__name__)(obj)

    def list(self, obj):
        print(obj)

    def Double07(self, obj):
        print(obj.state)

    def Hot_Potato(self, obj):
        print(obj.state)

    def Match(self, obj):
        print(obj.state)

    def Fragments(self, obj):
        print(obj.state)

    def MultiGame(self, obj):
        if obj.state.get('name'):
            getattr(self, obj.state['name'])(obj)
        else:
            print(obj.state)

    def Sequence(self, obj):
        print(obj.state)

    def MultiTap(self, obj):
        print(obj.state)

    def QuickMaff(self, obj):
        print(obj.state)


if __name__ == '__main__':
    DISPLAY = DisplayGame()
    PLAYERS = ['player1', 'player2', 'player3']
    DISPLAY.update(PLAYERS)
    GAME = games.Double07(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Hot_Potato(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Match(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Fragments(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    GAME = games.MultiGame(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
 