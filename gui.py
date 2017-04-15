from appJar.appjar import gui
import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pythonMagic.magic as magic
import os
import sys

def makeReadable(myString):
	print("QQQ")
	print(myString)
	myString = myString.replace(" ", "\ ")
	myString = myString.replace("(", "\(")
	myString = myString.replace(")", "\)")
	myString = myString.replace("*", "\*")
	myString = myString.replace("!", "\!")
	myString = myString.replace("@", "\@")
	myString = myString.replace("#", "\#")
	myString = myString.replace("$", "\$")
	myString = myString.replace("%", "\%")
	myString = myString.replace("^", "\^")
	myString = myString.replace("&", "\&")
	myString = myString.replace("<", "\<")
	myString = myString.replace(">", "\>")
	myString = myString.replace("[", "\[")
	myString = myString.replace("]", "\]")
	myString = myString.replace("|", "\|")
	myString = myString.replace("{", "\{")
	myString = myString.replace("}", "\}")
	print(myString)
	return myString

def chooseFile(btn):
	Tk().withdraw() 
	filename = askopenfilename()
	filename = makeReadable(filename)
	app.setLabel("fileName", str(filename))
	mime = magic.Magic(mime=True)
	mimeType = mime.from_file(filename)
	test = (magic.Magic.guess_extension(mimeType))
	app.setLabel("currentFileType", mimeType)

def changeFileType(btn):
	newFileType = str(app.getOptionBox("New File Type"))
	fileName = str(app.getLabel("fileName"))
	if newFileType != "None" and fileName != "filename":
		app.setLabelBg("status", "Khaki")
		app.setLabel("status", "Converting")
		os.system("ffmpeg -i " + fileName + " " + fileName + "." + newFileType)
		app.setLabel("status", "Converted")
		app.setLabelBg("status", "LimeGreen")

def compress(btn):
	fileName = str(app.getLabel("fileName"))
	if fileName != "filename":
		speed = str(app.getOptionBox("Speed"))
		print(speed)
		fileType = str(app.getLabel("currentFileType"))
		print(fileType)
		app.setLabel("status", "Compressing")
		app.setLabelBg("status", "Khaki")
		os.system("time ffmpeg -threads 8 -i " + fileName + " -c:v libx265 -preset " + speed + " -quality 1 -c:a aac -b:a 128k -strict -2 " + fileName + "Compressed.mp4 -y")
		app.setLabel("status", "Compressed")
		app.setLabelBg("status", "LimeGreen")




pwd = str(os.popen('pwd').read())
path = str(os.popen('$PATH').read())
if pwd in path:
	print("Is In")
else:
	os.system("PATH=$PATH:$(pwd)")
	print("Isnt")


app = gui()

app.addButton("Choose File", chooseFile, 0, 0)
app.addLabel("fileName", "filename", 0, 1)
app.setLabelBg("fileName", "GhostWhite")

app.addLabel("currentFileType", "", 1, 0)
app.addLabel("arrow", " => ", 1, 1)
app.addLabelOptionBox("New File Type", ["- Audio -", "mp3", "wav", "- Video -", "mp4", "avi",
                        "mov", "wmv"], 1, 2)
app.addButton("Change File", changeFileType, 1, 3)

app.addLabel("compress", "Compress", 2, 0)
app.addLabelOptionBox("Speed", ["slow", "medium", "fast"], 2, 2)
app.addButton("Compress", compress, 2, 3)

app.addLabel("status", "Standby", 3, 0)
app.setLabelWidth("status", 3)
app.setLabelBg("status", "GhostWhite")


app.go()



