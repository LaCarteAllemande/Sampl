import tkinter as tk
import Downloader

class DownloadWindow(tk.Toplevel):
    def __init__(self, root, path:str, url:str):
        tk.Toplevel.__init__(self) 

        self.titleLabel =""
        self.ratioLabel = ""
        self.downloader =""

        self.title("Download started")
        self.iconbitmap('./assets/logo.ico')
        self.config(width=500, height=200)
        self.resizable(False, False)
        self.wm_transient(root)

        
        self.ratioLabel = tk.Label(self, text="Download : 0.00%")
        self.downloader = Downloader.Downloader()
        self.titleLabel = tk.Label(self, text=self.downloader.getTitle(url))


        self.titleLabel.place(relx=0.5, rely=0.5, anchor=tk.constants.CENTER)
        self.ratioLabel.place(relx=0.5, rely=0.6, anchor=tk.constants.CENTER)

    def download(self, url :str, path :str):
        self.downloader.ytDownload(url, path, self)


    def updateRatio(self, ratio):
        self.ratioLabel.config(text = "Download :"+  str(round(ratio * 100, 2)) + "%")