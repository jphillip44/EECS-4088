from game import Game
from queue import Queue

class _007(Game):
    state = {}
    attack_queue = Queue()


    def play(self):
        self.set_state(self.players.values())
        print(self.state)

    def set_state(self, players):
        for player in players:
            self.state[player] = {'lives' :3, 'ap':1, 'action': 'none'}

    def defend(self, player):
        self.state[player]['action'] = 'defend'
        self.state[player]['ap'] -= 1

    def reload(self, player):
        self.state[player]['action'] = 'reload'
        self.state[player]['ap'] += 1

    def attack(self, player, other_player):
        attack_queue.put(player, other)

    # def handle_attack(self, attack_queue):


    # def handle_queues(self, players):


