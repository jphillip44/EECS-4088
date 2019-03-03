from tkinter import Tk, Frame, Label
from tkinter.font import Font
import sys
import os
import math
import time
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
        '''
        Default setup, completed on first call
        '''

        self.win = Tk()
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        self.deffont = self.setFontSize(int(screenHeight / 35)) 
        self.setscreen(screenWidth, screenHeight)

        # Based on the platform that is currently running the program, there are different ways to set the screen size properly (so it is only on 1 screen)
        if sys.platform == "linux":
            SS = str(screenWidth) + "x" + str(screenHeight)
            self.win.geometry(SS)
        else:
            self.win.state('zoomed') # make maximized (on windows)

        self.win.focus_set() #focus on fullscreen
        self.win.configure(background = self.backgroundC)


    def setup(self):
        '''
        The default setup for all the frames
        '''

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
        '''
        Sets up the dimensions of the screen for later reference (needed mainly for super() calls in other games)
        '''    
        self.screenW = width
        self.screenH = height
    
    def reset (self):
        '''
        Deletes all the frames, and by extension all the widgets within those frames
        '''
        for i in self.framelist:
            i.destroy()
        del self.framelist[0:]
                
    def addFrame (self, fname):
        '''    
        Adds a new frame to the list of frames. This is done so resetting the window is easy
        '''
        self.framelist.append(fname)

    def setFontSize(self, fSize):
        '''
        Ensures all text is the same font style, but the size could be different
        '''
        return Font(family = self.fontFamily, size = int(fSize))

    def getScreenH(self):
        '''
        Returns the height of the window
        '''
        return int (self.screenH)

    def getScreenW(self):
        '''
        Returns the width of the window
        '''
        return int (self.screenW)

    def setWindow (self, window):
        '''
        Ensures all references are to the same window, needed mainly for super() calls
        '''
        self.win = window

    def imageCreation (self, filename, height, width, folder = ""):
        '''
        Opens the image as specified by the name and the location and resizes them as needed
        '''
        path = os.path.join(os.path.relpath(os.path.dirname(__file__)),  '../static/images/' + str(folder))
        imageFolder = Path(path)

        imgFile2 = os.path.join(imageFolder, filename)
        img2 = Image.open(imgFile2)
        img2 = img2.resize((int(width), int(height)))
        resImg = ImageTk.PhotoImage(img2)

        return resImg

    def standings(self, standings):
        '''
        Prints out the player's placements after a game has been completed
        '''

        self.reset()

        topFrame = Frame(height = self.screenH / 10, width = self.screenW, bg= self.backgroundC)
        topFrame.pack_propagate(False) # ensures frame doesnt shrink to size of the wigets added down the road
        topFrame.place(x = 0, y = 0)
        self.addFrame(topFrame)

        label = Label(topFrame, text = "Standings", bg = self.backgroundC, fg = 'white', font = self.setFontSize(self.getScreenH() / 20))
        label.place (anchor = "center", x = self.getScreenW() / 2, y = self.getScreenH() / 20)

        numPlay = len(standings)
        numCol =  math.ceil(numPlay / 8)

        for i in range(numCol):
            print("standings i")
            frame = Frame(height = self.getScreenH() * 9/10, width = self.getScreenW () / numCol, bg = self.backgroundC)
            frame.place(x = i * int(self.getScreenW() / numCol), y = self.getScreenH() / 10)
            for j in range(8):
                if i * 8 + j < numPlay:
                    label = Label(frame, text = str(i * 8 + j + 1) + ". " + str(standings[i * 8 + j]), bg = self.backgroundC, fg = 'white', font = self.setFontSize(self.getScreenH() / (20 * numCol)))
                    label.place(anchor = "nw", y = j * self.getScreenH() / 10, x = self.getScreenW() / numCol / 2 - self.getScreenW() / 15)

            self.addFrame(frame)

        self.win.update()



