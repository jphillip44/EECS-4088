import socket
import qrcode
import desktop

class PlayerUI (desktop.DesktopUI):
    window = 0 
       
    def __init__(self, ui):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()
        self.setup()

    def setup(self):
        def get_ip_address():
            '''
            Obtains the IP address for all platforms, so players know where to connect and for the generation of the QR code
            '''
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]

        super().setup()

        super().framelist[1] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = super().getScreenW() / 3, bg = super().backgroundC)
        super().framelist[1].pack_propagate(False)
        super().framelist[1].place(x = 0, y = super().getScreenH() / 10)

        super().framelist[2] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = super().getScreenW() / 3, bg =  super().backgroundC)
        super().framelist[2].pack_propagate(False)
        super().framelist[2].place(x = (super().getScreenW() / 3) * 2, y = super().getScreenH() / 10)

        super().framelist[3] = desktop.Frame(height = (super().getScreenH() / 10) * 8, width = (super().getScreenW() / 3), bg =  super().backgroundC)
        super().framelist[3].pack_propagate(False)
        super().framelist[3].place(x = (super().getScreenW() / 3), y = super().getScreenH() / 10)

        IP = get_ip_address()

        label1 = desktop.Label(super().framelist[0], text="Go to http://" + str(IP) + ":5000 or scan the below code to enter the lobby", bg = super().framelist[0]['bg'], fg = "white", font = self.window.deffont)
        label1.place(x = super().getScreenW() / 2, y = super().getScreenH() / 20, anchor = 'center')

        img = qrcode.make("http://" + str(IP) + ":5000")

        resImg = desktop.ImageTk.PhotoImage(img)

        label2 = desktop.Label(super().framelist[3], image = resImg)
        label2.image = resImg # needed so images aren't garbage collected, thus not showing up
        label2.place(anchor = 'center', x = super().getScreenW() / 6, y = super().getScreenH() * 2/5)

        
    def PlayerShow (self, players):
        '''
        List out all the players that are currently connected
        '''

        numPlay = len(players)
        leftPlay = desktop.math.ceil(numPlay / 2)
        rightPlay = desktop.math.floor(numPlay / 2)
        center = int(super().getScreenH() / 2)
        offset = int(super().getScreenH() / 10)
        textColour = "white"
         
        self.window.reset()
        self.setup()

        #left player list
        if (leftPlay % 2) == 1:
            for i in range(leftPlay):
                label = desktop.Label(super().framelist[1], text = players[2 * i], font = self.window.deffont, bg = super().framelist[1]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - ((((leftPlay - 1) / 2) - i + 1) * offset), x = super().getScreenW() / 64)
        else:
            for i in range(leftPlay):
                label = desktop.Label(super().framelist[1], text = players[2 * i], font = self.window.deffont, bg = super().framelist[1]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - (leftPlay / 2 + .5 - i) * offset, x = super().getScreenW() / 64) 

        #right player list
        if (rightPlay % 2) == 1:
            for i in range(rightPlay):
                label = desktop.Label(super().framelist[2], text = players[2 * i + 1], font = self.window.deffont, bg = super().framelist[2]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - ((((rightPlay - 1) / 2) - i + 1) * offset), x = super().getScreenW() / 64)
        else:
            for i in range(rightPlay):
                label = desktop.Label(super().framelist[2], text = players[2 * i + 1], font = self.window.deffont, bg = super().framelist[2]['bg'], fg = textColour)
                label.place(anchor = "w", y = center - (rightPlay / 2 + .5 - i) * offset, x = super().getScreenW() / 64) 

