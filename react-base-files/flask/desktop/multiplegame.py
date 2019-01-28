import desktop

class MultiGameUI (desktop.DesktopUI):
    timerLabel = ""
    newRound = True

    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        super().setup()
        self.display(obj['players'], obj['valid'], obj['name'], obj['timer'])

    def display(self, players, valid, game, timer):
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


            if players[player].get("hp") > 0:
                label2 = desktop.Label(curFrame, text = "HP: ", image = lives, font = doubleFont, bg = curFrame['bg'], fg = textColour)
                label2.image = lives 
                label2.place(anchor = "nw", y = yPosP + yPosHA, x = xPosPH) 

        # label3 = desktop.Label(curFrame, text = "Act: " , image = "", font = doubleFont, bg = curFrame['bg'], fg = textColour)
        # label3.image = 
        # label3.place(anchor = "e", y = yPosP + yPosHA, x = xPosA)    

        if game == "Simon":
            self.displaySimon(valid, timer)
        elif game == "QuickMaff":
            self.displayQM(valid)
        else:
            self.displayTap(valid)         

    def heartDisplay(self, lives):
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

        return super().imageCreation(imgName, super().getScreenH() / 20,  super().getScreenW() / 10, "/multigame")
            
    
    def displaySimon(self, seq, timer):
        if timer == 20 and self.newRound:
            self.newRound = False
            
            label = desktop.Label(super().framelist[0], text = "Watch the sequence", font = super().setFontSize(super().getScreenH() / 20), bg = super().backgroundC, fg = "white")
            label.place (anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)

            for i in seq:
                super().framelist[3]['bg'] = i.lower()
                desktop.time.sleep(1)
                self.window.win.update()
                super().framelist[3]['bg'] = super().framelist[2]['bg']
                desktop.time.sleep(.5)
                self.window.win.update()

        label.config(text = "Replicate the sequence")
        label.place(anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 10)

        self.displayTimer(timer, "Simon")

        self.window.win.update()

    def displayQM(self, equation):
        pass
    
    def displayTap(self, goal):
        pass

    def displayTimer(self, timer, game):
        timerHeader = desktop.Label(super().framelist[3], text = "Time Remaining: ", fg = 'white', bg = super().backgroundC, font = super().setFontSize(super().getScreenH() / 30))
        timerHeader.place(anchor = "s", x = super().getScreenW() / 4, y = super().getScreenH() * 2/5)

        if timer == 5:
            self.newRound = True

        self.timerLabel = desktop.Label(super().framelist[3], text = str(timer), fg = 'white', bg = super().backgroundC, font = super().setFontSize(super().getScreenH() / 10))
        self.timerLabel.place(anchor = "n", x = super().getScreenW() / 4, y = super().getScreenH() * 2/5)


