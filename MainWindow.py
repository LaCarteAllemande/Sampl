import tkinter as tk


from tkinter import *


from tkinter import messagebox


from tkinter.filedialog import askdirectory



import Storage


import Downloader


import DownloadWindow


import threading




BG_COLOR = "#001833"


TEXT_COLOR = "white"


class MainWindow:


    def __init__(self):


        self.url ="" 


        self.downloadWindows = []


        self.path = "" 


        self.path = Storage.GetSamplePath() #why do I need to declare path a second time ??


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


        self.root['background']=BG_COLOR


        self.root.resizable(False, False)


        self.root.title('Sampl')


        self.root.geometry('550x300')


        self.root.iconbitmap('./assets/logo.ico')
    


    #open a dialog box to choose a directory to store the samples


    def openDirDialog(self):


        path =  askdirectory(title='Select the folder to store the samples') # shows dialog box and return the path


        if (path != ""):


            if (Data.CheckPath(path)):
                self.path = path


                self.pathLabel.config(text = self.path)



    #create the GUI's components


    def createGUIcomponents(self):


        self.folder_icon= tk.PhotoImage(file='./assets/folder.png').subsample(2, 2)
        


        self.directoryButton = Button(self.root,image= self.folder_icon,command= self.openDirDialog)


        self.pathLabel = tk.Label(self.root, text="Samples directory: " + self.path , font=("Arial Nova", 12), bg=BG_COLOR, fg=TEXT_COLOR)


        self.entryFrame = Frame(self.root, background=TEXT_COLOR)


        self.urlEntry = Entry(self.root,  bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)


        self.urlEntry.focus()


        self.btnFrame = Frame(self.root, background=TEXT_COLOR)


        self.downloadButton= Button(self.root,text="Download",command= self.download, font=("Arial Nova", 12), bg=BG_COLOR, fg=TEXT_COLOR, cursor="hand2", borderwidth= 0)
    


    #display the GUI's components


    def showGUIcomponents(self):


        self.directoryButton.place(relx=0.96, rely=0.03, relwidth=0.06, relheight=0.1, anchor=NE)


        self.pathLabel.place(relx=0.97, rely=0.15, anchor=NE)


        self.urlEntry.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.1, anchor=CENTER)


        self.entryFrame.place(relx=0.5, rely=0.5, relwidth=0.705, relheight=0.105, anchor=CENTER)


        self.downloadButton.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.1, anchor=CENTER)


        self.btnFrame.place(relx=0.5, rely=0.7, relwidth=0.21, relheight=0.12, anchor=CENTER)
        


    def download(self):
        if (Downloader.CheckLink(self.urlEntry.get())):
            if (Storage.CheckPath(self.path)):
                self.newDownloadThread()
                self.urlEntry.delete(0,END)
                self.urlEntry.insert(0, "")

            else:

                messagebox.showinfo("Invalid path", "Invalid download path")
        else:
            messagebox.showinfo("Invalid url", "Invalid url")

    #starts a new download thread
    def newDownloadThread(self):
        self.downloadWindows.append(DownloadWindow.DownloadWindow(self.root, self.path, self.urlEntry.get()))
        parallel = threading.Thread(target=self.downloadWindows[-1].download, args=(self.urlEntry.get(), self.path))
        parallel.start()

    def __del__(self):
        Storage.SavePath(self.path)