import desktop

class instructionsUI(desktop.DesktopUI):
    
    window = 0

    def __init__(self, ui, instructions):
        self.window = ui
        super().setWindow(self.window)
        super().setscreen(self.window.screenW, self.window.screenH)
        super().reset()

        windowFrame = desktop.Frame(height = super().getScreenH(), width = super().getScreenW(), bg = self.backgroundC)
        windowFrame.pack_propagate(False)
        windowFrame.place(x = 0, y = 0)
        super().addFrame(windowFrame)

        instr = desktop.Label(windowFrame, text = instructions, font = super().setFontSize(super().getScreenH() / 30), bg = super().backgroundC, fg = 'white', justify = 'left', wraplength = super().getScreenW())
        instr.place(anchor = 'center', x = super().getScreenW() / 2, y = super().getScreenH() / 2)

