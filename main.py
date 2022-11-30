import pafy
from pytube import YouTube
import requests
import os
import tkinter as tk
from tkinter import ttk

from tkinter.filedialog import askdirectory


class Sampl:
  def __init__(self):
    self.root = tk.Tk()
    self.directoryButton = dirButton= ttk.Button(
        root,
        image=folder_icon,
        command=openDirDialog
    )
    self.directoryLabel =
    self.downloadButton = 
    self.urlEntry = age
    


path  =""
global url

def checkPath():

    if (path == "" or (os.path.exists(path) == False)):

        return False

    return True



def initPath():

    global path
    f = open("./data/path.txt", "r")
    path = f.read()
    f.close()
  

def savePath():

    if (checkPath()):

        f = open("./data/path.txt", "w")

        f.write(path)
        f.close()



def openDirDialog():

    global path
    path =  askdirectory(title='Select the folder to store the samples') # shows dialog box and return the path




def checkLink():

    request = requests.get(url)

    return request.status_code == 200


def download():
    if (checkPath()):
        global url 
        url =  "https://www.youtube.com/watch?v=eACohWVwTOc"
        if (checkLink()):
            yt = YouTube(str(url))
            
            # extract only audio
            video = yt.streams.filter(only_audio=True).first()
            
            # download the file
            out_file = video.download(output_path=path)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'

            try:
                os.rename(out_file, new_file)
                print(yt.title + " has been successfully downloaded.")
            
            except:
                print("File not downloaded")

def main ():

    initPath()

    #create the window
    root = 
    root.resizable(False, False)

    root.title('Sampl')

    root.geometry('300x200+50+50')

    root.iconbitmap('./assets/logo.ico')


    #create folder button

    folder_icon= tk.PhotoImage(file='./assets/folder.png')

    



    actualPathlabel = tk.Label(

        root, text=path,

        font=("Arial Nova", 14))


    urlEntry = ttk.Entry(root)

    urlEntry.focus()


    downloadButton= ttk.Button(

        root,
        text="Download",
        command=download
    )


    #show elements
    

    dirButton.pack(

        ipadx=5,

        ipady=5,

        expand=False
        )

    actualPathlabel.pack()

    urlEntry.pack(fill='x', expand=True)
    
    downloadButton.pack()


    try:

        from ctypes import windll


        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        root.mainloop()



    savePath()



main()

