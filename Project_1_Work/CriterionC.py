from tkinter import * #GUI package
from tkinter import ttk #For different frames
import requests #Requesting for Api data
import json #Changing the format to json
root = Tk() #Opens Window

url = "https://www.balldontlie.io/api/v1/teams" #Define url as the api link
balldontlie = requests.get(url) #Requesting for API data from the url
data = json.loads(balldontlie.text) #Define data as all of API infromation

#ApiTeamnames
TNTor = (data["data"][27]["full_name"]) #TeamNameTorontoRapotrs
TNCli = (data["data"][12]["full_name"]) #TeamNameLAClippers
TNMia = (data["data"][15]["full_name"]) #TeamNameMiamiHeat
TNMil = (data["data"][16]["full_name"]) #TeamNameMilwakeeBucks
TNLak = (data["data"][13]["full_name"]) #TeamNameLALakers

#Function for Data
def TotalData():  
    global content_array 
    for line in content: 
        content_array.append(line.strip().split(','))

#MAIN
myFile = open('TeamData.cvs.txt', 'r') 
content = myFile.readlines() 
content_array = []

TotalData() #Call for Data

#Single Team Array Loops (This gets the stats for a single team)
Raptors = -1
for i in range (1,len(content_array)):
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
RaptorsStats = content_array[Raptors]
LakersStats = content_array[Lakers]
ClippersStats = content_array[Clippers]
BucksStats = content_array[Bucks]
HeatStats = content_array[Heat]
Stats = content_array[StatType][:-1] #Unknown reason the first line in 'TeamData.cvs.txt' had an extra piece of data at the end in the list, hence [:-1]

#Predictions Tabs
RaptorsPredictions = ttk.Notebook(root)
RaptorsPredictions.pack(pady=15)

#Different Tabs/Frames for each different matchup
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

#RaptorsMain Homepage Background Image
bg = PhotoImage(file="images/Raptors2.png")

BackgroundImage = Label(RaptorsMain, image=bg)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")
BGRapsMain.create_text(330,275, text="Toronto Raptors", font=("Helvetica",50), fill="red")

#RapsvsLakers Background Image
bg2 = PhotoImage(file="images/Lakers.png")

BackgroundImage = Label(RapsvsLakers, image=bg2)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")
BGRapsMain.create_text(330,40, text="Which team will win?", font=("Helvetica",50), fill="black")

#RapsvsClippers Background Image
bg3 = PhotoImage(file="images/Clippers.png")

BackgroundImage = Label(RapsvsClips, image=bg3)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")

#RapsvsBucks Background Image
bg4 = PhotoImage(file="images/Bucks.png")

BackgroundImage = Label(RapsvsBucks, image=bg4)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")

#RapsvsHeat Background Image
bg5 = PhotoImage(file="images/Miami.png")

BackgroundImage = Label(RapsvsHeat, image=bg5)
BackgroundImage.place(x=0,y=0, relwidth=1, relheight=1)

#Create Canvas
BGRapsMain = Canvas(RaptorsMain, width=715, height=700)
BGRapsMain.pack(fill="both",expand=True)
BGRapsMain.create_image(0,0, image=bg, anchor="nw")

#Scroll Bar for RapsvsLakersTable
RapsvsLakersSB = Scrollbar(RapsvsLakers)
RapsvsLakersSB.pack(side=RIGHT,fill=Y)

#Table for Raptors vs Lakers
RapsvsLakersTable = ttk.Treeview(RapsvsLakers, yscrollcommand=RapsvsLakersSB.set)

#Configure Scroll Bar
RapsvsLakersSB.config(command=RapsvsLakersTable.yview)

#Define our Columns 
RapsvsLakersTable['columns']=('Toronto Raptors', 'Stat', 'Los Angeles Lakers') 

#Format our Columns
RapsvsLakersTable.column("#0", width=0, stretch=NO) 
RapsvsLakersTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsLakersTable.column("Stat", anchor=CENTER, width=80)
RapsvsLakersTable.column("Los Angeles Lakers", anchor=CENTER, width=120)

#Create headings 
RapsvsLakersTable.heading("#0", text="Label", anchor=W)
RapsvsLakersTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER) #Using API for Heading of Table
RapsvsLakersTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsLakersTable.heading("Los Angeles Lakers", text=TNLak, anchor=CENTER) #Using API for Heading of Table

#Add Data
for i in range (2,25):
    RapsvsLakersTable.insert(parent='',index='end',iid=i,text="Parent",values=(RaptorsStats[i],Stats[i],LakersStats[i]))

Style = ttk.Style(RapsvsLakersTable)

Style.configure("Treeview",
    background="silver",
    foreground="black",
    rowheight=25,
    fieldbackground="silver"
    )
