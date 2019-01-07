import desktop
import games

class DisplayGame():

    def start(self):
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


if __name__ == '__main__':
    DISPLAY = DisplayGame()
    DISPLAY.start()
    PLAYERS = ['player1', 'player2']
    DISPLAY.update(PLAYERS)
    GAME = games.Double07(['A', 'B'])
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Hot_Potato(['A', 'B'])
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Match(['A', 'B'])
    DISPLAY.update(GAME.deepcopy)
    GAME = games.Fragments(['A', 'B'])
    DISPLAY.update(GAME.deepcopy)
 