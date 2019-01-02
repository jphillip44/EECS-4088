from Screen import DesktopUI
from tkinter import mainloop, Frame, Label
from tkinter.font import Font
import math

class PlayerUI ():
    window = DesktopUI()
    topframe = 0
    rightframe = 0
    leftframe = 0
    centerframe = 0
    deffont = Font(family = "Times", size = int(window.screenH / 30)) 
    
    def __init__(self, ui = window):
        self.setup(ui)

    def setup(self, ui = window):
        self.screen = ui
        topFrame = Frame(height = self.window.screenH / 10, width = self.window.screenW, bg="green")
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.pack()
        self.topframe = topFrame
        self.window.addFrame(topFrame)
        leftFrame = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 4, bg = "black")
        leftFrame.pack_propagate(False)
        leftFrame.place(x = 0, y = self.window.screenH / 10)
        self.leftframe = leftFrame
        self.window.addFrame(leftFrame)
        rightFrame = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 4, bg = "black")
        rightFrame.pack_propagate(False)
        rightFrame.place(x = (self.window.screenW / 4) * 3, y = self.window.screenH / 10)
        self.rightframe = rightFrame
        self.window.addFrame(rightFrame)
        centerFrame = Frame(height = (self.window.screenH / 10) * 8, width = (self.window.screenW / 4) * 2, bg = "red")
        centerFrame.pack_propagate(False)
        centerFrame.place(x = (self.window.screenW / 4), y = self.window.screenH / 10)
        self.centerframe = centerFrame
        self.window.addFrame(centerFrame)
        label1 = Label(centerFrame, text="Go to website or scan the below code to enter the lobby", bg = centerFrame['bg'], fg = "white", font = self.deffont, wraplength = self.window.screenW / 2)
        label1.place(x = self.window.screenW / 4, y = self.window.screenH / 10, anchor = 'center')
        self.NewPlayer()

    def NewPlayer (self):
        numPlay = len(self.window.players)
        leftPlay = math.ceil(numPlay / 2)
        rightPlay = math.floor(numPlay / 2)
        center = int(self.window.screenH / 2)
        offset = int(self.window.screenH / 10)
        textColour = "white"

        #left player list
        if (leftPlay % 2) == 1:
            for i in range(leftPlay):
                label = Label(self.leftframe, text = self.window.players[2 * i], font = self.deffont, bg = self.leftframe['bg'], fg = textColour)
                label.place(anchor = "center", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 8)
        else:
            for i in range(leftPlay):
                label = Label(self.leftframe, text = self.window.players[2 * i], font = self.deffont, bg = self.leftframe['bg'], fg = textColour)
                label.place(anchor = "center", y = center - (leftPlay / 2 + .5 - i) * offset, x = self.window.screenW / 8) 

        #right player list
        if (rightPlay % 2) == 1:
            for i in range(rightPlay):
                label = Label(self.rightframe, text = self.window.players[2 * i + 1], font = self.deffont, bg = self.rightframe['bg'], fg = textColour)
                label.place(anchor = "center", y = center - ((((rightPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 8)
        else:
            for i in range(rightPlay):
                label = Label(self.rightframe, text = self.window.players[2 * i + 1], font = self.deffont, bg = self.rightframe['bg'], fg = textColour)
                label.place(anchor = "center", y = center - (rightPlay / 2 + .5 - i) * offset, x = self.window.screenW / 8) 
   
    def AddPlayer(self, newPlayer):
        self.window.reset()
        self.window.players.append(newPlayer)
        print(len(self.window.players))
        self.setup()
          
           

                    
                

kek = PlayerUI()
mainloop()

kek.AddPlayer("P20")
mainloop()

#kek.window.reset()
#mainloop()
