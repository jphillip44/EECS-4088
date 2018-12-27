from game import Game
from queue import Queue, PriorityQueue, LifoQueue

class Double07(Game):
    '''
    Class Attributes:
        __state encodes the global state of the game.
        the queue methods are used to sequence game moves by priority, not timing.
        __ranks is used to compute the winner.
    '''
    __attack_queue = Queue()
    __target_queue = Queue()
    __other_queue = Queue()
    __ranks = LifoQueue()

    def __init__(self, players):
        '''
        Sets up the games default parameters.
        '''
        super().__init__(players)
        self.__set_state(self._Game__players)
        self.__input_timer = 15

    def action(self, data):
        '''
        Inherited from Game. Handles controller input.
        In Double07, passes off input to a series of queues for later processing.
        '''
        if data['action'] == "attack":
            self.__attack_queue.put((data['player'], data['other']))
            self.__target_queue.put((data['player'], data['other']))
        else:
            self.__other_queue.put((data['player'], data['action']))

    def end_round(self):
        '''
        Inherited from Game. Handles game at the end of a round.
        Processes the queues one at a time to prioritize actions.
        First two queues setup defenses and reloads (not exclusively).
        Last queue handles attacks.
        '''
        while not self.__other_queue.empty():
            player, action = self.__other_queue.get()
            getattr(self, '_'+self.__name__+'__' + action)(player)
        while not self.__target_queue.empty():
            self.__target(*self.__target_queue.get())
        while not self.__attack_queue.empty():
            self.__attack(*self.__attack_queue.get())

    def display(self):
        '''
        Displays the game state to the console.
        '''
        print(self.__state)
        self.__rank_players()

    def __set_state(self, players):
        '''
        Setups the game state for each player with default parameters.
        '''
        self.__state = {}
        for player in players:
            self.__state[player] = {'hp' : 3, 'ap': 1, 'defend': 'none'}

    def __defend(self, player):
        '''
        Handles logic for the defend action.
        '''
        self.__state[player]['defend'] = "all"
        self.__state[player]['ap'] -= 1

    def __reload(self, player):
        '''
        Handles logic for the reload action.
        '''
        self.__state[player]['defend'] = "none"
        self.__state[player]['ap'] += 1

    def __target(self, player, other):
        '''
        Handles defend logic for attack action.
        Sets defense to attacker to prevent double attacks.
        '''
        self.__state[player]['defend'] = other

    def __attack(self, player, other):
        '''
        Handles logic attack action.
        Handles different cases of success/failure.
        '''
        if self.__state[other]['defend'] == "all":
            self.__state[other]['ap'] += 1
            self.__state[player]['ap'] -= 1
        elif self.__state[other]['defend'] == player:
            self.__state[player]['ap'] -= 1
        else:
            self.__state[other]['hp'] -= 1

    def __rank_players(self):
        '''
        Ranks players based on order of death.
        Simultaneous deaths are tie-broken by the player with greater AP.
            If that is tied, it is broken arbitrarily (pretty sure reverse alphabetical order kicks in)
        '''
        dead = PriorityQueue()
        def check_dead():
            '''
            A local function to __rank_players(). 
            Adds players to ranking queue if they are dead.
            '''
            for player, stats in self.__state.items():
                if stats['hp'] != 'dead' and stats['hp'] <= 0:
                    dead.put((stats['ap'], player))
                    self.__state[player]['hp'] = 'dead'
            while not dead.empty(): 
                self.__ranks.put(dead.get()[1])

        def check_alive():
            '''
            A local function to __rank_players().
            Returns a list of living players.
            '''
            for player, stats in self.__state.items():
                if stats['hp'] != 'dead':
                    yield player

        def print_standings(alive):
            '''
            A local function to __rank_players().
            Prints standings.
            '''

            i = 1
            print("Standings")
            while not self.__ranks.empty():
                print(str(i) + ": " + self.__ranks.get())
                i += 1


        check_dead()
        alive = list(check_alive())
        if len(alive) < 2:
            for player in alive:
                self.__ranks.put(player) 
            print_standings(alive)
            self.end_game()




def main():
    game = Double07(['A','B', 'C'])
    game.display()
    game.action({'player': "C", 'action': 'defend'})
    game.action({'player': "B", 'action': 'reload'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()    #test hit
    game.display()
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.action({'player': "B", 'action': 'defend'})
    game.action({'player': "C", 'action': 'reload'})
    game.end_round()    # test defend
    game.display()
    game.action({'player': "A", 'action': 'reload'})
    game.action({'player': "B", 'action': 'attack', 'other': 'C'})
    game.action({'player': "C", 'action': 'attack', 'other': 'B'})
    game.end_round() # test simultaneous fire
    game.display()
    game.action({'player': "C", 'action': 'reload'})
    game.action({'player': "B", 'action': 'attack', "other": 'C'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()    # test hit
    game.display()
    game.action({'player': "C", 'action': 'attack', "other": 'A'})
    game.action({'player': "B", 'action': 'attack', "other": 'C'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()    # test 3 way hit and death
    game.display()
    game.action({'player': "A", 'action': 'attack', 'other':'C'})
    game.action({'player': "C", 'action': 'reload'})
    game.end_round()    # should trigger end game
    game.display()

    game = Double07(['A','B', 'C'])
    game.display()
    game.action({'player': "A", 'action': 'reload'})
    game.action({'player': "C", 'action': 'defend'})
    game.action({'player': "B", 'action': 'reload'})
    game.end_round()
    game.display()
    game.action({'player': "A", 'action': 'defend'})
    game.action({'player': "C", 'action': 'reload'})
    game.action({'player': "B", 'action': 'reload'})
    game.end_round()
    game.display()
    game.action({'player': "C", 'action': 'attack', "other": 'A'})
    game.action({'player': "B", 'action': 'attack', "other": 'C'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()
    game.display()
    game.action({'player': "C", 'action': 'attack', "other": 'A'})
    game.action({'player': "B", 'action': 'attack', "other": 'C'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()
    game.display()
    game.action({'player': "C", 'action': 'attack', "other": 'A'})
    game.action({'player': "B", 'action': 'attack', "other": 'C'})
    game.action({'player': "A", 'action': 'attack', 'other': 'B'})
    game.end_round()    #triple kill
    game.display() 

    # game = Double07([chr(c) for c in range(ord('A'), ord('Z') + 1)])
    game = Double07(map(chr, range(ord('a'),ord('z')+1)))
    game.display()
    
if __name__ == '__main__':
    main()


