import os
from tkinter import messagebox

DATE_FILE ="path.txt"
DATA_FOLDER = "./data/"
DATA_PATH = DATA_FOLDER + DATE_FILE

#create a data file to store the samples' path
def CreateDataPath():
    print("hello")
    if not (os.path.exists(DATA_FOLDER)):
        os.makedirs(DATA_FOLDER)
    if not (os.path.exists(DATA_PATH)):
        open(DATA_PATH, 'w')

#check if the path is correct
def CheckPath(path):
    if (path == "" or (os.path.exists(path) == False)):
        return False
    return True

#save teh path into a text file
def SavePath(path):
    try:
        f = open(DATA_PATH, "w")
        f.write(path)
        f.close()
    except:
        CreateDataPath()

#return the saved path to store the samples
def GetSamplePath():
    try:
        f = open(DATA_PATH, "r")
        path = f.read()
        f.close()

        if (CheckPath(path)):
            return path
        else:
            messagebox.showinfo("Path invalid", "Path is not valid")
        
    except:
        CreateDataPath()
        messagebox.showinfo("Some data missing", "Couldn't retrieve saved path")
    
    return DefaultPath()

#return the default path to save the samples
def DefaultPath():
    return os.path.dirname(os.path.realpath(__file__))