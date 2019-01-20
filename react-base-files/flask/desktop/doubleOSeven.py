from tkinter import Tk, Label, Frame
from tkinter.font import Font
import math
import os
import time
from pathlib import Path
from PIL import Image, ImageTk
from __screen import DesktopUI


class Double07UI(DesktopUI):
    window = 0 #DesktopUI()

    topframe = 0
    rightframe = 0
    leftframe = 0
    centerframe = 0

    topFrameLabel = ""

    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        super().setup()

        self.display(obj['players'], obj['timer'])
        self.timer(obj['timer'], obj['players'])

    def display(self, players, timer):
        numPlay = len(players)
        leftPlay = math.ceil(numPlay / 2)
        rightPlay = math.floor(numPlay / 2)
        center = int(self.window.screenH / 2)
        offset = int(self.window.screenH / 8)
        textColour = "white"
        doubleFont = self.window.setFontSize(int(self.window.screenH / 50))


        for i, player in enumerate(players):
            lives = self.heartDisplay(players[player].get("hp"))
            prevAct = self.actions(players[player].get("defend"))
           
            curFrame = super().framelist[2]

            xPosPH = super().getScreenW() / 128
            xPosA = super().getScreenW() / 4.1
            yPosP = 0
            yPosHA = super().getScreenH() / 30
            

            if i < leftPlay:
                curFrame = super().framelist[1]
                if  (leftPlay / 2) % 2 == 1:
                    yPosP = center - ((((leftPlay - 1) / 2) - i + 1) * offset)

                else:
                    yPosP = center - (leftPlay / 2 + .5 - i) * offset
            else:
                if (rightPlay % 2) == 1:
                    yPosP = center - ((((rightPlay - 1) / 2) - (i - leftPlay) + 1) * offset)
                    
                else:
                    yPosP = center - (rightPlay / 2 + .5 - (i - leftPlay)) * offset

            label = Label(curFrame, text = player, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label.place(anchor = "nw", y = yPosP, x = xPosPH) 

            label2 = Label(curFrame, text = "HP: ", image = lives, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label2.image = lives 
            label2.place(anchor = "nw", y = yPosP + yPosHA, x = xPosPH) 

            label3 = Label(curFrame, text = "Act: " , image = prevAct, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label3.image = prevAct
            label3.place(anchor = "e", y = yPosP + yPosHA, x = xPosA)             

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
            topFrameLabel = Label(super().framelist[0], text = "Time Remaining to select an action: " + str(timer), font = self.window.deffont, bg = self.rightframe['bg'], fg = "white") 
            topFrameLabel.place(anchor = "center", y = self.window.screenH / 20, x = self.window.screenW / 2) 

        if timer == -1:
            topFrameLabel = Label(super().framelist[0], text = "Time Remaining to select an action: 0", font = self.window.deffont, bg = self.rightframe['bg'], fg = "white") 
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

        ELFont = self.window.setFontSize(int (self.window.screenH / 50))
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

                    label1 = Label(self.centerframe, text = player, font = ELFont, bg = super().framelist[3]['bg'], fg = textColour)
                    label1.place(anchor = "nw", y = posY, x = 1/40 * self.window.screenW / 2)

                    imgFile = os.path.join(imageFolder, act)
                    img = Image.open(imgFile)
                    img = img.resize((int(self.window.screenW / 30), int(self.window.screenH / 20)))

                    actImg = ImageTk.PhotoImage(img)
                    
                    label2 = Label(self.centerframe, image = actImg, bg = super().framelist[3]['bg']) 
                    label2.image = actImg 
                    label2.place(anchor = "nw", y = posY, x = 17/40 * self.window.screenW / 2)

                    label3 = Label(self.centerframe, text = curPlayerAction, font = ELFont, bg = super().framelist[3]['bg'], fg = textColour)
                    label3.place(anchor = "ne", y = posY, x = 35.5/40 * self.window.screenW / 2)

                    if result != 'none':
                        imgFile2 = os.path.join(imageFolder, result)
                        img2 = Image.open(imgFile2)
                        img2 = img2.resize((int(self.window.screenW / 30), int(self.window.screenH / 20)))

                        resImg = ImageTk.PhotoImage(img2)

                        label4 = Label(self.centerframe, image = resImg, bg = super().framelist[3]['bg']) 
                        label4.image = resImg 
                        label4.place(anchor = "nw", y = posY, x = 36.5/40 * self.window.screenW / 2)

                    posCounter += 1
                    time.sleep(1.5)
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
        time.sleep(5)  

def main():
    pass
                
if __name__ == '__main__':
    main()
