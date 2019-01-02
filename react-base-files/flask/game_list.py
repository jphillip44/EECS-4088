import games

class GameList():

    def select_game(type, users, **kwargs):
        return getattr(games, type)(users, **kwargs)

    def list_games():
        return [game.__name__ for game in games.Game.__subclasses__()]

if __name__ == '__main__':
    print(GameList.list_games())
    game = GameList.select_game("Double07", {"A", "B"})
    game.display()



        
