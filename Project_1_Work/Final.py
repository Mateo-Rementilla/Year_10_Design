from tkinter import * #GUI package
from tkinter import ttk #For different frames
import requests #Requesting for Api data
import json #Changing the format to json
root = Tk() #Opens Window
root.geometry("715x700") #Set size of the Window
root.title("Raptors 2020 Game Predictions") #Create title of the Window

url = "https://www.balldontlie.io/api/v1/teams" #Define url as the api link
balldontlie = requests.get(url) #Requesting for API data from the url
data = json.loads(balldontlie.text) #Define data as all of API infromation

#ApiTeamnames #Dictionary names have "" and list are numbers
TNTor = (data["data"][27]["full_name"]) #TeamNameTorontoRapotrs
TNCli = (data["data"][12]["full_name"]) #TeamNameLAClippers
TNMia = (data["data"][15]["full_name"]) #TeamNameMiamiHeat
TNMil = (data["data"][16]["full_name"]) #TeamNameMilwakeeBucks
TNLak = (data["data"][13]["full_name"]) #TeamNameLALakers

#DATA
#Function for Data
def TotalData():  
    for line in content: 
        content_array.append(line.strip().split(',')) 
#Creates a list of lists

#MAIN
myFile = open('TeamData.cvs.txt', 'r') #Opens Data file
content = myFile.readlines() #Readlines
content_array = []
TotalData() #Call for Data

#Single Team Array Loops (This gets the number of the row for each team)
Raptors = -1
for i in range (1,len(content_array)): #Second Item in the Array 
# to total numnber of items in the list (In this case it could 
# be subsituted with 25) 
    try:
        Raptors = content_array[i].index('Toronto Raptors') 
        Raptors = i
    except:
        pass

Lakers = -1
for i in range (1,len(content_array)):
    try:
        Lakers = content_array[i].index('Los Angeles Lakers')
        Lakers = i
    except:
        pass

Clippers = -1
for i in range (1,len(content_array)):
    try:
        Clippers = content_array[i].index('LA Clippers')
        Clippers = i
    except:
        pass

Bucks = -1
for i in range (1,len(content_array)):
    try:
        Bucks = content_array[i].index('Milwaukee Bucks')
        Bucks = i
    except:
        pass

Heat = -1
for i in range (1,len(content_array)):
    try:
        Heat = content_array[i].index('Miami Heat')
        Heat = i
    except:
        pass

StatType = -1
for i in range (0,len(content_array)):
    try:
        StatType = content_array[i].index('Rk')
        StatType = i
    except:
        pass

#Create variable for specific team data 
#Within the the list of lists print just the list/line for the Raptors 
RaptorsStats = content_array[Raptors]
LakersStats = content_array[Lakers]
ClippersStats = content_array[Clippers]
BucksStats = content_array[Bucks]
HeatStats = content_array[Heat]
Stats = content_array[StatType][:-1] 
#Unknown reason the first line which is the variable "Stats "in 'TeamData.cvs.txt' had an extra piece of data at the end in the list, hence [:-1]

#FRAMES
#Predictions Frames
RaptorsPredictions = ttk.Notebook(root) #Notebook command gives the ability to create multiple frames
RaptorsPredictions.pack(pady=15)

#Different Frames for each different matchup
RaptorsMain = Frame(RaptorsPredictions, width = 1000, height = 1000) 
RapsvsLakers = Frame(RaptorsPredictions, width = 1000, height = 1000)
RapsvsClips = Frame(RaptorsPredictions, width = 1000, height = 1000)
RapsvsBucks = Frame(RaptorsPredictions, width = 1000, height = 1000)
RapsvsHeat = Frame(RaptorsPredictions, width = 1000, height = 1000)

#Pack means place them on the GUI
RaptorsMain.pack(fill="both", expand=1)
RapsvsLakers.pack(fill="both", expand=1)
RapsvsClips.pack(fill="both", expand=1)
RapsvsBucks.pack(fill="both", expand=1)
RapsvsHeat.pack(fill="both", expand=1)

#'.add' gives the ability to create titles for each frame
RaptorsPredictions.add(RaptorsMain, text="Raptors Main")
RaptorsPredictions.add(RapsvsLakers, text="Raptors vs Lakers")
RaptorsPredictions.add(RapsvsClips, text="Raptors vs Clippers")
RaptorsPredictions.add(RapsvsBucks, text="Raptors vs Bucks")
RaptorsPredictions.add(RapsvsHeat, text="Raptors vs Heat")

#BACKGROUNDS
#RaptorsMain Homepage Background Image
bg = PhotoImage(file="images/Raptors2.png")

BackgroundImage = Label(RaptorsMain, image=bg)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")
BGRapsMain.create_text(330,295, text="Toronto Raptors", font=("Helvetica",50), fill="#b90438")

