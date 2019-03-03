import desktop

class MatchingUI(desktop.DesktopUI):
    topFrameLabel = "" # so timer ticks are displayed cleanly
    nextLabel = ""  # so next player is displayed cleanly

    prevCursor = [0, 0] # needed for moving the cursor properly, and quickly

    # for board size
    columns = 0
    rows = 0

    cardTaken = False # determines if, when a card is selected, it is the first or second card picked
    cardTakenPos = [0, 0] # needed for putting the first card selected back after the two cards are picked

    def __init__(self, ui, obj, columns, rows):
        '''
        The inital setup for this game
        '''
        super().setWindow(ui.win)
        super().setscreen(ui.screenW, ui.screenH)
        super().reset()
        self.setup()

        self.topFrameLabel = desktop.Label (super().framelist[0], text = "init", bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        self.topFrameLabel.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        self.columns = columns
        self.rows = rows

        self.display(obj.get('gameBoard'), obj.get('next'), obj.get('cursor'), obj.get('timer'))

    def setup(self): 
        '''
        Slight modifcation to the default setup to better suit this game
        '''

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
        '''
        Shows all the cards, the timer, the current player and the next player
        '''
        for i in range (self.rows):
            for j in range (self.columns):
        
                if cursor == [i, j]:
                    self.updateCard(boardState[i, j], [i, j], True)

                else:
                    self.updateCard(boardState[i, j], [i, j], False)
        
        self.displayTimer(timer, nextP[0])

        self.nextLabel = desktop.Label (super().framelist[2], text = "Next Player: " + nextP[1], bg = super().backgroundC, font = super().setFontSize(int((super().getScreenH() / 30))), fg = 'white')
        self.nextLabel.place(anchor = "center", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

    def nextPlayer (self, next):
        '''
        Updates the label telling the players who's turn is next
        '''
        self.nextLabel.configure(text = "Next Player: " + str(next))
    
    def displayTimer (self, timer, nextPlayer):
        '''
        Updates the timer on screen as it ticks and shows the player that is to select a card
        '''
        self.topFrameLabel.config(text = str(nextPlayer) + " select a card for the board. Time Remaining: " + str(timer))

    def cursorMove (self, cursor, boardState):
        '''
        Unhightlights where the cursor was, highlights where the cursor now is
        '''

        self.updateCard(boardState[self.prevCursor[0], self.prevCursor[1]], [self.prevCursor[0], self.prevCursor[1]], False)

        self.updateCard(boardState[cursor[0], cursor[1]], [cursor[0], cursor[1]], True)

        self.prevCursor = cursor

    def getCardImgName (self, name):
        '''
        Gets the file name of the card based on what is to be displayed to the players
        '''
        if str(name) == "XX":
            cardSuffix = "back"
        else:
            cardSuffix = str(name)

        cardFileName = "card_" + cardSuffix +".png"

        return cardFileName

    def updateCard (self, card, position, highlighted):
        '''
        Displays the cards for the board
        '''
        if highlighted: # i.e. cursor is on that card
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
