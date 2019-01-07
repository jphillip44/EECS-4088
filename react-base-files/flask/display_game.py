import desktop
import games

class DisplayGame():

    def start(self):
        pass

    def update(self, obj):
        getattr(self, obj.__class__.__name__)(obj)

    def list(self, obj):
        print(obj)
        # pass

    def Double07(self, obj):
        print(obj.state)

    def Hot_Potato(self, obj):
        print(obj.state)

    def Match(self, obj):
        print(obj.state)

    def Fragments(self, obj):
        print(obj.state)


if __name__ == '__main__':
    display = DisplayGame()
    display.start()
    player_list = ['player1', 'player2']
    display.update(player_list)
    game = games.Double07(['A', 'B'])
    display.update(game.deepcopy)
    game = games.Hot_Potato(['A', 'B'])
    display.update(game.deepcopy)
    game = games.Match(['A', 'B'])
    display.update(game.deepcopy)
    game = games.Fragments(['A', 'B'])
    display.update(game.deepcopy)
 