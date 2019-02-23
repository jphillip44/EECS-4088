import desktop

class HotPotatoUI(desktop.DesktopUI):
    window = 0

    def __init__(self, ui, obj):
        self.window = ui
        super().setWindow(self.window.win)
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()
        self.display(obj.get('players'), obj.get('timer'), obj.get('current'), obj.get('next'),  obj.get('max'))

    def setup(self):
        super().setup()
        
        super().framelist[3].destroy
        del super().framelist[3]

        super().framelist[1] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = super().getScreenW() / 3, bg = super().backgroundC)
        super().framelist[1].pack_propagate(False)
        super().framelist[1].place(x = 0, y = self.screenH / 10)

        super().framelist[2] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = super().getScreenW() / 3, bg = super().backgroundC)
        super().framelist[2].pack_propagate(False)
        super().framelist[2].place(x = 2/3 * super().getScreenW(), y = super().getScreenH() / 10)

    def display(self, players, timer, currentP, nextP, max):
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
            explosion = False

            if timer <= 0:
                result = "palm_explosion_Desktop.png"
                explosion = True
            else:
                result = "palm_potato_Desktop.png"
                explosion = False

            resImg = super().imageCreation(result, super().getScreenH() / 12, super().getScreenW() / 12)

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

            if currentP == player:
                label5 = desktop.Label(curFrame, image = resImg, bg = super().backgroundC)
                label5.image = resImg 
                label5.place(anchor = "nw", y = yPos, x = super().getScreenW() / 4) 

        label3 = desktop.Label(super().framelist[0], text = "First to " + str(max) + " points wins!", font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = textColour)
        label3.place(anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        label4 = desktop.Label(super().framelist[0], text = "Next player: " + nextP, font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = textColour)
        label4.place(anchor = "n", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        if explosion:
            desktop.time.sleep(3)

    def standings(self, standings):
        super().standings(standings)
 
    