#RapsvsLakers Background Image
bg2 = PhotoImage(file="images/Lakers.png")

BackgroundImage2 = Label(RapsvsLakers, image=bg2)
BackgroundImage2.place(x=0,y=0, relwidth=1, relheight=1)

#RapsvsClippers Background Image
bg3 = PhotoImage(file="images/Clippers.png")

BackgroundImage3 = Label(RapsvsClips, image=bg3)
BackgroundImage3.place(x=0,y=0, relwidth=1, relheight=1)

#RapsvsBucks Background Image
bg4 = PhotoImage(file="images/Bucks.png")

BackgroundImage4 = Label(RapsvsBucks, image=bg4)
BackgroundImage4.place(x=0,y=0, relwidth=1, relheight=1)

#RapsvsHeat Background Image
bg5 = PhotoImage(file="images/Miami.png")

BackgroundImage5 = Label(RapsvsHeat, image=bg5)
BackgroundImage5.place(x=0,y=0, relwidth=1, relheight=1)

#TABLES
#Scroll Bar for RapsvsLakersTable
RapsvsLakersSB = Scrollbar(RapsvsLakers)
RapsvsLakersSB.pack(side=RIGHT,fill=Y) 

#Table for Raptors vs Lakers
RapsvsLakersTable = ttk.Treeview(RapsvsLakers, yscrollcommand=RapsvsLakersSB.set)

#Configure Scroll Bar
RapsvsLakersSB.config(command=RapsvsLakersTable.yview)

#Everything is 'Y' eg.fill=Y,yscrollcommand,RapsvsLakerTable.yview because you want the the SB to be vertical/on the Y Axis. 

#Define our Columns 
RapsvsLakersTable['columns']=('Toronto Raptors', 'Stat', 'Los Angeles Lakers') 

#Format our Columns
RapsvsLakersTable.column("#0", width=0, stretch=NO) #Phantom column 
RapsvsLakersTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsLakersTable.column("Stat", anchor=CENTER, width=80)
RapsvsLakersTable.column("Los Angeles Lakers", anchor=CENTER, width=120)

#Create headings 
RapsvsLakersTable.heading("#0", anchor=W)
RapsvsLakersTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER) #Using API for Heading of Table
RapsvsLakersTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsLakersTable.heading("Los Angeles Lakers", text=TNLak, anchor=CENTER) #Using API for Heading of Table

#Add Data
for i in range (2,25): #Grabs all items in list from the 3rd to the 25th
    RapsvsLakersTable.insert(parent='',index='end',iid=i,values=(RaptorsStats[i],Stats[i],LakersStats[i]))

#Place the table on Raptors vs Lakers frame
RapsvsLakersTable.place(x=167,y=170)

#Scroll Bar for RapsvsClipsTable
RapsvsClipsSB = Scrollbar(RapsvsClips)
RapsvsClipsSB.pack(side=RIGHT,fill=Y)

#Table for Raptors vs Clippers
RapsvsClipsTable = ttk.Treeview(RapsvsClips, yscrollcommand=RapsvsClipsSB.set)

#Configure Scroll Bar
RapsvsClipsSB.config(command=RapsvsClipsTable.yview)

#Define our Columns 
RapsvsClipsTable['columns']=('Toronto Raptors', 'Stat', 'Los Angeles Clippers') 

#Format our Columns
RapsvsClipsTable.column("#0", width=0, stretch=NO) 
RapsvsClipsTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsClipsTable.column("Stat", anchor=CENTER, width=80)
RapsvsClipsTable.column("Los Angeles Clippers", anchor=CENTER, width=120)

#Create headings
RapsvsClipsTable.heading("#0", anchor=W)
RapsvsClipsTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsClipsTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsClipsTable.heading("Los Angeles Clippers", text=TNCli, anchor=CENTER)

#Add Data
for i in range (2,25): #Grabs all items in list from the 3rd to the 25th
    RapsvsClipsTable.insert(parent='',index='end',iid=i,values=(RaptorsStats[i],Stats[i],ClippersStats[i]))

#Place the table on Raptors vs Clippers frame
RapsvsClipsTable.place(x=167,y=170)

#Scroll Bar for RapsvsBucksTable
RapsvsBucksSB = Scrollbar(RapsvsBucks)
RapsvsBucksSB.pack(side=RIGHT,fill=Y)

#Table for Raptors vs Bucks
RapsvsBucksTable =ttk.Treeview(RapsvsBucks, yscrollcommand=RapsvsBucksSB.set)

#Configure Scroll Bar
RapsvsBucksSB.config(command=RapsvsBucksTable.yview)

#Define our Columns 
RapsvsBucksTable['columns']=('Toronto Raptors', 'Stat', 'Milwaukee Bucks') 

