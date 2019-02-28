import desktop

class MatchingUI(desktop.DesktopUI):
    window = 0

    topFrameLabel = ""

    prevCursor = [0, 0]

    columns = 0
    rows = 0

    cardTaken = False
    cardTakenPos = [0, 0]

    def __init__(self, ui, obj, columns, rows):
        self.window = ui
        super().setWindow(self.window.win)
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()

        self.topFrameLabel = desktop.Label (super().framelist[0], text = "init", bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        self.topFrameLabel.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        self.columns = columns
        self.rows = rows

        self.display(obj.get('gameBoard'), obj.get('next'), obj.get('cursor'), obj.get('timer'))

    def setup(self): 
        super().setup()
        
        for i in range(2):
            super().framelist[1].destroy
            del super().framelist[1]

        super().framelist[1] = desktop.Frame(height = (super().getScreenH() / 10) * (self.columns * 2 / 8), width = super().getScreenW() * self.rows / 10, bg = super().backgroundC)
        super().framelist[1].pack_propagate(False)
        super().framelist[1].place(anchor = 'center', x = super().getScreenW() / 2, y = super().getScreenH() / 2)

        bottomFrame = desktop.Frame(height = super().getScreenH() / 10, width = super().getScreenW(), bg = super().backgroundC)
        bottomFrame.pack_propagate(False)
        bottomFrame.place (y = super().getScreenH() * 8/10, x = 0)
        super().addFrame(bottomFrame)


    def display(self, boardState, nextP, cursor, timer):
        for i in range (self.rows):
            for j in range (self.columns):
        
                if cursor == [i, j]:
                    self.updateCard(boardState[i, j], [i, j], True)

                else:
                    self.updateCard(boardState[i, j], [i, j], False)
        
        self.displayTimer(timer, nextP[0])

        label2 = desktop.Label (super().framelist[2], text = "Next Player: " + nextP[1], bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        label2.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)
    
    def displayTimer (self, timer, nextPlayer):
        self.topFrameLabel.config(text = str(nextPlayer) + " select a card for the board. Time Remaining: " + str(timer))

    def cursorMove (self, cursor, boardState):
        self.updateCard(boardState[self.prevCursor[0], self.prevCursor[1]], [self.prevCursor[0], self.prevCursor[1]], False)

        self.updateCard(boardState[cursor[0], cursor[1]], [cursor[0], cursor[1]], True)

        self.prevCursor = cursor

    def getCardImgName (self, name):
        if str(name) == "XX":
            cardSuffix = "back"
        else:
            cardSuffix = str(name)

        cardFileName = "card_" + cardSuffix +".png"

        return cardFileName

    def updateCard (self, card, position, highlighted):
        if highlighted:
            cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC, highlightthickness = 10)
            cardImage = super().imageCreation(self.getCardImgName(card), super().getScreenH() / 5 - 45, super().getScreenW() / 10 - 45, "/match/cards")

            cardFrame.pack_propagate(False)
            cardFrame.grid(row = position[0], column = position[1], padx = 10, pady = 10) 

            label2 = desktop.Label(cardFrame, image = cardImage, bg = super().backgroundC)
            label2.img = cardImage
            label2.place(x = 0, y = 0)
        else:
            cardFrame = desktop.Frame(super().framelist[1], height = super().getScreenH() / 5 - 20, width = super().getScreenW() / 10 - 20, bg = super().backgroundC)
            cardImage = super().imageCreation(self.getCardImgName(card), super().getScreenH() / 5 - 20, super().getScreenW() / 10 - 20, "/match/cards")

            cardFrame.pack_propagate(False)
            cardFrame.grid(row = position[0], column = position[1], padx = 10, pady = 10) 

            label = desktop.Label(cardFrame, image = cardImage, bg = super().backgroundC)
            label.img = cardImage
            label.place(x = 0, y = 0)

    def standings(self, standings):
        super().standings(standings)
