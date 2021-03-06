import games

class GameList():

    def select_game(name, users, **kwargs):
        '''
        Used to launch the specified game from the server.
        '''
        return getattr(games, name)(users, **kwargs)

    def list_games():
        '''
        Returns a list of all available games on the server. 
        '''
        return [game.__name__ for game in games.Game.__subclasses__()]

if __name__ == '__main__':
    print(GameList.list_games())
    GAME = GameList.select_game("Double07", {"A", "B"})
    GAME.display()
