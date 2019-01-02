from tkinter import Tk, mainloop, Frame
import sys, time


class DesktopUI():
    screenW = 0
    screenH = 0
    win = 0
    framelist = []
    players = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]

    def __init__(self):
        self.win = Tk()
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        self.setscreen(screenWidth, screenHeight)
        
        self.win.attributes('-fullscreen', True) #make fullscreen
        self.win.focus_set() #focus on fullscreen
        self.win.configure(background = '#001a35')

        self.win.bind("<Escape>", lambda e: self.win.quit())        
    
    def setscreen(self, width, height):
        self.screenW = width
        self.screenH = height
    
    def reset (self):
        for i in self.framelist:
            i.destroy()
        del self.framelist[0:]
                
    def addFrame (self, fname):
        self.framelist.append(fname)


