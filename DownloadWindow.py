import tkinter as tk

class DownloadWindow(tk.Toplevel):
    def __init__(self, title):
        tk.Toplevel.__init__(self) 
        self.titleLabel =""
        self.ratioLabel = ""

        self.title("Download started")
        self.iconbitmap('./assets/logo.ico')
        self.config(width=300, height=200)
        self.resizable(False, False)

        self.titleLabel = tk.Label(self, text=title)
        self.ratioLabel = tk.Label(self, text="Download : 0.00%")

        self.titleLabel.place(relx=0.5, rely=0.5, anchor=tk.constants.CENTER)
        self.ratioLabel.place(relx=0.5, rely=0.6, anchor=tk.constants.CENTER)

    def updateRatio(self, ratio):
        self.ratioLabel.config(text = "Download :"+  str(round(ratio, 2)* 100) + "%")