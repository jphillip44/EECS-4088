import desktop

class MultiGameUI (desktop.DesktopUI):
    window = ""    
    timerLabel = ""
    prevGame = ""

    def __init__(self, ui, obj):
        '''
        Initial setup for the game
        '''
        self.window = ui
        super().setWindow(self.window.win)  
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()
        
        if obj.get('name') == "QuickMaff":
            formula = obj.get('formula')
        else:
            formula = ""

        self.display(obj.get('players'), obj.get('valid'), obj.get('name'), obj.get('timer'), formula, obj.get('maxTimer'))

    def setup(self):
        '''
        Slight modification to the initial display setup
        '''
        super().setup()
        self.timerLabel = desktop.Label(super().framelist[3], text = "", fg = 'white', bg = super().backgroundC, font = super().setFontSize(super().getScreenH() / 10))
        self.timerLabel.place(anchor = "center", x = super().getScreenW() / 4, y = super().getScreenH() * 2/5) 

    def display(self, players, valid, game, timer, formula, maxTimer):
        '''
        Places the players and their HP as well as any other features needed for each of the subgames
        '''
        numPlay = len(players)
        leftPlay = desktop.math.ceil(numPlay / 2)
        rightPlay = desktop.math.floor(numPlay / 2)
        center = int(super().getScreenH() / 2)
        offset = int(super().getScreenH() / 8)
        textColour = "white"
        doubleFont = self.window.setFontSize(int(super().getScreenH() / 50))

        for i, player in enumerate(players):
            lives = self.heartDisplay(players[player].get("hp"))
           
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

            label1 = desktop.Label(curFrame, text = player, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label1.place(anchor = "nw", y = yPosP, x = xPosPH) 


            label2 = desktop.Label(curFrame, text = "HP: ", image = lives, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label2.image = lives 
            label2.place(anchor = "nw", y = yPosP + yPosHA, x = xPosPH) 

            if not (players[player].get('old_correct')):
                imgLast = "xMark.png"
            else:
                imgLast = "Checkmark.png"

            prevAct = super().imageCreation(imgLast, super().getScreenH() / 10, super().getScreenW() / 11, "/multigame")

            label3 = desktop.Label(curFrame, text = "Prev: " , image = prevAct, font = doubleFont, bg = curFrame['bg'], fg = textColour)
            label3.image = prevAct
            label3.place(anchor = "e", y = yPosP + yPosHA, x = xPosA)    

        if game == "Simon":
            self.displaySimon(valid, timer, maxTimer)
        elif game == "QuickMaff":
            self.displayQM(formula, timer)
        else:
            self.displayTap(valid, timer)         

    def heartDisplay(self, lives):
        '''
        Translates HP into the appropriate heart image
        '''
        if lives == 0 or lives == 'dead':
            imgName = "0Heart5.png"
        elif lives == 1:
            imgName = "1Heart5.png"
        elif lives == 2:
            imgName = "2Heart5.png"
        elif lives == 3:
            imgName = "3Heart5.png"
        elif lives == 4:
            imgName = "4Heart5.png"
        else:
            imgName = "5Heart5.png"

        return super().imageCreation(imgName, super().getScreenH() / 20,  super().getScreenW() / 8, "/multigame")
            
    
    def displaySimon(self, seq, timer, maxTimer):
        '''
        Setup for Simon
        '''
        if timer == maxTimer:
            
            label = desktop.Label(super().framelist[0], text = "Watch the sequence", font = super().setFontSize(super().getScreenH() / 20), bg = super().backgroundC, fg = "white")
            label.place (anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)

            for i in seq:
                super().framelist[3]['bg'] = i.lower()
                self.timerLabel['bg'] = i.lower()
                desktop.time.sleep(1)
                self.window.win.update()
                super().framelist[3]['bg'] = super().framelist[2]['bg']
                self.timerLabel['bg'] = super().framelist[2]['bg']
                desktop.time.sleep(.5)
                self.window.win.update()

        label = desktop.Label(super().framelist[0], text = "Replicate the sequence", font = super().setFontSize(super().getScreenH() / 20), bg = super().backgroundC, fg = "white")
        label.place (anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)

        self.displayTimer(timer)

        self.window.win.update()

    def displayQM(self, formula, timer):
        '''
        Setup for QuickMaff
        '''
        label = desktop.Label(super().framelist[0], text = "Solve: " + str(formula), bg = super().backgroundC, fg = 'white', font = super().setFontSize(super().getScreenH() / 20))
        label.place(anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)

        self.displayTimer(timer)
        self.window.win.update()

    
    def displayTap(self, goal, timer):
        '''
        Setup for Tap
        '''
        label = desktop.Label(super().framelist[0], text = "Tap the screen exactly " + str(goal) + " times", font = super().setFontSize(super().getScreenH() / 20), bg = super().backgroundC, fg = "white")
        label.place (anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)
        
        self.displayTimer(timer)
        self.window.win.update()

    def displayTimer(self, timer):
        '''
        Displays the timer as it ticks
        '''
        timerHeader = desktop.Label(super().framelist[3], text = "Time Remaining: ", fg = 'white', bg = super().backgroundC, font = super().setFontSize(super().getScreenH() / 30))
        timerHeader.place(anchor = "s", x = super().getScreenW() / 4, y = super().getScreenH() * 1/5)

        self.timerLabel.configure(text = str(timer))

    def standings(self, standings):
        '''
        Shows the results when game is over
        '''
        super().standings(standings)



