import desktop

class MatchingUI(desktop.DesktopUI):
    window = 0

    topFrameLabel = ""

    prevCursor = [0, 0]

    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()

        self.topFrameLabel = desktop.Label (super().framelist[0], text = "init", bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        self.topFrameLabel.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        self.display(obj['gameBoard'], obj['next'], obj['cursor'], obj['timer'])

    def setup(self): 
        super().setup()
        
        for i in range(2):
            super().framelist[1].destroy
            del super().framelist[1]

        super().framelist[1] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = super().getScreenW(), bg = super().backgroundC)
        super().framelist[1].pack_propagate(False)
        super().framelist[1].place(x = 0, y = super().getScreenH() / 10)

        bottomFrame = desktop.Frame(height = super().getScreenH() / 10, width = super().getScreenW(), bg = super().backgroundC)
        bottomFrame.pack_propagate(False)
        bottomFrame.place (y = super().getScreenH() * 9/10, x = 0)
        super().addFrame(bottomFrame)

    def display(self, boardState, nextP, cursor, timer):
        for i in range (4):
            for j in range (10):
                cardFilename = self.getCardImgName(boardState[i, j])

                if cursor == [i, j]:
                    cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC, highlightthickness = 10)
                    cardImage = super().imageCreation(cardFilename, super().getScreenH() / 5 - 45, super().getScreenW() / 10 - 45, "/match/cards")
                else:
                    cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC)
                    cardImage = super().imageCreation(cardFilename, super().getScreenH() / 5 - 20, super().getScreenW() / 10 - 20, "/match/cards")
               
                cardFrame.pack_propagate(False)
                cardFrame.grid(row = i, column = j, padx = 10, pady = 10) 

                label = desktop.Label(cardFrame, image = cardImage, bg = super().backgroundC)
                label.img = cardImage
                label.place(x = 0, y = 0)
        
        self.displayTimer(timer, nextP[0])

        label2 = desktop.Label (super().framelist[2], text = "Next Player: " + nextP[1], bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        label2.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)
    
    def displayTimer (self, timer, nextPlayer):
        self.topFrameLabel.config(text = str(nextPlayer) + " select a card for the board. Time Remaining: " + str(timer))

    def cursorMove (self, cursor, boardState):
        cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC)
        cardImage = super().imageCreation(self.getCardImgName(boardState[self.prevCursor[0], self.prevCursor[1]]), super().getScreenH() / 5 - 20, super().getScreenW() / 10 - 20, "/match/cards")

        cardFrame.pack_propagate(False)
        cardFrame.grid(row = self.prevCursor[0], column = self.prevCursor[1], padx = 10, pady = 10) 

        label = desktop.Label(cardFrame, image = cardImage, bg = super().backgroundC)
        label.img = cardImage
        label.place(x = 0, y = 0)

        cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC, highlightthickness = 10)
        cardImage = super().imageCreation(self.getCardImgName(boardState[cursor[0], cursor[1]]), super().getScreenH() / 5 - 45, super().getScreenW() / 10 - 45, "/match/cards")

        cardFrame.pack_propagate(False)
        cardFrame.grid(row = cursor[0], column = cursor[1], padx = 10, pady = 10) 

        label2 = desktop.Label(cardFrame, image = cardImage, bg = super().backgroundC)
        label2.img = cardImage
        label2.place(x = 0, y = 0)

        self.prevCursor = cursor

    def getCardImgName (self, name):
        if str(name) == "XX":
            cardSuffix = "back"
        else:
            cardSuffix = str(name)

        cardFileName = "card_" + cardSuffix +".png"

        return cardFileName

    def standings(self, standings):
        super().standings(standings)
        self.window.win.update()
        desktop.time.sleep(10)  