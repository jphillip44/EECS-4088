from tkinter import Tk, Label, Frame
from tkinter.font import Font
import math
from __screen import DesktopUI
import socket
import qrcode
from PIL import ImageTk

class PlayerUI (DesktopUI):
    window = 0 #DesktopUI()
       
    def __init__(self, ui):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()

    def setup(self):
        super().setup()

        super().framelist[1] = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 3, bg = self.window.backgroundC)
        super().framelist[1].pack_propagate(False)
        super().framelist[1].place(x = 0, y = self.window.screenH / 10)

        super().framelist[2] = Frame(height = (self.window.screenH / 10) * 8, width = self.window.screenW / 3, bg =  self.window.backgroundC)
        super().framelist[2].pack_propagate(False)
        super().framelist[2].place(x = (self.window.screenW / 3) * 2, y = self.window.screenH / 10)

        super().framelist[3] = Frame(height = (self.window.screenH / 10) * 8, width = (self.window.screenW / 3), bg =  self.window.backgroundC)
        super().framelist[3].pack_propagate(False)
        super().framelist[3].place(x = (self.window.screenW / 3), y = self.window.screenH / 10)

        IP = socket.gethostbyname(socket.gethostname())

        label1 = Label(super().framelist[0], text="Go to http://" + str(IP) + ":5000 or scan the below code to enter the lobby", bg = super().framelist[0]['bg'], fg = "white", font = self.window.deffont)
        label1.place(x = self.window.screenW / 2, y = self.window.screenH / 20, anchor = 'center')

        img = qrcode.make("http://" + str(IP) + ":5000")

        resImg = ImageTk.PhotoImage(img)

        label2 = Label(super().framelist[3], image = resImg)
        label2.image = resImg
        label2.place(anchor = 'center', x = super().getScreenW() / 6, y = super().getScreenH() * 2/5)

        
    def PlayerShow (self, players):
        numPlay = len(players)
        leftPlay = math.ceil(numPlay / 2)
        rightPlay = math.floor(numPlay / 2)
        center = int(self.window.screenH / 2)
        offset = int(self.window.screenH / 10)
        textColour = "white"
         
        self.window.reset()
        self.setup()

        #left player list
        if (leftPlay % 2) == 1:
            for i in range(leftPlay):
                label = Label(super().framelist[1], text = players[2 * i], font = self.window.deffont, bg = super().framelist[1]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 64)
        else:
            for i in range(leftPlay):
                label = Label(super().framelist[1], text = players[2 * i], font = self.window.deffont, bg = super().framelist[1]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - (leftPlay / 2 + .5 - i) * offset, x = self.window.screenW / 64) 

        #right player list
        if (rightPlay % 2) == 1:
            for i in range(rightPlay):
                label = Label(super().framelist[2], text = players[2 * i + 1], font = self.window.deffont, bg = super().framelist[2]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - ((((rightPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 64)
        else:
            for i in range(rightPlay):
                label = Label(super().framelist[2], text = players[2 * i + 1], font = self.window.deffont, bg = super().framelist[2]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - (rightPlay / 2 + .5 - i) * offset, x = self.window.screenW / 64) 

        
          
           
def main():
    pass              
                
if __name__ == '__main__':
    main()
