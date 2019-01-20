import desktop

class HotPotatoUI(desktop.DesktopUI):
    window = 0


    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        super().setup()
        self.display(obj['players'], obj['timer'], obj['next'])

    def display(self, players, timer, nextP):
        numPlay = len(players)
        leftPlay = desktop.math.ceil(numPlay / 2)
        rightPlay = desktop.math.floor(numPlay / 2)
        center = int(super().getScreenH() / 2)
        offset = int(super().getScreenH() / 10)
        print(super().getScreenH())
        textColour = "white"

        for i, player in enumerate(players):   
            playerScore = players[player].get("score")
            xPos = super().getScreenW() / 32
            yPos = 0 
            fontSize = super().setFontSize(int((super().getScreenH()) / 30))
            curFrame = super().framelist[2]
            sleep = False

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
            label2.place (anchor = "ne", x = super().getScreenW() / 4 - xPos, y = yPos)

        label3 = desktop.Label(super().framelist[0], text = "First to x points wins!", font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = textColour)
        label3.place(anchor = "s", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        label4 = desktop.Label(super().framelist[0], text = "Next player: " + nextP, font = super().setFontSize(int((super().getScreenH() / 30))), bg = super().backgroundC, fg = textColour)
        label4.place(anchor = "n", x = super().getScreenW() / 2, y = super().getScreenH() / 20)

        path = desktop.os.path.join(desktop.os.path.relpath(desktop.os.path.dirname(__file__)),  '../../public/images')
        imageFolder = desktop.Path(path)

        if timer <= 0:
            result = "palm_explosion_Desktop.png"
            explosion = True
        else:
            result = "palm_potato_Desktop.png"
            explosion = False

        imgFile2 = desktop.os.path.join(imageFolder, result)
        img2 = desktop.Image.open(imgFile2)
        img2 = img2.resize((int(self.window.screenW / 2.5), int(self.window.screenH / 2.5)))
        resImg = desktop.ImageTk.PhotoImage(img2)

        label5 = desktop.Label(super().framelist[3], image = resImg, bg = super().backgroundC)
        label5.image = resImg 
        label5.place(anchor = "center", y = 4 * super().getScreenH() / 10, x = super().getScreenW() / 4) 

        self.window.win.update()

        if explosion:
            desktop.time.sleep(3)

    