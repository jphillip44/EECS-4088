import desktop
import games

class DisplayGame():

    def update(self, obj):
        getattr(self, obj.__class__.__name__)(obj)

    def list(self, obj):
        print(*obj, sep='\n')

    def Double07(self, obj):
        obj.display()

    def Hot_Potato(self, obj):
        obj.display()


if __name__ == '__main__':
    player_list = ['player1', 'player2']
    DisplayGame().update(player_list)
    game = games.Double07(['A', 'B'])
    DisplayGame().update(game)
    game = games.Hot_Potato(['A', 'B'])
    DisplayGame().update(game)
 