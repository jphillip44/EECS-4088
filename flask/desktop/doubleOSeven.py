import desktop

class Double07UI(desktop.DesktopUI):
    window = 0 
    topFrameLabel = "" # needed for timer to display properly, without text overlapping

    def __init__(self, ui, obj):
        '''
        Default setup, completed on first call
        '''

        self.window = ui
        super().setWindow(self.window.win)
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        super().setup()

        self.topFrameLabel = desktop.Label(super().framelist[0], text = 'init', font = self.window.deffont, bg = super().framelist[2]['bg'], fg = "white")
        self.topFrameLabel.place(anchor = "center", y = super().getScreenH() / 20, x = super().getScreenW() / 2) 

        self.timer(obj.get('timer'), obj.get('players'))
        self.display(obj.get('players'), obj.get('timer'))
        

    def display(self, players, timer):
        '''
        Prints out all the players, their current HP and their previous action
        '''
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
        '''
        Finds the appropriate image based on the action taken
        ''' 
        if act == 'none':
            imgName = "Reload.png"
        elif act == 'all':
            imgName = "Defend.png"
        else:
            imgName = "Attack.png"

        return super().imageCreation(imgName, super().getScreenH() / 10,  super().getScreenW() / 15)

    def timer (self, timer, players = []):
        '''
        Updates the main label with the current time remaining in the round
        '''
        if timer > 0:
            self.topFrameLabel.config(text = "Time Remaining to select an action: " + str(timer))
        elif timer <= 0:
            self.topFrameLabel.config(text = "Time Remaining to select an action: 0" )

            self.eventlog(players)


    def heartDisplay(self, number):
        '''
        Gets the appropriate image based on the HP of the player
        '''
        if number == 'dead' or number <= 0:
            imgName ="0Heart3.png"
        elif number == 1:
            imgName ="1Heart3.png"
        elif number == 2:
            imgName ="2Heart3.png"
        elif number == 3:
            imgName ="3Heart3.png"

        return super().imageCreation(imgName, super().getScreenH() / 20,  super().getScreenW() / 15, "/double07")

    def eventlog(self, players):
        '''
        Prints out a log of all the actions taken in the previous round so players know what is actually happening
        '''
        playerActed = [] # used to ensure there is no double counting of actions
        
        act = 0
        result = 0
        posCounter = 0

        ELFont = super().setFontSize(int (super().getScreenH() / 50))
        textColour = "white"

        for player in players:
            if players[player].get('hp') != "dead": # i.e. if the players are alive 

                curPlayerAction = players[player].get('defend')

                if not(curPlayerAction == "none" or curPlayerAction == "all" or (player in playerActed)): # i.e. if the players actually attacked and haven't already been shown 
                
                    oppAct = players[curPlayerAction].get('defend')
                    playerActed.append(player)

                    if oppAct == 'all': # attack into a block
                        playerActed.append(curPlayerAction)
                        act = "Attack.png"
                        result = "Defend.png"
                        
                    elif oppAct == 'none' or oppAct != player: # attack into a player attacking a different player
                        act = "Attack.png"
                        result = "Heart.png"

                    else: # players attacking one another
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

                    if result != 'none': # shows the result of the attackers attack (i.e. took HP or was blocked)
                        resImg = super().imageCreation(result, int(super().getScreenH() / 20), int(super().getScreenW() / 30))

                        label4 = desktop.Label(super().framelist[3], image = resImg, bg = super().framelist[3]['bg']) 
                        label4.image = resImg 
                        label4.place(anchor = "nw", y = posY, x = 36.5/40 * super().getScreenW() / 2)

                    posCounter += 1
                    self.window.win.update()   
                    desktop.time.sleep(2) # done so eventlog appears one entry at a time

            else: # if the player is dead, we dont need to deal with them
                playerActed.append(player)

        for player in players: # this is done so that attacks show first, then defends that blocked nothing and reloads
            act = ""

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
        desktop.time.sleep(1)  
    
    def standings(self, standings):
        '''
        Displays the end results
        '''
        super().standings(standings)
