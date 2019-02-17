class Instructions():
    def __init__(self):
        self.string = ""

    def get(self, name):
        getattr(self, name.casefold())()
        return self

    def double07(self):
        self.string = """
            007
Each player starts with 3 life points and 2 action points
Defending and attacking cost 1 action point
Reloading grants 1 action point
Attacking a player that is reloading or attacking another players results in them losing 1 life point and the attacker gaining 1 action point
Defending against an attack from another player will grant the player defending 1 action point
Once a player loses all of their life points they are eliminated
The goal is to be the last player with life points

        """

    def hot_potato(self):
        self.string = """
The objective the game is to to be the first player to equal or exceed the point total
When the potato is in your possession swipe the potato away to pass it to another player.
For each second you hold the potato without it exploding you will earn 1 point.
If the potato explodes in your possession the seconds you held the potato will be deducted from your point total.
        """

    def match(self):
        self.string = """
Users will be split into teams of 2.
One player at a time will be tasked with picking a card from the board of cards displayed on the main computer screen by navigating with the directional pad on their mobile device.
A selected card will be turned face up.
Once the user picks a card their partner will attempt to find that cards matching pair by navigating through the board and selecting another card.
If the team member does not find the matching card both cards are turned face down and that teams turn ends.
If the team member finds the matching card then those 2 cards are removed from the board and that team is awarded a point. 
The team with the most points once the board has been cleared is the winner.
        """

    def fragments(self):
        self.string = """
An image will be shown on the main computer screen. 
Your task is to select the image on your mobile device that is part of the larger image on the computer screen. 
Users who select the correct fragment will be awarded a point.
The user with the most points at the end of the round wins the game.
        """

    def multigame(self):
        self.string = """
You will be asked to complete a series of tasks. Failure to complete the task correctly will result the offending player being deducted 1 point. Once the game ends users will be ranked based on who has the most points.
		
Quicktap
Your task is to tap the button on your screen as many times as is indicated on the computer screen.

Simon
A series of squares of varying colors are shown on the computer screen. Your task is to enter the combination of colors on your mobile device.

Quickmaff
A simple math equation will be shown on the computer screen. You will be prompted to enter the result on your handheld device.
        """