Style.map('Treeview',
    background=[('selected','#eeeee4')])


#Place the table on Raptors vs Lakers tab/frame
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
RapsvsClipsTable.heading("#0", text="Label", anchor=W)
RapsvsClipsTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsClipsTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsClipsTable.heading("Los Angeles Clippers", text=TNCli, anchor=CENTER)

#Add Data
for i in range (2,25):
    RapsvsClipsTable.insert(parent='',index='end',iid=i,text="Parent",values=(RaptorsStats[i],Stats[i],ClippersStats[i]))

#Place the table on Raptors vs Clippers tab/frame
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
RapsvsBucksTable.heading("#0", text="Label", anchor=W)
RapsvsBucksTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsBucksTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsBucksTable.heading("Milwaukee Bucks", text=TNMil, anchor=CENTER)

#Add Data
for i in range (2,25):
    RapsvsBucksTable.insert(parent='',index='end',iid=i,text="Parent",values=(RaptorsStats[i],Stats[i],BucksStats[i]))

#Place the table on Raptors vs Heat tab/frame
RapsvsBucksTable.place(x=167,y=170)
'''
#Scroll Bar for RapsvsClipsTable
RapsvsHeatSB = Scrollbar(RapsvsHeat)
RapsvsHeatSB.pack(side=RIGHT,fill=Y)
'''
#Table for Raptors vs Heat
RapsvsHeatTable =ttk.Treeview(RapsvsHeat)
'''
RapsvsHeatSB.config(command=RapsvsHeatTable.yview)
'''
#Define our Columns 
RapsvsHeatTable['columns']=('Toronto Raptors', 'Stat', 'Miami Heat') 

#Format our Columns
RapsvsHeatTable.column("#0", width=0, stretch=NO) 
RapsvsHeatTable.column("Toronto Raptors", anchor=CENTER, width=120)
RapsvsHeatTable.column("Stat", anchor=CENTER, width=80)
RapsvsHeatTable.column("Miami Heat", anchor=CENTER, width=120)

#Create headings
RapsvsHeatTable.heading("#0", text="Label", anchor=W)
RapsvsHeatTable.heading("Toronto Raptors", text=TNTor, anchor=CENTER)
RapsvsHeatTable.heading("Stat", text="Stat", anchor=CENTER)
RapsvsHeatTable.heading("Miami Heat", text=TNMia, anchor=CENTER)

#Add Data
for i in range (2,25):
    RapsvsHeatTable.insert(parent='',index='end',iid=i,text="Parent",values=(RaptorsStats[i],Stats[i],HeatStats[i]))

#Place the table on Raptors vs Lakers tab/frame
RapsvsHeatTable.place(x=167,y=170)

#Win and Lose Buttons
def myClick():
    WorLLakersButton = Label(RapsvsLakers,text="Raptors Win",bg='chartreuse3',width=17)
    WorLLakersButton.place(x=250,y=475)

LakersResult = Button(RapsvsLakers,text='Run simulation of Game', bd='5', bg='red',fg='black',command=myClick)  
LakersResult.place(x=250,y=445) 

def myClick():
    WorLClipsButton = Label(RapsvsClips,text="Raptors Win",bg='chartreuse3',width=17)
    WorLClipsButton.place(x=250,y=475)

ClipsResult = Button(RapsvsClips,text='Run simulation of Game', bd='5', bg='red',fg='black',command=myClick)  
ClipsResult.place(x=250,y=445) 

def myClick():
    WorLHeatButton = Label(RapsvsHeat,text="Raptors Win",bg='chartreuse3',width=17)
    WorLHeatButton.place(x=250,y=475)

HeatResult = Button(RapsvsHeat,text='Run simulation of Game', bd='5', bg='red',fg='black',command=myClick)  
HeatResult.place(x=250,y=445) 

def myClick():
    WorLBucksButton = Label(RapsvsBucks,text="Raptors Win",bg='chartreuse3',width=17)
    WorLBucksButton.place(x=250,y=475)

BucksResult = Button(RapsvsBucks,text='Run simulation of Game', bd='5', bg='red',fg='black',command=myClick)  
BucksResult.place(x=250,y=445) 

#Exit Button
ExitButtonHomepage = Button(RaptorsMain,text='Exit', bd='5', bg='red',fg='black',command= root.destroy)  
ExitButtonHomepage.place(x=623, y=574) 

#ROOT
root.geometry("715x700")
root.title("NBA Predictions")
root.mainloop()

#STEPS NEEDED
#ACCESSING THE DATA
#DISPLAY THE DATA
#DISPLAY IN A TABLE
#SHOW THE WINNER AND LOSER