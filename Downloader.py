

from pytube import YouTube

import pafy

from tkinter import messagebox

import requests

import Storage
import os

from pydub import AudioSegment
import time 

import DownloadWindow




class Downloader:

    def ytDownload(self, url:str, path :str, fileName:str, window):

        self.window = window #delete that ?

        self.video = YouTube(url)

        self.video.streams.filter(only_audio=True).order_by('abr').desc().first().download(output_path=path, filename=fileName, on_progress_callback= self.updateDownloadProgress)

        self.convertToMp3(path, fileName, "mp4")



    def updateDownloadProgress(self, stream, chunk, bytes_remaining):   


        total_size = stream.filesize

        bytes_downloaded = total_size - bytes_remaining

        download_ratio = bytes_downloaded / total_size


        self.window.updateRatio(download_ratio)

        if (download_ratio == 1.0):

            time.sleep(2) 
            
    

    def getTitle(self, url :str):

        try:

            return YouTube(url).title

        except:

            try :

                return pafy.new(url).title

            except:

                return "Name"
    

    def getAuthor(self, url :str):

        try:

            return YouTube(url).author

        except:

            try :

                return pafy.new(url).author

            except:

                return "Author"


    def getFilename(self):
        return self.file


    def convertToMp3(self, path :str, audioFile:str, extension:str):

        actualPath = os.getcwd()

        os.chdir(path)

        audio = AudioSegment.from_file(audioFile)

        audio.export(self.window.getSampleName() + ".mp3", format="mp3")

        os.remove(audioFile) 

        os.chdir(actualPath)



#check if the url is correct

def CheckLink(link):

    try:

        request = requests.get(link)

        return request.status_code == 200

    except:

        return False


