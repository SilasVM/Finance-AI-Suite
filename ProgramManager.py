from tkinter import *
from tkinter import messagebox
import sys
import webbrowser
import subprocess
import signal
import os

APP_DIR = "apps"

#Code to build tkinter window
window = Tk()
#Title
window.title("Welcome to my Financial AI Suite!")
#Size
window.geometry('800x800')
#Scaling
window.tk.call('tk', 'scaling', 3.0)

#User Greeting
greetingCard = Label(window, text="Welcome to the Financial AI Program Suite!", font=("Times New Roman", 20, "bold"), pady = 20)
greetingCard.grid()

container = Frame(window)
container.grid(padx = 20, pady = 20)



#Function to retrieve YouTube Video Links from txt file.
def getVideoLink(assn):
    with open("videos.txt") as f:
        for line in f:
            if line.startswith(assn + ":"):
                return line.split(":", 1)[1].strip()
    return None

matchedDocs = {}

currentProcess = None

#function to utilize run code button and run code.
def runCode(pythonFile):
    global currentProcess

    if currentProcess is not None and currentProcess.poll() is None:
        try:
            currentProcess.terminate()
        except Exception as e:
            messagebox.showerror("Error", "Could not stop previous process")

    try:
        currentProcess = subprocess.Popen([sys.executable, pythonFile])
    except Exception as e:
        messagebox.showerror("Error running the selected program", str(e))

#Searching all subfolders of Assignments. Detecting python code and 
row = 0
col = 0
maxCols = 3
for folder in sorted(os.listdir(APP_DIR)):
    #Extending the filepath to include subfolders
    folderPath = os.path.join(APP_DIR, folder)

    if os.path.isdir(folderPath):

        #Creating a frame for the program
        card = Frame(container, width = 400, height = 150, bd = 2, relief = "raised")
        card.grid(row = row, column = col, padx = 10, pady = 10)
        card.grid_propagate(False)

        #Spacer to put the buttons towards the bottom of each card
        card.grid_rowconfigure(1, weight = 1)

        #Finding the file containing python code for program
        pythonList = [f for f in os.listdir(folderPath) if f.endswith(".py")]
        if pythonList:
            pythonFilePath = os.path.join(folderPath, pythonList[0])
            
            #Adding buttons for each program frame to run, link the vide, and pull up docs
            runButton = Button(card, text = "Run", command = lambda f = pythonFilePath: runCode(f))
            runButton.grid(row = 2, column = 0, padx = 3, pady = 5, sticky = "ew")
            

            #pythonFiles[folder] = pythonList if pythonList else None
            fileName = os.path.splitext(pythonList[0])[0]

            label = Label(card, text = fileName, font = ("Times New Roman", 8, "bold"))
            label.grid(row = 0, column = 1, columnspan = 3, pady = (10, 5))

            docxPath = os.path.join(folderPath, f"{fileName}.docx")
            pdfPath = os.path.join(folderPath, f"{fileName}.pdf")

            docPath = None
            if os.path.exists(docxPath):
                docPath = docxPath
            elif os.path.exists(pdfPath):
                docPath = pdfPath

            if docPath:
                matchedDocs[fileName] = docPath

                docButton = Button(card, text = "Doc", command = lambda f = docPath: webbrowser.open(f"file://{os.path.abspath(f)}"))
                docButton.grid(row = 2, column = 1, padx = 3, pady = 5, sticky = "ew")

            youTubeVideo = getVideoLink(folder)

            if youTubeVideo:
                videoButton = Button(card, text = "Video", command = lambda f = youTubeVideo: webbrowser.open(f))
                videoButton.grid(row = 2, column = 2, padx = 3, pady = 5, sticky = "ew")
    col += 1
    if col >= maxCols:
        col = 0
        row += 1

#Loop to keep window open and running
window.mainloop()