#Format our Columns
RapsvsBucksTable.column("#0", width=0, stretch=NO) 
RapsvsBucksTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsBucksTable.column("Stat", anchor=CENTER, width=80)
RapsvsBucksTable.column("Milwaukee Bucks", anchor=CENTER, width=120)

#Create headings
RapsvsBucksTable.heading("#0", anchor=W)
RapsvsBucksTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsBucksTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsBucksTable.heading("Milwaukee Bucks", text=TNMil, anchor=CENTER)

#Add Data
for i in range (2,25): #Grabs all items in list from the 3rd to the 25th 
    RapsvsBucksTable.insert(parent='',index='end',iid=i,values=(RaptorsStats[i],Stats[i],BucksStats[i])) 

#Place the table on Raptors vs Heat frame
RapsvsBucksTable.place(x=167,y=170)

#Scroll Bar for RapsvsClipsTable
RapsvsHeatSB = Scrollbar(RapsvsHeat)
RapsvsHeatSB.pack(side=RIGHT,fill=Y)

#Table for Raptors vs Heat
RapsvsHeatTable = ttk.Treeview(RapsvsHeat, yscrollcommand=RapsvsHeatSB.set)

RapsvsHeatSB.config(command=RapsvsHeatTable.yview)

#Define our Columns 
RapsvsHeatTable['columns']=('Toronto Raptors', 'Stat', 'Miami Heat') 

#Format our Columns
RapsvsHeatTable.column("#0", width=0, stretch=NO) 
RapsvsHeatTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsHeatTable.column("Stat", anchor=CENTER, width=80)
RapsvsHeatTable.column("Miami Heat", anchor=CENTER, width=120)

#Create headings
RapsvsHeatTable.heading("#0", anchor=W)
RapsvsHeatTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsHeatTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsHeatTable.heading("Miami Heat", text=TNMia, anchor=CENTER)

#Add Data
for i in range (2,25): #Grabs all items in list from the 3rd to the 25th
    RapsvsHeatTable.insert(parent='',index='end',iid=i,values=(RaptorsStats[i],Stats[i],HeatStats[i]))

#Place the table on Raptors vs Lakers frame
RapsvsHeatTable.place(x=167,y=170)

#Creates colour to tables when stat is clicked on 
Style = ttk.Style()

#Add atributes eg. colour
Style.configure("Treeview",
    background="silver",
    foreground="black",
    rowheight=25,
    fieldbackground="silver"
    )
Style.map('Treeview',
    background=[('selected','#eeeee4')])

#BUTTONS
#Win and Lose Buttons
def myClick(team1Data, team2Data, team1Name, team2Name, frame):
    team1Score = team1Data[6] #[6] refers to 7th item in the list which is FG%
    team2Score = team2Data[6] #[6] refers to 7th item in the list which is FG%

    if team1Score > team2Score: 
        text = team1Name + " Win!"
    elif team1Score == team2Score: 
        text = "Tie Game"
    else: 
        text = team2Name + " Win!"

    WinningLabel = Label(frame,text=text,bg='chartreuse3',width=17)
    WinningLabel.place(x=250,y=475)

#Functions for every button that simply calls myClick with the correct data.
def RunFunctionRapsvsLakers():
    myClick(RaptorsStats, LakersStats, 
    "Raptors", "Lakers", RapsvsLakers)

LakersResult = Button(RapsvsLakers,text='Run simulation of Game', bd='5', bg='red',fg='black',command=RunFunctionRapsvsLakers)  
LakersResult.place(x=250,y=445) 

def RunFunctionRapsvsClips():
    myClick(RaptorsStats, ClippersStats, 
    "Raptors", "Clippers", RapsvsClips)

ClipsResult = Button(RapsvsClips,text='Run simulation of Game', bd='5', bg='red',fg='black',command=RunFunctionRapsvsClips )  
ClipsResult.place(x=250,y=445) 

def RunFunctionRapsvsBucks():
    myClick(RaptorsStats, BucksStats, 
    "Raptors", "Bucks", RapsvsBucks)

BucksResult = Button(RapsvsBucks,text='Run simulation of Game', bd='5', bg='red',fg='black',command=RunFunctionRapsvsBucks )  
BucksResult.place(x=250,y=445) 

def RunFunctionRapsvsHeat():
    myClick(RaptorsStats, HeatStats, 
    "Raptors", "Heat", RapsvsHeat)

HeatResult = Button(RapsvsHeat,text='Run simulation of Game', bd='5', bg='red',fg='black',command=RunFunctionRapsvsHeat )  
HeatResult.place(x=250,y=445) 

#Exit Button
ExitButtonHomepage = Button(RaptorsMain,text='Exit', bd='5',fg='black',command= root.destroy)
ExitButtonHomepage.place(x=623, y=574) 

root.mainloop()