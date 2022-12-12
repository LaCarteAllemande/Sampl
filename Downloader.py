import pafy
from tkinter import messagebox
import requests
import Data
import os

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
    os.chdir(path)
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download()
