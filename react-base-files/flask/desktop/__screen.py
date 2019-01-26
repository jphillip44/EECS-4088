from tkinter import Tk, Frame
from tkinter.font import Font
import sys
import os
from pathlib import Path
from PIL import Image, ImageTk

class DesktopUI():
    screenW = 0
    screenH = 0
    win = 0
    framelist = []
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
            self.win.state('zoomed') # make maximized (on windows)

        # self.win.attributes('-fullscreen', True) #make fullscreen
        self.win.focus_set() #focus on fullscreen
        self.win.configure(background = self.backgroundC)

        self.win.bind("<Escape>", lambda e: self.win.quit())    

    def setup(self):
        topFrame = Frame(height = self.screenH / 10, width = self.screenW, bg= self.backgroundC)
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.place(x = 0, y = 0)
        self.addFrame(topFrame)

        leftFrame = Frame(height = (self.screenH / 10) * 8, width = self.screenW / 4, bg = self.backgroundC)
        leftFrame.pack_propagate(False)
        leftFrame.place(x = 0, y = self.screenH / 10)
        self.addFrame(leftFrame)

        rightFrame = Frame(height = (self.screenH / 10) * 8, width = self.screenW / 4, bg =  self.backgroundC)
        rightFrame.pack_propagate(False)
        rightFrame.place(x = (self.screenW / 4) * 3, y = self.screenH / 10)
        self.addFrame(rightFrame)

        centerFrame = Frame(height = (self.screenH / 10) * 8, width = (self.screenW / 4) * 2, bg =  self.backgroundC)
        centerFrame.pack_propagate(False)
        centerFrame.place(x = (self.screenW / 4), y = self.screenH / 10)
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

    def imageCreation (self, filename, height, width, folder = ""):
        path = os.path.join(os.path.relpath(os.path.dirname(__file__)),  '../../public/images/' + str(folder))
        imageFolder = Path(path)

        imgFile2 = os.path.join(imageFolder, filename)
        img2 = Image.open(imgFile2)
        img2 = img2.resize((int(width), int(height)))
        resImg = ImageTk.PhotoImage(img2)

        return resImg
        

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @screen.deleter
    def screen(self):
        del self.__screen   


