#!/usr/bin/python3
import random

from __game import Queue, Game

class Fragments(Game):
    def __init__(self, players, images=12, **kwargs):
        '''
        Sets up the games default parameters.
        '''
        super().__init__(players, {'score': 0}, **kwargs)
        self.__move_queue = Queue()
        if self.socketio is not None:
            self.socketio.on_event('select', self.action)
        self.__pool = [format(x, '02d') +"." + str(random.randint(0,9)) + ".jpg" for x in range(images)] 
        self.reset_state()

    def reset_state(self):
        '''
        Resets the game state back to default for a new round.
        '''
        self.state['fragments'] = random.sample(self.__pool, 9)
        self.state['selection'] = random.choice(self.state['fragments'])
        self.state['display'] = self.state['selection'].replace('.fragment', '')
        self.state['timer'] = 30

    def display(self):
        '''
        Displays game state to the terminal.
        '''
        if self.active:
            print(self.state['players'])
            print("Fragments: " + str(self.state['fragments']))
            print("Selection: "+ self.state['selection'])
            print("Display: " + self.state['display'])
        else:
            self.print_standings()

    def action(self, data, timer=None):
        '''
        Handles input logic. Increases score for correct answer, decreases for incorrect.
        '''
        print(data)
        if timer is None:
            timer = round(self.state['timer'], 2)
        if data['selection'] == self.state['selection']:
            self.state['players'][data['player']]['score'] += timer
        else:
            self.state['players'][data['player']]['score'] -= min(self.state['players'][data['player']]['score'], timer)

    def run_game(self):
        '''
        Function that runs the gameloop from the server.
        '''
        count = 0
        timer = self.state['timer']
        while self.active:
            self.display_game.update(self.deepcopy)
            self.socketio.emit('turn', self.state, broadcast=True)
            while self.state['timer'] > 0:
                print(round(self.state['timer']))
                for _ in range(100):
                    self.socketio.sleep(0.01)
                    self.state['timer'] -= 0.01
                self.display_game.update(self.deepcopy)
            else:
                self.display()
                self.state['timer'] = timer
                self.reset_state()
                count += 1
                if count == 5:
                    self.end_game()
            super().run_game()


if __name__ == '__main__':
    game = Fragments(['A', 'B', 'C'])
    game.display()
    game.action({'player': 'A', 'selection': game.state['selection']}, 25.77)
    game.action({'player': 'B', 'selection': game.state['selection']}, 19.31)
    game.action({'player': 'C', 'selection': "XX"}, 11.64)
    game.display()
    game.action({'player': 'A', 'selection': "XX"}, 5.61)
    game.action({'player': 'B', 'selection': "XX"}, 22.5)
    game.action({'player': 'C', 'selection': game.state['selection']}, 17.44)
    game.display()
    game.end_game()
    game.rank_players()
    game.display()
    game = Fragments(['A', 'B', 'C'])
    game.end_game()
    game.rank_players()
    game.display()