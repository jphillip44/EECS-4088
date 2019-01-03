import desktop
import games

class DisplayGame():

    def update(obj):
        getattr(DisplayGame, obj.__class__.__name__)(obj)

    def list(obj):
        print("users")
        print(*obj, sep='\n') if obj else print('none')

    def Double07(obj):
        print(obj.get_state())

    def Hot_Potato(obj):
        print(obj.get_state())

    def Match(obj):
        print(obj.get_state())


if __name__ == '__main__':
    player_list = ['player1', 'player2']
    DisplayGame.update(player_list)
    game = games.Double07(['A', 'B'])
    DisplayGame.update(game)
    game = games.Hot_Potato(['A', 'B'])
    DisplayGame.update(game)
 