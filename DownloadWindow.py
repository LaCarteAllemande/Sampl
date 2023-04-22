import tkinter as tk
import Downloader
import MainWindow

class DownloadWindow(tk.Toplevel):
    def __init__(self, root, path:str, url:str):
        tk.Toplevel.__init__(self) 

        self['background']=MainWindow.BG_COLOR
        self.titleLabel =""
        self.ratioLabel = ""
        self.downloader =""
        self.titleSample =""
        self.url = url
        self.path = path
        
        self.title("Download started")
        self.iconbitmap('./assets/logo.ico')
        self.config(width=500, height=200)
        self.resizable(False, False)
        self.wm_transient(root)

        
        self.ratioLabel = tk.Label(self, text="Download : 0.00%", bg=MainWindow.BG_COLOR, fg=MainWindow.TEXT_COLOR)
        self.downloader = Downloader.Downloader()
        self.titleSample = self.generateSampleTitle(self.downloader.getTitle(url), self.downloader.getAuthor(url))
        
        self.titleLabel = tk.Entry(self, bg=MainWindow.BG_COLOR, fg=MainWindow.TEXT_COLOR, borderwidth=0, insertbackground=MainWindow.TEXT_COLOR, justify='center')
        self.titleLabel.insert(0, self.titleSample)
        self.titleLabel.place(relx=0.5, rely=0.5, relwidth=0.7,anchor=tk.constants.CENTER)
        self.ratioLabel.place(relx=0.5, rely=0.6, anchor=tk.constants.CENTER)


    def generateSampleTitle(self, videoTitle:str, author:str):
        title = videoTitle.replace("(Official Music Video)", "") 
        
        if not (author in title):
            author = author.replace(" - Topic", "")
            title = title + " - " + author
        return title

    def generateFileName(self):
        return self.titleSample + ".mp4"

    def download(self, url :str, path :str):
        self.downloader.ytDownload(url, path, self.generateFileName(), self)
        self.destroy()


    def getSampleName(self):
        if (self.titleLabel.get() != ""):
            return self.titleLabel.get()


    def updateRatio(self, ratio):
        self.ratioLabel.config(text = "Download :"+  str(round(ratio * 100, 2)) + "%")