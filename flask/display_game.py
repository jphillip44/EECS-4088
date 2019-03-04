#!/usr/bin/python3
import desktop
import games
import time

class DisplayGame():

    prevGame = ""

    def __init__(self):
        self.screenSetup = desktop.DesktopUI()
        self.curScreen = desktop.PlayerUI(self.screenSetup)
        self.screenSetup.win.update()
        
    def update(self, obj):
        '''
        A psuedo-visitor pattern construct, whenever update is called, it receives a copy of the object that needs to be updated.
        It then calls a function by the same name and displays that item on the screen.
        '''
        getattr(self, obj.__class__.__name__.casefold())(obj)

    def players(self, obj):
        '''
        The call for the player connection screen
        '''
        if not(isinstance(self.curScreen, desktop.PlayerUI)):
            self.curScreen = desktop.PlayerUI(self.screenSetup)
            self.curScreen.PlayerShow(obj.players)

        else:
            self.curScreen.PlayerShow(obj.players)

        self.screenSetup.win.update()

    def ranks(self, obj):
        '''
        The game over call to display the final results
        '''
        print(obj.ranks)
        self.curScreen.standings(obj.ranks)
        self.screenSetup.win.update()

    def double07(self, obj):
        '''
        The function for any update to the main screen when the current game is 007
        '''
        timerVal = obj.state.get('timer')
        
        if not (isinstance(self.curScreen, desktop.Double07UI)):
            self.curScreen = desktop.Double07UI(self.screenSetup, obj.state)
        else:
            if timerVal > -1:
                self.curScreen.timer(timerVal) 
            else:
                self.curScreen.__init__(self.screenSetup, obj.state)
   
        self.screenSetup.win.update()


    def hot_potato(self, obj):
        '''
        The function for any update to the main screen when the current game is Hot Potato
        '''
        if not (isinstance(self.curScreen, desktop.HotPotatoUI)):
            self.curScreen = desktop.HotPotatoUI(self.screenSetup, obj.state)
        else:
            self.curScreen.__init__(self.screenSetup, obj.state)
        self.screenSetup.win.update()

    def match(self, obj):
        '''
        The function for any update to the main screen when the current game is Match
        '''
        # checks why the function was called (first run, cursor moved, card taken or timer tick)
        if not (isinstance(self.curScreen, desktop.MatchingUI)):
            self.curScreen = desktop.MatchingUI(self.screenSetup, obj.state, obj.columns, obj.rows)
        elif not (self.curScreen.prevCursor == obj.state.get('cursor')):
            self.curScreen.cursorMove(obj.state.get('cursor'), obj.state.get('gameBoard'))
        elif obj.state.get('gameBoard')[obj.state.get('cursor')[0], obj.state.get('cursor')[1]] == 'ZZ' and not self.curScreen.cardTaken:
           self.curScreen.cardTaken = True
           self.curScreen.cardTakenPos = obj.state.get('cursor')
           self.curScreen.updateCard(obj.state.get('gameBoard')[obj.state.get('cursor')[0], obj.state.get('cursor')[1]], obj.state.get('cursor'), True)
        else:
            self.curScreen.displayTimer(obj.state.get('timer'), obj.state.get('next', ['broken'])[0])
            self.curScreen.nextPlayer(obj.state.get('next')[1])
        
        # if both cards get taken, wait for them to be displayed on the controller, then return them to the display
        if self.curScreen.cardTaken and not (obj.state.get('gameBoard')[self.curScreen.cardTakenPos[0], self.curScreen.cardTakenPos[1]] == "ZZ"):
            self.curScreen.updateCard("ZZ", obj.state.get('cursor'), True)
            self.screenSetup.win.update()
            time.sleep(5)
            if not (list(obj.state.get('gameBoard').flatten()).count('XX') == 0): 
                self.curScreen.cardTaken = False
                self.curScreen.updateCard(obj.state.get('gameBoard')[self.curScreen.cardTakenPos[0], self.curScreen.cardTakenPos[1]], self.curScreen.cardTakenPos, False)
                self.curScreen.updateCard(obj.state.get('gameBoard')[obj.state.get('cursor')[0], obj.state.get('cursor')[1]], obj.state.get('cursor'), True)

        self.screenSetup.win.update()

    def fragments(self, obj):
        '''
        The function for any update to the main screen when the current game is Fragments
        '''
        if not (isinstance(self.curScreen, desktop.FragmentsUI)):
            self.curScreen = desktop.FragmentsUI(self.screenSetup, obj.state)
        else:
            if obj.state.get('timer') < obj.state.get('maxTimer'):
                self.curScreen.timer(obj.state.get('timer'))
            else: 
                self.curScreen.__init__(self.screenSetup, obj.state)

        self.screenSetup.win.update()
    

    def multigame(self, obj):
        '''
        The function for any update to the main screen when the current game is MultiGame
        '''
        if obj.state.get('name'):
            if not (isinstance(self.curScreen, desktop.MultiGameUI)):
                self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
            else:
                timerVal = obj.state.get('timer')
                if not(timerVal == 0) and self.curScreen.prevGame == obj.state.get('name'):
                    self.curScreen.displayTimer(timerVal)
                else:
                    self.curScreen.__init__(self.screenSetup, obj.state)
                    self.screenSetup.win.update()
            self.curScreenprevGame = obj.state.get('name')
        else:
            self.curScreen = desktop.MultiGameUI(self.screenSetup, obj.state)
            self.screenSetup.win.update()

    def instructions(self, obj):
        '''
        The function for displaying the instructions before any game begins
        '''
        print(obj.string)
        self.curScreen = desktop.instructionsUI(self.screenSetup, obj.string)
        self.screenSetup.win.update()
        time.sleep(25)


if __name__ == '__main__':
    '''
        Main function for testing without running the game properly (initialization testing and error checking)
    '''
    DISPLAY = DisplayGame()
    PLAYERS = ['WWWWWWWWWW/ddd', 'player2', 'player3', 'player4']
    # DISPLAY.update(PLAYERS)
    # time.sleep(30)
    GAME = games.Double07(PLAYERS)
    DISPLAY.update(GAME)
    # time.sleep(5)
    GAME = games.Hot_Potato(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(2)
    GAME = games.Match(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
    GAME = games.Fragments(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
    GAME = games.MultiGame(PLAYERS)
    DISPLAY.update(GAME.deepcopy)
    # time.sleep(5)
 