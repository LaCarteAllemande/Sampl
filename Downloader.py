import pafy
from tkinter import messagebox
import requests
import Data
import os
#from pydub import AudioSegment

import DownloadWindow


class Downloader:
    def ytDownload(self, url:str, path :str, window):
        self.window = window
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download(filepath=path, quiet=True, callback=self.updateDownload)
        return bestaudio.title

    def updateDownload(self, total, recvd, ratio, rate, eta):   
        self.window.updateRatio(ratio)
        if (ratio == 1.0):
            self.window.destroy()
        #messagebox.showinfo("Invalid path", (round(ratio, 2)))
    
    def getTitle(self, url:str):
        video = pafy.new(url)
        return video.title

    def ConvertToMp3(audioFile, extension, name):
        #print(audioFile, "\n", extension, name)


        # audio = AudioSegment.from_file("./" + audioFile, format=extension)
        
        # audio.export(name+".mp3", format="mp3")
        print(os.getcwd())
        audio = AudioSegment.from_file("a.mp3", format="mp3")
        
        audio.export("b.mp3", format="mp3")

#check if the url is correct
def CheckLink(link):
    try:
        request = requests.get(link)
        return request.status_code == 200
    except:
        return False