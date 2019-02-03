import desktop

class Double07UI(desktop.DesktopUI):
    window = 0 
    topFrameLabel = ""

    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        super().setup()

        self.display(obj.get('players'), obj.get('timer'))
        self.timer(obj.get('timer'), obj('players'))

    def display(self, players, timer):
        numPlay = len(players)
        leftPlay = desktop.math.ceil(numPlay / 2)
        rightPlay = desktop.math.floor(numPlay / 2)
        center = int(super().getScreenH() / 2)
        offset = int(super().getScreenH() / 8)
        textColour = "white"
        doubleFont = super().setFontSize(int(super().getScreenH() / 50))


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

            label = desktop.Label(curFrame, text = player, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label.place(anchor = "nw", y = yPosP, x = xPosPH) 

            label2 = desktop.Label(curFrame, text = "HP: ", image = lives, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label2.image = lives 
            label2.place(anchor = "nw", y = yPosP + yPosHA, x = xPosPH) 

            label3 = desktop.Label(curFrame, text = "Act: " , image = prevAct, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label3.image = prevAct
            label3.place(anchor = "e", y = yPosP + yPosHA, x = xPosA)             

    def actions(self, act):
         
        if act == 'none':
            imgName = "Reload.png"
        elif act == 'all':
            imgName = "Defend.png"
        else:
            imgName = "Attack.png"

        return super().imageCreation(imgName, super().getScreenH() / 10,  super().getScreenW() / 15)

    def timer (self, timer, players):
        if timer >= 0:
            topFrameLabel = desktop.Label(super().framelist[0], text = "Time Remaining to select an action: " + str(timer), font = self.window.deffont, bg = super().framelist[2]['bg'], fg = "white") 
            topFrameLabel.place(anchor = "center", y = super().getScreenH() / 20, x = super().getScreenW() / 2) 

        if timer == -1:
            topFrameLabel = desktop.Label(super().framelist[0], text = "Time Remaining to select an action: 0", font = self.window.deffont, bg = super().framelist[2]['bg'], fg = "white") 
            topFrameLabel.place(anchor = "center", y = super().getScreenH() / 20, x = super().getScreenW() / 2) 

            self.eventlog(players)


    def heartDisplay(self, number):

        if number == 0 or number == 'dead':
            imgName ="0Heart3.png"
        elif number == 1:
            imgName ="1Heart3.png"
        elif number == 2:
            imgName ="2Heart3.png"
        elif number == 3:
            imgName ="3Heart3.png"

        return super().imageCreation(imgName, super().getScreenH() / 20,  super().getScreenW() / 15, "/double07")

    def eventlog(self, players):
        playerActed = []
        
        act = 0
        result = 0
        posCounter = 0

        ELFont = super().setFontSize(int (super().getScreenH() / 50))
        textColour = "white"

        for player in players:
            if players[player].get('hp') != "dead" or players[player].get('defend') != 'none':

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

                    posY = super().getScreenH() * (1/10 + 1/10 * posCounter)

                    label1 = desktop.Label(super().framelist[3], text = player, font = ELFont, bg = super().framelist[3]['bg'], fg = textColour)
                    label1.place(anchor = "nw", y = posY, x = 1/40 * super().getScreenW() / 2)

                    actImg = super().imageCreation(act, int(super().getScreenH() / 20), int(super().getScreenW() / 30))
                    
                    label2 = desktop.Label(super().framelist[3], image = actImg, bg = super().framelist[3]['bg']) 
                    label2.image = actImg 
                    label2.place(anchor = "nw", y = posY, x = 17/40 * super().getScreenW() / 2)

                    label3 = desktop.Label(super().framelist[3], text = curPlayerAction, font = ELFont, bg = super().framelist[3]['bg'], fg = textColour)
                    label3.place(anchor = "ne", y = posY, x = 35.5/40 * super().getScreenW() / 2)

                    if result != 'none':
                        resImg = super().imageCreation(result, int(super().getScreenH() / 20), int(super().getScreenW() / 30))

                        label4 = desktop.Label(super().framelist[3], image = resImg, bg = super().framelist[3]['bg']) 
                        label4.image = resImg 
                        label4.place(anchor = "nw", y = posY, x = 36.5/40 * super().getScreenW() / 2)

                    posCounter += 1
                    self.window.win.update()   
                    desktop.time.sleep(2)

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
                
                posY = (1/10 + 1/10 * posCounter) * super().getScreenH() 

                label1 = desktop.Label(super().framelist[3], text = player, font = ELFont, bg = super().framelist[3]['bg'], fg = textColour)
                label1.place(anchor = "nw", y = posY, x = 1/40 * super().getScreenW() / 2)

                actImg = super().imageCreation(act, super().getScreenH() / 20, super().getScreenW() / 30)
                
                label2 = desktop.Label(super().framelist[3], image = actImg, bg = super().framelist[3]['bg']) 
                label2.image = actImg
                label2.place(anchor = "nw", y = posY, x = 17/40 * super().getScreenW() / 2)
                
                posCounter += 1
                self.window.win.update()   
                desktop.time.sleep(1)
        
        self.window.win.update()   
        desktop.time.sleep(3)  
    
    def standings(self, standings):
        super().standings(standings)
        self.window.win.update()
        desktop.time.sleep(10)  