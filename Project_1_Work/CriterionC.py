from tkinter import *
import requests
import json

url = "https://www.balldontlie.io/api/v1/teams"
balldontlie = requests.get(url)
data = json.loads(balldontlie.text)
'''
TNBos = (data["data"][1]["full_name"])
TNBky = (data["data"][2]["full_name"])
TNCha = (data["data"][3]["full_name"])
'''
root = Tk()

#Functions
def TotalData():  
    global content_array 
    for line in content: 
        content_array.append(line.strip().split(','))
        
'''
#TEXTBOX
class Table(Window): 
    def __init__(self,root): 
        for i in range(rows): 
            for j in range(columns): 
                self.e = Label(root, 
                    width=10, 
                    fg='black', 
                    font=('Arial',20,'bold'), 
                    borderwidth=2,
                    text=('Lakers'[i][0])
                    )
                self.e.place(x=300,y=300)

rows = 1 
columns = 1 


#TABLE
class Table(Window): 
    def __init__(self,root): 
        for i in range(rows): 
            for j in range(columns): 
                self.e = Label(root, 
                    width=10, 
                    fg='black', 
                    font=('Arial',20,'bold'), 
                    borderwidth=2,
                    text=('Lakers'[i][0])
                    )
                self.e.place(x=300,y=300)
 
Lakers = ['Lakers']

rows = len(Lakers)
columns = 3 
'''
#MAIN
myFile = open('TeamData.cvs.txt', 'r') 
content = myFile.readlines() 
content_array = []
'''
#Call for Table
Table(root) 
'''
#Call for Data
TotalData() 

#Single Team Array

SingleTeamData = 4
for i in range (4,len(content_array)):
    try:
        Dallas = content_array[i].index('Lakers')
        Raptors = content_array[i].index('Toronto Raptors')
        Lakers = content_array[i].index('Los Angeles Lakers')
    except:
        pass
app = Window(root)
root.wm_title("NBA Team Predictions")
root.geometry("815x800")
root.mainloop()