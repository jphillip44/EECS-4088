#!/usr/bin/python3
import desktop
import games
import time

class DisplayGame():

    def __init__(self):
        self.screenSetup = desktop.DesktopUI()
        self.curScreen = desktop.PlayerUI(self.screenSetup)
        self.screenSetup.win.update()
        
    def update(self, obj):
        getattr(self, obj.__class__.__name__)(obj)

    def list(self, obj):
        # print(obj)
        self.curScreen = desktop.PlayerUI(self.screenSetup)
        self.curScreen.PlayerShow(obj)
        self.screenSetup.win.update()

    def Ranks(self, obj):
        print(obj.ranks)

    def Double07(self, obj):
        # print(obj.state)
        self.curScreen = desktop.Double07UI(self.screenSetup, obj.state)        
        self.screenSetup.win.update()


    def Hot_Potato(self, obj):
        # print(obj.state)
        self.curScreen = desktop.HotPotatoUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def Match(self, obj):
        # print(obj.state)
        self.curScreen = desktop.MatchingUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def Fragments(self, obj):
        # print(obj.state)
        pass

    def MultiGame(self, obj):
        if obj.state.get('name'):
            getattr(self, obj.state['name'])(obj)
        else:
            print(obj.state)
            self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
            self.screenSetup.win.update()
            pass

    def Simon(self, obj):
        print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()
        pass

    def MultiTap(self, obj):
        print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()
        pass

    def QuickMaff(self, obj):
        print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()
        pass


if __name__ == '__main__':
    DISPLAY = DisplayGame()
    PLAYERS = ['WWWWWWWWWW/ddd', 'player2', 'player3', 'player4']
    DISPLAY.update(PLAYERS)
    # time.sleep(3)
    GAME = games.Double07(PLAYERS)
    DISPLAY.update(GAME)
    time.sleep(5)
    GAME = games.Hot_Potato(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(2)
    GAME = games.Match(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
    GAME = games.Fragments(PLAYERS)
    DISPLAY.update(GAME)
    GAME = games.MultiGame(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
 