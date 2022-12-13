import pafy
from tkinter import messagebox


import requests
import Data
import os

from pydub import AudioSegment

import DownloadWindow




#check if the url is correct
def CheckLink(link):
    try:
        request = requests.get(link)
        return request.status_code == 200
    except:
        return False

def Download(link, path):
    if (CheckLink(link)):
        if (Data.CheckPath(path)):
            YtDownload(link, path)
        else:
            messagebox.showinfo("Invalid path", "Invalid download path")
    else:
        messagebox.showinfo("Invalid url", "Invalid url")

def YtDownload(url, path):
    global dlWindow
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    
    dlWindow = DownloadWindow.DownloadWindow(bestaudio.title)
    bestaudio.download(path, quiet=True,  callback=UpdateDownload)
    
    #ConvertToMp3(bestaudio.filename, bestaudio.extension,bestaudio.title)


def UpdateDownload(total, recvd, ratio, rate, eta):

    if (dlWindow is not None):
        print(ratio)
        dlWindow.updateRatio(rate)
    #messagebox.showinfo("Invalid path", (round(ratio, 2)))


def ConvertToMp3(audioFile, extension, name):
    #print(audioFile, "\n", extension, name)


    # audio = AudioSegment.from_file("./" + audioFile, format=extension)
    
    # audio.export(name+".mp3", format="mp3")
    print(os.getcwd())
    audio = AudioSegment.from_file("a.mp3", format="mp3")
    
    audio.export("b.mp3", format="mp3")

