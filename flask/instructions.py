class Instructions():
    def __init__(self):
        self.string = ""

    def get(self, name):
        getattr(self, name.casefold())()
        return self

    def double07(self):
        self.string = """
Each player starts with 3 life points and 1 action point
Defending and attacking cost 1 action point
Reloading grants 1 action point
Successfully attack hitting an attack on a player grants 1 action point
An attack is successful if the target is reloading or attacking a different players
If the attack is not blocked, the target loses 1 HP
Defending against an attack from another player will grant the player defending 1 action point for each block
Once a player loses all of their life points they are eliminated
The goal is to be the last player alive
        """

    def hot_potato(self):
        self.string = """
The objective the game is to to be the first player to equal or exceed the point total
When the potato is in your possession swipe the potato away to pass it to another player.
For each second you hold the potato without it exploding you will earn 1 point.
If the potato explodes in your possession you will lose points equal to the total number of seconds the current potato has been in play
        """

    def match(self):
        self.string = """
One at a time, the current player will be tasked with picking a card from the board of cards displayed on the main computer screen by navigating with the directional pad on their mobile device.
A selected card will be turned appear face down on their mobile device.
The next player attempts to find the matching pair to the card selected by the first player by navigating through the board and selecting another card.
If there is not a match both cards are turned face down and returned to the board.
If there is a match then those 2 cards are are returned to the board. 
The standings at the end will show the players based on the number of matches they were a part of.
        """

    def fragments(self):
        self.string = """
An image will be shown on the main computer screen. 
Your task is to select the image on your mobile device that is part of the larger image on the computer screen. 
Users who select the correct fragment will be awarded a points.
The faster you select the correct image the more points you will be awarded.
If you are incorrect, they will lose points.
The user with the most points at the end of all the rounds wins.
        """

    def multigame(self):
        self.string = """
You will be asked to complete a series of tasks. Failure to complete the task correctly will result the offending player being deducted 1 life.
Last player with lives remaining wins.

Quicktap
Your task is to tap the button on your screen as many times as is indicated on the computer screen in the time allotted.

Simon
A series of squares of varying colors are shown on the computer screen. Your task is to re-enter the combination of colors on your mobile device within the time allotted.

Quick maffs
A math equation will be shown on the computer screen. You will be prompted to enter the result on your handheld device within the time allotted.
        """