from game import Game
from queue import Queue, PriorityQueue, LifoQueue

class Double07(Game):
    '''
    Class Attributes:
        __state encodes the global state of the game.
        the queue methods are used to sequence game moves by priority, not timing.
        __ranks is used to compute the winner.
    '''
    __state = {}
    __attack_queue = Queue()
    __target_queue = Queue()
    __other_queue = Queue()
    __ranks = LifoQueue()

    def play(self):
        '''
        Inherited from Game. Setups the games default parameters.
        Is called at __init__.
        '''
        print("New "+self.name()+" Started")
        self.__set_state(self._Game__players)

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

    def display(self):
        '''
        Displays the game state to the console.
        '''
        print(self.__state, end='\n')
        self.__rank_players()

    def __set_state(self, players):
        '''
        Setups the game state for each player with default parameters.
        '''
        for player in players:
            self.__state[player] = {'lives' : 3, 'ap': 1, 'defend': 'none'}

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
            self.__state[other]['lives'] -= 1

    def __handle_queues(self):
        '''
        Processes the queues one at a time to prioritize actions.
        First two queues setup defenses and reloads.
        Last queue handles attacks.
        '''
        while not self.__other_queue.empty():
            action = self.__other_queue.get()
            exec('self._'+self.name()+'__' + action[1] + "(\'" + str(action[0] + '\')'))
        while not self.__target_queue.empty():
            action = self.__target_queue.get()
            self.__target(action[0], action[1])
        while not self.__attack_queue.empty():
            action = self.__attack_queue.get()
            self.__attack(action[0], action[1])

    def __rank_players(self):
        '''
        Ranks players based on order of death.
        Simultaneous deaths are tie-broken by the player with greater AP.
            If that is tied, it is broken arbitrarily(pretty sure alphabetical order kicks in)
        '''
        dead = PriorityQueue()
        def check_dead():
            '''
            A local function to __rank_players(). 
            Adds players to ranking queue if they are dead.
            '''
            for player, stats in self.__state.items():
                if stats['lives'] != 'dead' and stats['lives'] <= 0:
                    dead.put((stats['ap'], player))
                    self.__state[player]['lives'] = 'dead'
            while not dead.empty():
                player = dead.get()
                self.__ranks.put(player[1])

        def check_alive():
            '''
            A local function to __rank_players().
            Returns a list of living players.
            '''
            for player, stats in self.__state.items():
                if stats['lives'] != 'dead':
                    yield player

        def print_standings(alive):
            '''
            A local function to __rank_players().
            Adds remaining living player(if any) to standings.
            Prints standings
            '''
            for player in alive:
                self.__ranks.put(player) 
            i = 1
            print("Standings")
            while not self.__ranks.empty():
                print(str(i) + ": " + self.__ranks.get())
                i += 1
                
        check_dead()
        alive = list(check_alive())
        if len(alive) < 2:
            print_standings(alive)



def main():
    game = Double07(['A','B', 'C'])
    game.display()
    game.action({'player': "C",'action': 'defend'})
    game.action({'player': "B",'action': 'reload'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")    # test hit
    game.display()
    game.action({'player': "A", 'action': 'attack', 'other':'B'})
    game.action({'player': "B", 'action': 'defend'})
    game.action({'player': "C", 'action': 'reload'})
    exec("game._"+game.name()+"__handle_queues()")    # test defend
    game.display()
    game.action({'player': "A", 'action': 'reload'})
    game.action({'player': "B", 'action': 'attack', 'other': 'C'})
    game.action({'player': "C", 'action': 'attack', 'other': 'B'})
    exec("game._"+game.name()+"__handle_queues()") # test simultaneous fire
    game.display()
    game.action({'player': "C",'action': 'reload'})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")    # test hit
    game.display()
    game.action({'player': "C",'action': 'attack', "other": "A"})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")    # test 3 way hit and death
    game.display()
    game.action({'player': "A",'action': 'attack', 'other':'C'})
    game.action({'player': "C", 'action': 'reload'})
    exec("game._"+game.name()+"__handle_queues()")    # should trigger end game
    game.display()

    game = Double07(['A','B', 'C'])
    game.display()
    game.action({'player': 'A', 'action': 'reload'})
    game.action({'player': 'C', 'action': 'defend'})
    game.action({'player': 'B', 'action': 'reload'})
    exec("game._"+game.name()+"__handle_queues()")
    game.display()
    game.action({'player': 'A', 'action': 'defend'})
    game.action({'player': 'C', 'action': 'reload'})
    game.action({'player': 'B', 'action': 'reload'})
    exec("game._"+game.name()+"__handle_queues()")
    game.display()
    game.action({'player': "C",'action': 'attack', "other": "A"})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")
    game.display()
    game.action({'player': "C",'action': 'attack', "other": "A"})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")
    game.display()
    game.action({'player': "C",'action': 'attack', "other": "A"})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    exec("game._"+game.name()+"__handle_queues()")    #triple kill
    game.display() 
    
if __name__ == '__main__':
    main()


