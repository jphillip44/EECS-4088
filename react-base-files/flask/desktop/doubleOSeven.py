from tkinter import *
from tkinter.font import Font
import math
from __screen import DesktopUI


class Double07UI():
    window = DesktopUI()
    deffont = Font(family = "Times", size = int(window.screenH / 30)) 

    topframe = 0
    rightframe = 0
    leftframe = 0
    centerframe = 0

    def __init__(self, ui, players, timer):
        self.window = ui
        self.setup()
        self.display(players)
        self.timer(timer)

    def setup(self):
        topFrame = Frame(height = self.window.screenH / 10, width = self.window.screenW, bg= self.window.backgroundC)
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.pack()
        self.topframe = topFrame
        self.window.addFrame(topFrame)
        leftFrame = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 4, bg = self.window.backgroundC)
        leftFrame.pack_propagate(False)
        leftFrame.place(x = 0, y = self.window.screenH / 10)
        self.leftframe = leftFrame
        self.window.addFrame(leftFrame)
        rightFrame = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 4, bg =  self.window.backgroundC)
        rightFrame.pack_propagate(False)
        rightFrame.place(x = (self.window.screenW / 4) * 3, y = self.window.screenH / 10)
        self.rightframe = rightFrame
        self.window.addFrame(rightFrame)
        centerFrame = Frame(height = (self.window.screenH / 10) * 8, width = (self.window.screenW / 4) * 2, bg =  self.window.backgroundC)
        centerFrame.pack_propagate(False)
        centerFrame.place(x = (self.window.screenW / 4), y = self.window.screenH / 10)
        self.centerframe = centerFrame
        self.window.addFrame(centerFrame)
        

    def display(self, players):
        numPlay = len(players)
        leftPlay = math.ceil(numPlay / 2)
        rightPlay = math.floor(numPlay / 2)
        center = int(self.window.screenH / 2)
        offset = int(self.window.screenH / 10)
        textColour = "white"
        
        for i in range(numPlay):
            if i < leftPlay:
                    if  (leftPlay / 2) % 2 == 1:
                        #background image
                        label = Label(self.leftframe, text = players[i], font = self.deffont, bg = self.leftframe['bg'], fg = textColour)
                        label.place(anchor = "left", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 8)


    def actions(self, players):
        pass

    def timer (self, timer):
        pass        

def main():
    pass
    #kek = __screen.DesktopUI()
    #Double07UI(kek, [], 10)
    #mainloop()

                
if __name__ == '__main__':
    main()
