from game import Game
from queue import Queue

class _007(Game):
    state = {}
    attack_queue = Queue()
    target_queue = Queue()
    other_queue = Queue()

    def play(self):
        self.set_state(self.players.values())

    def display(self):
        print(self.state)

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

def main():
    game = _007({1: "Josh", 2:"JP", 3:'J'})
    game.play()
    game.display()
    game.action({'player': "J",'action': 'defend'})
    game.action({'player': "JP",'action': 'reload'})
    game.action({'player': "Josh",'action': 'attack', 'other':'JP'})
    game.handle_queues()
    game.display()
    game.action({'player': "Josh", 'action': 'attack', 'other':'JP'})
    game.action({'player': "JP", 'action': 'defend'})
    game.action({'player': "J", 'action': 'reload'})
    game.handle_queues()
    game.display()
    game.action({'player': "Josh", 'action': 'reload'})
    game.action({'player': "JP", 'action': 'attack', 'other': 'J'})
    game.action({'player': "J", 'action': 'attack', 'other': 'JP'})
    game.handle_queues()
    game.display()

if __name__ == '__main__':
    main()


