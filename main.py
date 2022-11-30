import pafy
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory


global path

def initPath():
    global path
    f = open("./data/path.txt", "r")
    path = f.read()

initPath()

def openDirDialog():
    global path
    path =  askdirectory(title='Select the folder to store the samples') # shows dialog box and return the path



def main ():
    #create the window
    root = tk.Tk()
    root.resizable(False, False)
    root.title('Sampl')
    root.geometry('300x200+50+50')
    root.iconbitmap('./assets/logo.ico')

    #create folder button
    folder_icon= tk.PhotoImage(file='./assets/folder.png')
    dirButton= ttk.Button(
        root,
        image=folder_icon,
        command=openDirDialog
    )


    actualPathlabel = tk.Label(
    root, text=path,
    font=("Arial Nova", 14))


    urlEntry = ttk.Entry(root)
    urlEntry.focus()

    #show elements
    actualPathlabel.pack()
    dirButton.pack(
     ipadx=5,
     ipady=5,
     expand=False
    )

    urlEntry.pack(fill='x', expand=True)

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()


if (path == ""):
    print("no path")


else:
    if (os.path.exists(path)):
        os.chdir(path)
        print(path)

    else:
        raise Exception("Directory is not correct:" + path)




url = "https://www.youtube.com/watch?v=eACohWVwTOc"
video = pafy.new(url)

bestaudio = video.getbestaudio()
bestaudio.download()

