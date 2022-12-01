import pafy
from pytube import YouTube
import requests
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

class Sampl:
    def checkPath(self):
        if (self.path == "" or (os.path.exists(self.path) == False)):
            return False
        return True

    def initRoot(self):
        self.root= tk.Tk()
        self.root.resizable(True, True)
        self.root.title('Sampl')
        self.root.geometry('900x500+50+50')
        self.root.iconbitmap('./assets/logo.ico')

    def initPath(self):
        #add check
        f = open("./data/path.txt", "r")
        self.path = f.read()
        f.close()
    
    def savePath(self):
        if (self.checkPath()):
            f = open("./data/path.txt", "w")
            f.write(self.path)
            f.close()
    
    def run(self):
        if (self.root is not None):
            self.root.mainloop()

    def openDirDialog(self):
        self.path =  askdirectory(title='Select the folder to store the samples') # shows dialog box and return the path
        if (self.checkPath()):
            self.pathLabel.config(text = self.path)

    def initElements(self):
        self.folder_icon= tk.PhotoImage(file='./assets/folder.png')
        self.directoryButton = ttk.Button(
            self.root,
            image= self.folder_icon,
            command= self.openDirDialog
        )

        self.pathLabel = tk.Label(
            self.root, text=self.path,

            font=("Arial Nova", 14))

        self.urlEntry = ttk.Entry(self.root)
        self.urlEntry.focus()

        self.downloadButton= ttk.Button(
                self.root,
                text="Download",
                command=self.download
            )
    
    def showWidgets(self):
        self.directoryButton.pack(
            anchor=tk.NE,
            ipadx=5,

            ipady=5,

            expand=False
            )

        self.pathLabel.pack(anchor=tk.NE)

        self.urlEntry.pack(expand=False, anchor=tk.CENTER, padx=10, pady=5, ipadx= 10, ipady = 10)
        
        self.downloadButton.pack(anchor=tk.NE)
    

    def checkLink(self):
        try :
            request = requests.get(self.url)
            return request.status_code == 200
        except:
            return False

    def download(self):
        if (self.checkPath()):
            self.url = self.urlEntry.get()
            if (self.checkLink()):
                yt = YouTube(str(self.url))
                
                fileName = self.path + '/' + yt.title + '.mp3'

                if (os.path.exists(fileName) == False):
                    # extract only audio
                    video = yt.streams.filter(only_audio=True).first()
                    
                    # download the file
                    out_file = video.download(output_path=self.path)

                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'

                    try:
                        os.rename(out_file, new_file)
                        messagebox.showinfo("Yessir", "Successfully downloaded")
                    
                    except:
                        messagebox.showinfo("Unknown error", "File not downloaded, sorry")
                
                else:
                    messagebox.showinfo("File already exists", "File already exists")
            else:
                messagebox.showinfo("Invalid url", "Invalid url")

    def __init__(self):
        self.url =""
        self.path= "" 
        self.initPath()
        self.initRoot()
        self.initElements()
        self.showWidgets()

    def __del__(self):
        self.savePath()
    
def main ():
    app = Sampl()

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        app.run()

main()

