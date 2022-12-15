import pafy
from tkinter import messagebox
import requests
import Data
import os
from pydub import AudioSegment
import time 
import DownloadWindow


class Downloader:
    def ytDownload(self, url:str, path :str, window):
        self.window = window
        video = pafy.new(url)
        self.title = video.title
        bestaudio = video.getbestaudio(preftype="m4a", ftypestrict=True)
        self.file = bestaudio.filename
        self.extension = bestaudio.extension
        bestaudio.download(filepath=path, quiet=True, callback=self.updateDownload)
        self.window.convert()
        #self.window.destroy()

    def updateDownload(self, total, recvd, ratio, rate, eta):   
        self.window.updateRatio(ratio)
        if (ratio == 1.0):
            time.sleep(2) 
            
            #self.window.destroy()
        #messagebox.showinfo("Invalid path", (round(ratio, 2)))
    
    def getTitle(self, url :str):
        return pafy.new(url).title

    def getFilename(self):
        return self.file

#check if the url is correct
def CheckLink(link):
    try:
        request = requests.get(link)
        return request.status_code == 200
    except:
        return False

def ConvertToMp3(path :str, audioFile:str, extension:str):
        #print(audioFile, "\n", extension, name)
        # audio = AudioSegment.from_file("./" + audioFile, format=extension)
        
        # audio.export(name+".mp3", format="mp3")
    os.chdir(path)
    print(audioFile)
    audio = AudioSegment.from_file(audioFile)
    audio.export("b.mp3", format="mp3")