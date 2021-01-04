from tkinter import *
from tkinter import ttk
import requests
import json

root = Tk()

url = "https://www.balldontlie.io/api/v1/teams"
balldontlie = requests.get(url)
data = json.loads(balldontlie.text)

#APITEAMNAMES
TNTor = (data["data"][27]["full_name"])
TNCli = (data["data"][12]["full_name"])
TNMia = (data["data"][15]["full_name"])
TNMil = (data["data"][16]["full_name"])
TNLak = (data["data"][13]["full_name"])

#PREDICTIONS RAPTORS AGAINST DIF TEAMS TABS
RaptorsPredictions = ttk.Notebook(root)
RaptorsPredictions.pack(pady=15)

RaptorsMain = Frame(RaptorsPredictions, width = 1000, height = 1000, bg = 'Red')
RapsvsLakers = Frame(RaptorsPredictions, width = 1000, height = 1000, bg = 'Yellow')
RapsvsClips = Frame(RaptorsPredictions, width = 1000, height = 1000, bg = 'Blue')
RapsvsBucks = Frame(RaptorsPredictions, width = 1000, height = 1000, bg = 'Green')
RapsvsHeat = Frame(RaptorsPredictions, width = 1000, height = 1000, bg = 'Orange')

RaptorsMain.pack(fill="both", expand=1)
RapsvsLakers.pack(fill="both", expand=1)
RapsvsClips.pack(fill="both", expand=1)
RapsvsBucks.pack(fill="both", expand=1)
RapsvsHeat.pack(fill="both", expand=1)

RaptorsPredictions.add(RaptorsMain, text="Raptors Main")
RaptorsPredictions.add(RapsvsLakers, text="Raptors vs Lakers")
RaptorsPredictions.add(RapsvsClips, text="Raptors vs Clippers")
RaptorsPredictions.add(RapsvsBucks, text="Raptors vs Bucks")
RaptorsPredictions.add(RapsvsHeat, text="Raptors vs Heat")

#TITLE
text = Label(RaptorsMain,text="Toronto Raptors",font=('Arial',50),bg="red")
text.place(x=300,y=20)

text = Label(RapsvsLakers,text="Which team will win?",font=('Arial',20),bg="yellow")
text.place(x=377,y=13)

text = Label(RapsvsClips,text="Which team will win?",font=('Arial',20),bg="blue")
text.place(x=377,y=13)

text = Label(RapsvsBucks,text="Which team will win?",font=('Arial',20),bg="green")
text.place(x=377,y=13)

text = Label(RapsvsHeat,text="Which team will win?",font=('Arial',20),bg="Orange")
text.place(x=377,y=13)

#Team Names 
TNTor.place(x=377,y=13)

#NBADESCRIPTION FOR HOMEPAGE
'''
NBAdes = Label(RaptorsMain, 
text="The National Basketball Association is an American men's professional basketball league. It is composed of 30 teams and is one of the four major professional sports leagues in the United States and Canada. It is the premier men's professional basketball league in the world.",
font=('Arial',10,'bold'), height=10, width=100,)
NBAdes.place(x=10,y=400)
'''
#ROOT
root.geometry("1000x1000")
root.title("NBA Predictions")
root.mainloop()

#STEPS NEEDED
#ACCESSING THE DATA
#DISPLAY THE DATA
#DISPLAY IN A TABLE
#SHOW TEH WINNER AND LOSER