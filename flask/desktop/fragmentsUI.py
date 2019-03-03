import desktop

class FragmentsUI (desktop.DesktopUI):
    timerLabel = ""

    def __init__(self, ui, obj):
        '''
        Initial setup of the window
        '''
        super().setscreen(ui.screenW, ui.screenH)
        super().setWindow(ui.win)
        super().reset()
        self.setup(obj.get('maxTimer'))
        self.display(obj.get('players'), obj.get('timer'), obj.get('display'))
    
    def setup(self, timer):
        '''
        Slight modification of the default setup
        '''

        super().setup()

        self.timerLabel = desktop.Label(super().framelist[0], text = "Time Remaining: " + str(timer) , font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = 'white')
        self.timerLabel.place(anchor = "n", x = super().getScreenW() / 2, y = super().getScreenH() / 20)


    def display(self, players, timer, fragment):
        '''
        Displays all the players, their current score and the image they need a fragment from
        '''

        numPlay = len(players)
        leftPlay = desktop.math.ceil(numPlay / 2)
        rightPlay = desktop.math.floor(numPlay / 2)
        center = int(super().getScreenH() / 2)
        offset = int(super().getScreenH() / 10)
        textColour = "white"

        for i, player in enumerate(players):   
            playerScore = players[player].get("score")
            xPos = super().getScreenW() / 32
            yPos = 0
            yPosS = super().getScreenW() / 40 
            fontSize = super().setFontSize(int((super().getScreenH()) / 40))
            curFrame = super().framelist[2]

            if i < leftPlay:
                curFrame = super().framelist[1]
                if leftPlay % 2 == 1:
                    yPos = center - ((((leftPlay - 1) / 2) - i + 1) * offset)
                else:
                    yPos = center - (leftPlay / 2 + .5 - i) * offset
            else:
                if rightPlay % 2 == 1:
                    yPos = center - ((((rightPlay - 1) / 2) - (i - leftPlay) + 1) * offset)
                else:
                    yPos = center - (rightPlay / 2 + .5 - (i - leftPlay)) * offset
            
            label1 = desktop.Label(curFrame, text = player, font = fontSize, bg = super().backgroundC, fg = textColour)
            label1.place(anchor = "nw", x = xPos, y = yPos)

            label2 = desktop.Label(curFrame, text = "Score: " + str (playerScore), font = fontSize, bg = super().backgroundC, fg = textColour)
            label2.place (anchor = "nw", x = xPos, y = yPos + yPosS)

        label3 = desktop.Label(super().framelist[0], text = "Find the fragment that matches the image", font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = textColour)
        label3.place(anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        fragmentImg = super().imageCreation(fragment, super().getScreenW() / 2.5,  super().getScreenW() / 2.5, "/fragments")

        label5 = desktop.Label(super().framelist[3], image = fragmentImg, bg = super().backgroundC)
        label5.img = fragmentImg
        label5.place(anchor = "center", y = super().getScreenH() * (2 / 5), x = super().getScreenW() / 4)

    def timer (self, timer):
        '''
        Displays the amount of time left in the round
        '''

        if timer >= 0:
            self.timerLabel.configure(text = "Time Remaining: " + str(round(timer)))
        else:
            self.timerLabel.configure(text = "Time Remaining: 0")

    def standings(self, standings):
        '''
        Displays the end results of the game
        '''
        super().standings(standings)
