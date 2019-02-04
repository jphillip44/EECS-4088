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
        getattr(self, obj.__class__.__name__.casefold())(obj)

    # def list(self, obj):
    #     # print(obj)
    #     self.curScreen = desktop.PlayerUI(self.screenSetup)
    #     self.curScreen.PlayerShow(obj)
    #     self.screenSetup.win.update()

    def players(self, obj):
        self.curScreen = desktop.PlayerUI(self.screenSetup)
        self.curScreen.PlayerShow(obj.players)
        self.screenSetup.win.update()

    def ranks(self, obj):
        print(obj.ranks)
        self.curScreen.standings(obj.ranks)
        self.screenSetup.win.update()

    def double07(self, obj):
        # print(obj.state)
        timerVal = obj.state.get('timer')
        
        if not (isinstance(self.curScreen, desktop.Double07UI)):
            self.curScreen = desktop.Double07UI(self.screenSetup, obj.state)
        else:
            if timerVal > 0:
                self.curScreen.timer(timerVal) 
            else:
                self.curScreen.__init__(self.screenSetup, obj.state)
   
        self.screenSetup.win.update()


    def hot_potato(self, obj):
        # print(obj.state)
        if not (isinstance(self.curScreen, desktop.HotPotatoUI)):
            self.curScreen = desktop.HotPotatoUI(self.screenSetup, obj.state)
        else:
            self.curScreen.__init__(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def match(self, obj):
        # print(obj.state)
        if not (isinstance(self.curScreen, desktop.MatchingUI)):
            self.curScreen = desktop.MatchingUI(self.screenSetup, obj.state)
        elif not (self.curScreen.prevCursor == obj.state.get('cursor')):
            self.curScreen.cursorMove(obj.state.get('cursor'), obj.state.get('gameBoard'))
        # elif True:
            # self.curScreen.__init__(self.screenSetup, obj.state)
        else:
            self.curScreen.displayTimer(obj.state.get('timer'), obj.state.get('next', ['broken'])[0])
            
        self.screenSetup.win.update()

    def fragments(self, obj):
        # print(obj.state)
        self.curScreen = desktop.FragmentsUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()
    

    def multigame(self, obj):
        if obj.state.get('name'):
            getattr(self, obj.state['name'])(obj)
        else:
            # print(obj.state)
            self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
            self.screenSetup.win.update()

    def simon(self, obj):
        # print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def multitap(self, obj):
        # print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def quickmaff(self, obj):
        # print(obj.state)
        self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def instructions(self, obj):
        # print(obj.string)
        pass


if __name__ == '__main__':
    DISPLAY = DisplayGame()
    PLAYERS = ['WWWWWWWWWW/ddd', 'player2', 'player3', 'player4']
    # DISPLAY.update(PLAYERS)
    # time.sleep(3)
    GAME = games.Double07(PLAYERS)
    DISPLAY.update(GAME)
    # time.sleep(5)
    GAME = games.Hot_Potato(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(2)
    GAME = games.Match(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    time.sleep(5)
    GAME = games.Fragments(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
    GAME = games.MultiGame(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
 