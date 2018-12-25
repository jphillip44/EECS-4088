from game import Game
from queue import Queue, PriorityQueue, LifoQueue

class _007(Game):
    state = {}
    attack_queue = Queue()
    target_queue = Queue()
    other_queue = Queue()
    ranks = LifoQueue()

    def play(self):
        print("New 007 Started")
        self.set_state(self.players)

    def display(self):
        print(self.state, end='\n')
        self.rank_players()

    def set_state(self, players):
        for player in players:
            self.state[player] = {'lives' :3, 'ap':1, 'defend': 'none'}

    def defend(self, player):
        self.state[player]['defend'] = "all"
        self.state[player]['ap'] -= 1

    def reload(self, player):
        self.state[player]['defend'] = "none"
        self.state[player]['ap'] += 1

    def target(self, player, other):
        self.state[player]['defend'] = other

    def attack(self, player, other):
        if self.state[other]['defend'] == "all":
            self.state[other]['ap'] += 1
            self.state[player]['ap'] -=1
        elif self.state[other]['defend'] == player:
            self.state[player]['ap'] -=1
        else:
            self.state[other]['lives'] -=1

    def action(self, data):
        if data['action'] == "attack":
            self.attack_queue.put((data['player'], data['other']))
            self.target_queue.put((data['player'], data['other']))
        else:
            self.other_queue.put((data['player'], data['action']))

    def handle_queues(self):
        while not self.other_queue.empty():
            action = self.other_queue.get()
            exec(".".join(["self", action[1]]) + str(action[0]).join(['(\'','\')']))
        while not self.target_queue.empty():
            action = self.target_queue.get()
            self.target(action[0], action[1])
        while not self.attack_queue.empty():
            action = self.attack_queue.get()
            self.attack(action[0], action[1])

    def rank_players(self):
        dead = PriorityQueue()
        def check_dead():
            for player, stats in self.state.items():
                if stats['lives'] != 'dead' and stats['lives'] <= 0:
                    dead.put((-stats['ap'], player))
                    self.state[player]['lives'] = 'dead'
                while not dead.empty():
                    player = dead.get()
                    self.ranks.put(player[1])

        def check_alive():
            for player, stats in self.state.items():
                if stats['lives'] != 'dead':
                    yield player

        check_dead()
        alive = list(check_alive())
        if len(alive) < 2:
            for player in alive:
                self.ranks.put(player) 
            i = 1
            print("Standings")
            while not self.ranks.empty():
                print(str(i) + ": " + self.ranks.get())
                i += 1
                



    def check_endgame(self):
        def check_alive():
            for player in self.state.values():
                if player['lives']:
                    yield player

        if len(list(check_alive())) < 2:
            for player, vals in self.state.items():
                print(': '.join([player, str(vals['ap'] + vals['lives'])]))


def main():
    game = _007(['A','B', 'C'])
    game.play()
    game.display()
    game.action({'player': "C",'action': 'defend'})
    game.action({'player': "B",'action': 'reload'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    game.handle_queues()    # test hit
    game.display()
    game.action({'player': "A", 'action': 'attack', 'other':'B'})
    game.action({'player': "B", 'action': 'defend'})
    game.action({'player': "C", 'action': 'reload'})
    game.handle_queues()    # test defend
    game.display()
    game.action({'player': "A", 'action': 'reload'})
    game.action({'player': "B", 'action': 'attack', 'other': 'C'})
    game.action({'player': "C", 'action': 'attack', 'other': 'B'})
    game.handle_queues() # test simultaneous fire
    game.display()
    game.action({'player': "C",'action': 'reload'})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    game.handle_queues()    # test hit
    game.display()
    game.action({'player': "C",'action': 'attack', "other": "A"})
    game.action({'player': "B",'action': 'attack', "other": 'C'})
    game.action({'player': "A",'action': 'attack', 'other':'B'})
    game.handle_queues()    # test 3 way hit and death
    game.display()
    game.action({'player': "A",'action': 'attack', 'other':'C'})
    game.action({'player': "C", 'action': 'reload'})
    game.handle_queues()    # should trigger end game
    game.display()

    game = _007(['A','B', 'C', 'D'])
    game.play()
    game.display()

if __name__ == '__main__':
    main()


