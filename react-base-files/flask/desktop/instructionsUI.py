import desktop

class instructionsUI(desktop.DesktopUI):
    
    window = 0

    def __init__(self, ui, obj):
        self.window = ui
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()

        windowFrame = desktop.Frame(height = super().getScreenH(), width = super().getScreenW(), bg = self.backgroundC)
        windowFrame.pack_propagate(False)
        windowFrame.place(x = 0, y = 0)
        super().addFrame(windowFrame)

        instr = desktop.Label(windowFrame, text = obj.state, font = super().setFontSize(super().getScreenH() / 20), bg = super().backgroundC, fg = 'white')
        instr.place(anchor = 'center', x = super().getScreenW() / 2, y = super().getScreenH / 2)

        desktop.time.sleep(20)

