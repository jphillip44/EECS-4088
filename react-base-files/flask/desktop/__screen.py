from tkinter import Tk, Frame
from tkinter.font import Font
import sys
#from colour import Color

class DesktopUI():
    screenW = 0
    screenH = 0
    win = 0
    framelist = []
    #top = Color("black")
    #bottom = Color("#001a35")
    #colours = list(top.range_to(bottom, 100))
    backgroundC = "#001a35"
    deffont = 0
    fontFamily = "Times"

    def __init__(self):
        self.win = Tk()
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        self.deffont = self.setFontSize(int(screenHeight / 35)) 
        self.setscreen(screenWidth, screenHeight)

        if sys.platform == "linux":
            SS = str(screenWidth) + "x" + str(screenHeight)
            self.win.geometry(SS)
        else:
            self.win.state('zoomed') #make maximized (on windows)

        #self.win.attributes('-fullscreen', True) #make fullscreen
        self.win.focus_set() #focus on fullscreen
        self.win.configure(background = self.backgroundC)

        self.win.bind("<Escape>", lambda e: self.win.quit())    

    def setup(self):
        topFrame = Frame(height = self.screenH / 10, width = self.screenW, bg= self.backgroundC)
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.place(x = 0, y = 0)
        self.topframe = topFrame
        self.addFrame(topFrame)

        leftFrame = Frame(height = (self.screenH / 10) * 8, width = self.screenW / 4, bg = self.backgroundC)
        leftFrame.pack_propagate(False)
        leftFrame.place(x = 0, y = self.screenH / 10)
        self.leftframe = leftFrame
        self.addFrame(leftFrame)

        rightFrame = Frame(height = (self.screenH / 10) * 8, width = self.screenW / 4, bg =  self.backgroundC)
        rightFrame.pack_propagate(False)
        rightFrame.place(x = (self.screenW / 4) * 3, y = self.screenH / 10)
        self.rightframe = rightFrame
        self.addFrame(rightFrame)

        centerFrame = Frame(height = (self.screenH / 10) * 8, width = (self.screenW / 4) * 2, bg =  self.backgroundC)
        centerFrame.pack_propagate(False)
        centerFrame.place(x = (self.screenW / 4), y = self.screenH / 10)
        self.centerframe = centerFrame
        self.addFrame(centerFrame)   
      
    def setscreen(self, width, height):
        self.screenW = width
        self.screenH = height
    
    def reset (self):
        for i in self.framelist:
            i.destroy()
        del self.framelist[0:]
                
    def addFrame (self, fname):
        self.framelist.append(fname)

    def setFontSize(self, fSize):
        return Font(family = self.fontFamily, size = fSize)

    def getScreenH(self):
        return int (self.screenH)

    def getScreenW(self):
        return int (self.screenW)

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @screen.deleter
    def screen(self):
        del self.__screen   


