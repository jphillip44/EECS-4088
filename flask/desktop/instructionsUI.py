import desktop

class instructionsUI(desktop.DesktopUI):

    def __init__(self, ui, instructions):
        '''
        Will show the insturctions for the game the players are about to play
        '''
        self.window = ui
        super().setWindow(ui.win)
        super().setscreen(ui.screenW, ui.screenH)
        super().reset()

        windowFrame = desktop.Frame(height = super().getScreenH(), width = super().getScreenW(), bg = self.backgroundC)
        windowFrame.pack_propagate(False)
        windowFrame.place(x = 0, y = 0)
        super().addFrame(windowFrame)

        instr = desktop.Label(windowFrame, text = instructions, font = super().setFontSize(super().getScreenH() / 30), bg = super().backgroundC, fg = 'white', justify = 'left', wraplength = super().getScreenW())
        instr.place(anchor = 'center', x = super().getScreenW() / 2, y = super().getScreenH() / 2)

