from tkinter import Tk, Label, Frame
from tkinter.font import Font
import math
import os
import time
from pathlib import Path
from PIL import Image, ImageTk
from __screen import DesktopUI


class Double07UI():
    window = 0 #DesktopUI()

    topframe = 0
    rightframe = 0
    leftframe = 0
    centerframe = 0

    topFrameLabel = ""

    def __init__(self, ui, obj):
        self.window = ui
        self.setup()
        self.display(obj['players'], obj['timer'])
        self.timer(obj['timer'], obj['players'])

    def setup(self):
        topFrame = Frame(height = self.window.screenH / 10, width = self.window.screenW, bg= self.window.backgroundC)
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.place(x = 0, y = 0)
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
        

    def display(self, players, timer):
        numPlay = len(players)
        leftPlay = math.ceil(numPlay / 2)
        rightPlay = math.floor(numPlay / 2)
        center = int(self.window.screenH / 2)
        offset = int(self.window.screenH / 10)
        textColour = "white"
        doubleFont = self.window.setFontSize(int(self.window.screenH / 50))
                
        for i, player in enumerate(players):
            lives = self.heartDisplay(players[player].get("hp"))
            prevAct = self.actions(players[player].get("defend"))
            if i < leftPlay:
                if  (leftPlay / 2) % 2 == 1:
                    #background image
                    #playerFrame = Frame(height = (self.window.screenH / 15), width = (3 * self.window.screenW / 12), bg =  "black")
                    #playerFrame.pack_propagate(False)
                    #playerFrame.place(anchor = "w", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW /16)
                    #self.window.addFrame(playerFrame)

                    label = Label(self.leftframe, text = player, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)#.pack()
                    label.place(anchor = "w", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 32)

                    label2 = Label(self.leftframe, text = "HP: ", image = lives, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)
                    label2.image = lives #ensures image isnt trash collected
                    label2.place(anchor = "center", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 7)
                    
                    label3 = Label(self.leftframe, text = "Act: /n", image = prevAct, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)
                    label3.image = prevAct
                    label3.place(anchor = "e", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = self.window.screenW / 4)



                else:
                    label = Label(self.leftframe, text = player, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)
                    label.place(anchor = "w", y = center - (leftPlay / 2 + .5 - i) * offset, x = self.window.screenW / 32) 


                    label2 = Label(self.leftframe, text = "HP: ", image = lives, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)
                    label2.image = lives
                    label2.place(anchor = "center", y = center - (leftPlay / 2 + .5 - i) * offset, x = self.window.screenW / 7) 

                    label3 = Label(self.leftframe, text = "Act: /n" , image = prevAct, font = doubleFont, bg = self.leftframe['bg'], fg = textColour)
                    label3.image = prevAct
                    label3.place(anchor = "e", y = center - (leftPlay / 2 + .5 - i) * offset, x = self.window.screenW / 4) 
            else:
                if (rightPlay % 2) == 1:
                    label = Label(self.rightframe, text = player, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label.place(anchor = "w", y = center - ((((rightPlay - 1) / 2) - (i - leftPlay) + 1) * offset), x = self.window.screenW / 32)

                    label2 = Label(self.rightframe, text = "HP: ", image = lives, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label2.image = lives
                    label2.place(anchor = "center", y = center - ((((rightPlay - 1) / 2) - (i - leftPlay) + 1) * offset), x = self.window.screenW / 7) 

                    label3 = Label(self.rightframe, text = "Act: /n" , image = prevAct, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label3.image = prevAct
                    label3.place(anchor = "e", y = center - ((((rightPlay - 1) / 2) - (i - leftPlay) + 1) * offset), x = self.window.screenW / 4.1) 
                else:
                    label = Label(self.rightframe, text = player, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label.place(anchor = "w", y = center - (rightPlay / 2 + .5 - (i - leftPlay)) * offset, x = self.window.screenW / 32) 

                    label2 = Label(self.rightframe, text = "HP: ", image = lives, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label2.image = lives 
                    label2.place(anchor = "center", y = center - (rightPlay / 2 + .5 - (i - leftPlay)) * offset, x = self.window.screenW / 7) 

                    label3 = Label(self.rightframe, text = "Act: /n" , image = prevAct, font = doubleFont, bg = self.rightframe['bg'], fg = textColour)
                    label3.image = prevAct
                    label3.place(anchor = "e", y = center - (rightPlay / 2 + .5 - (i - leftPlay)) * offset, x = self.window.screenW / 4.1) 



    def actions(self, act):
        path = os.path.join(os.path.relpath(os.path.dirname(__file__)),  '../../public/images')
        imageFolder = Path(path)
       
        if act == 'none':
            imgName = "Reload.png"
        elif act == 'all':
            imgName = "Defend.png"
        else:
            imgName = "Attack.png"

        imgFile = os.path.join(imageFolder, imgName)
        img = Image.open(imgFile)

        img = img.resize((int(self.window.screenW / 15), int(self.window.screenH / 10)))

        ph = ImageTk.PhotoImage(img)
        return ph

    def timer (self, timer, players):
        if timer >= 0:
            topFrameLabel = Label(self.topframe, text = "Time Remaining to select an action: " + str(timer), font = self.window.deffont, bg = self.rightframe['bg'], fg = "white") 
            topFrameLabel.place(anchor = "center", y = self.window.screenH / 20, x = self.window.screenW / 2) 

        if timer == -1:
            topFrameLabel = Label(self.topframe, text = "Time Remaining to select an action: 0", font = self.window.deffont, bg = self.rightframe['bg'], fg = "white") 
            topFrameLabel.place(anchor = "center", y = self.window.screenH / 20, x = self.window.screenW / 2) 

            self.eventlog(players)


    def heartDisplay(self, number):
        path = os.path.join(os.path.relpath(os.path.dirname(__file__)),  '../../public/images')
        imageFolder = Path(path)

        if number == 0 or number == 'dead':
            imgName ="0Heart.png"
        elif number == 1:
            imgName ="1Heart.png"
        elif number == 2:
            imgName ="2Heart.png"
        elif number == 3:
            imgName ="3Heart.png"

        imgFile = os.path.join(imageFolder, imgName)

        img = Image.open(imgFile)

        img = img.resize((int(self.window.screenW / 15), int(self.window.screenH / 20)))

        ph = ImageTk.PhotoImage(img)

        return ph

    def eventlog(self, players):
        playerActed = []
        
        act = 0
        result = 0
        posCounter = 0

        ELFont = self.window.setFontSize(int (self.window.screenH / 30))
        textColour = "white"

        path = os.path.join(os.path.relpath(os.path.dirname(__file__)),  '../../public/images')
        imageFolder = Path(path)
        
        for player in players:
            if players[player].get('hp') != "dead":

                curPlayerAction = players[player].get('defend')

                if not(curPlayerAction == "none" or curPlayerAction == "all" or (player in playerActed)):
                
                    oppAct = players[curPlayerAction].get('defend')
                    playerActed.append(player)

                    if oppAct == 'all':
                        playerActed.append(curPlayerAction)
                        act = "Attack.png"
                        result = "Defend.png"
                        
                    elif oppAct == 'none' or oppAct != player:
                        act = "Attack.png"
                        result = "Heart.png"

                    else:
                        playerActed.append(curPlayerAction)
                        act = "CAttack.png"
                        result = "none"

                    posY = self.window.screenH * (1/10 + 1/10 * posCounter)

                    label1 = Label(self.centerframe, text = player, font = ELFont, bg = self.centerframe['bg'], fg = textColour)
                    label1.place(anchor = "nw", y = posY, x = 1/40 * self.window.screenW / 2)

                    imgFile = os.path.join(imageFolder, act)
                    img = Image.open(imgFile)
                    img = img.resize((int(self.window.screenW / 30), int(self.window.screenH / 20)))

                    actImg = ImageTk.PhotoImage(img)
                    
                    label2 = Label(self.centerframe, image = actImg, bg = self.centerframe['bg']) 
                    label2.image = actImg 
                    label2.place(anchor = "nw", y = posY, x = 17/40 * self.window.screenW / 2)

                    label3 = Label(self.centerframe, text = curPlayerAction, font = ELFont, bg = self.centerframe['bg'], fg = textColour)
                    label3.place(anchor = "ne", y = posY, x = 35.5/40 * self.window.screenW / 2)

                    if result != 'none':
                        imgFile2 = os.path.join(imageFolder, result)
                        img2 = Image.open(imgFile2)
                        img2 = img2.resize((int(self.window.screenW / 30), int(self.window.screenH / 20)))

                        resImg = ImageTk.PhotoImage(img2)

                        label4 = Label(self.centerframe, image = resImg, bg = self.centerframe['bg']) 
                        label4.image = resImg 
                        label4.place(anchor = "nw", y = posY, x = 36.5/40 * self.window.screenW / 2)

                    posCounter += 1
                    time.sleep(1)
                    self.window.win.update()   

            else:
                playerActed.append(player)


       
        for player in players:
            act = 0

            if not (player in playerActed):
                playerAct = players[player].get('defend')
                if playerAct == "none":
                    act = "Reload.png"
                else:
                    act = "Defend.png"
                
                posY = (1/10 + 1/10 * posCounter) * self.window.screenH 

                label1 = Label(self.centerframe, text = player, font = ELFont, bg = self.centerframe['bg'], fg = textColour)
                label1.place(anchor = "nw", y = posY, x = 1/40 * self.window.screenW / 2)

                imgFile = os.path.join(imageFolder, act)
                img = Image.open(imgFile)
                img = img.resize((int(self.window.screenW / 30), int(self.window.screenH / 20)))

                actImg = ImageTk.PhotoImage(img)
                
                label2 = Label(self.centerframe, image = actImg, bg = self.centerframe['bg']) 
                label2.image = actImg
                label2.place(anchor = "nw", y = posY, x = 17/40 * self.window.screenW / 2)
                
                posCounter += 1
                time.sleep(1)
                self.window.win.update()   
        
        self.window.win.update()   
        time.sleep(2)  

def main():
    pass
    #kek = __screen.DesktopUI()
    #Double07UI(kek, [], 10)
    #mainloop()

                
if __name__ == '__main__':
    main()
