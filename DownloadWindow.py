import tkinter as tk
import Downloader

class DownloadWindow(tk.Toplevel):
    def __init__(self, root, path:str, url:str):
        tk.Toplevel.__init__(self) 

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

        
        self.ratioLabel = tk.Label(self, text="Download : 0.00%")
        self.downloader = Downloader.Downloader()
        self.titleSample = self.generateSampleTitle(self.downloader.getTitle(url), self.downloader.getAuthor(url))
        
        self.titleLabel = tk.Label(self, text=self.titleSample)


        self.titleLabel.place(relx=0.5, rely=0.5, anchor=tk.constants.CENTER)
        self.ratioLabel.place(relx=0.5, rely=0.6, anchor=tk.constants.CENTER)

    def convert(self):
        Downloader.ConvertToMp3(self.path , self.downloader.getFilename(), "m4a" , self.titleSample)

    def generateSampleTitle(self, videoTitle:str, author:str):
        #print(self.titleSample.replace("(Official Music Video)", ""))
        title = videoTitle.replace("(Official Music Video)", "")
        
        if not (author in title):
            title = title + " - " + author

        return title
    
    def download(self, url :str, path :str):
        try:
            self.downloader.ytDownload(url, path, self)
        except:
            messagebox.option('Download error', "Error while downloading " + self.titleSample + ", maybe try again ?")

    def updateRatio(self, ratio):
        self.ratioLabel.config(text = "Download :"+  str(round(ratio * 100, 2)) + "%")