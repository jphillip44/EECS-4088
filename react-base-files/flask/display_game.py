import desktop
import games

class DisplayGame():

    def start():
        pass

    def update(obj):
        getattr(DisplayGame, obj.__class__.__name__)(obj)

    def list(obj):
        print(obj)
        # pass

    def Double07(obj):
        print(obj.state)

    def Hot_Potato(obj):
        print(obj.state)

    def Match(obj):
        print(obj.state)


if __name__ == '__main__':
    DisplayGame.start()
    player_list = ['player1', 'player2']
    DisplayGame.update(player_list)
    game = games.Double07(['A', 'B'])
    DisplayGame.update(game)
    game = games.Hot_Potato(['A', 'B'])
    DisplayGame.update(game)
 