from tkinter import * #GUI package
from tkinter import ttk #For different frames
import requests #Requesting for Api data
import json #Changing the format to json
root = Tk() #Opens Window
root.geometry("500x500")
root.title("Testing")

url = "https://www.balldontlie.io/api/v1/teams" #Define url as the api link
balldontlie = requests.get(url) #Requesting for API data from the url
data = json.loads(balldontlie.text) #Define data as all of API infromation

#ApiTeamnames
TNTor = (data["data"][27]["full_name"]) #TeamNameTorontoRapotrs
TNCli = (data["data"][12]["full_name"]) #TeamNameLAClippers
TNMia = (data["data"][15]["full_name"]) #TeamNameMiamiHeat
TNMil = (data["data"][16]["full_name"]) #TeamNameMilwakeeBucks
TNLak = (data["data"][13]["full_name"]) #TeamNameLALakers

#Tables for different frames
my_tree =ttk.Treeview(root)

#Define our Columns 
my_tree['columns']=('Toronto Raptors', 'Stat', 'Los Angeles Lakers') 

#Format our Columns
my_tree.column("#0", width=0, stretch=NO) 
my_tree.column("Toronto Raptors", anchor=W, width=120)
my_tree.column("Stat", anchor=CENTER, width=80)
my_tree.column("Los Angeles Lakers", anchor=W, width=120)

#Create headings
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Toronto Raptors", text=TNTor, anchor=W)
my_tree.heading("Stat", text="Stat", anchor=CENTER)
my_tree.heading("Los Angeles Lakers", text=TNLak, anchor=W)

#Add Data
my_tree.insert(parent='',index='end',iid=0,text="Parent",values=("52-4","Record","53-1"),)

my_tree.place(x=100,y=100)

root.mainloop()
