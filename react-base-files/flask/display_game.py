import desktop
import games

class DisplayGame():

    def switch(self, obj):
        getattr(self, obj.__name__)(obj)

    def Double07(self, obj):
        obj.display()

    def Hot_Potato(self, obj):
        obj.display()


if __name__ == '__main__':
    game = games.Double07(['A', 'B'])
    DisplayGame().switch(game)
    game = games.Hot_Potato(['A', 'B'])
    DisplayGame().switch(game)
 