


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import Data
import Downloader


class Sampl:

    def __init__(self):
        self.url ="" 
        self.path = "" 
        self.path = Data.GetSamplePath() #why do I need to declare path a second time ??
        self.createRootWindow()
        self.createGUIcomponents()
        self.showGUIcomponents()
    
    #run 
    def run(self):
        if (self.root is not None):
            self.root.mainloop()
    
    #create the main GUI (root window)
    def createRootWindow(self):
        self.root= tk.Tk()
        self.root.resizable(False, False)
        self.root.title('Sampl')
        self.root.geometry('550x300')
        self.root.iconbitmap('./assets/logo.ico')
    
    #open a dialog box to choose a directory to store the samples
    def openDirDialog(self):
        self.path =  askdirectory(title='Select the folder to store the samples') # shows dialog box and return the path
        if (Data.CheckPath(self.path)):
            self.pathLabel.config(text = self.path)

    #create the GUI's components
    def createGUIcomponents(self):
        self.folder_icon= tk.PhotoImage(file='./assets/folder.png').subsample(2, 2)
        self.directoryButton = Button(self.root,image= self.folder_icon,command= self.openDirDialog)
        self.pathLabel = tk.Label(self.root, text="Samples directory :" + self.path , font=("Arial Nova", 10))
        self.urlEntry = Entry(self.root)
        self.urlEntry.focus()
        self.downloadButton= Button(self.root,text="Download",command= self.dwl)
    
    #display the GUI's components
    def showGUIcomponents(self):
        self.directoryButton.place(relx=0.96, rely=0.03, relwidth=0.06, relheight=0.1, anchor=NE)
        self.pathLabel.place(relx=0.97, rely=0.15, anchor=NE)
        self.urlEntry.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.1, anchor=CENTER)
        self.downloadButton.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.1, anchor=CENTER)

    #starts the download
    def dwl(self):
        Downloader.Download(self.urlEntry.get(), self.path)
    def __del__(self):
        Data.SavePath(self.path)