from tkinter import *

# create root window 
root = Tk() 
t = Table(root) 
root.mainloop()
  
class Table: 
      
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Label(root, width=10, fg='black', 
                               font=('Arial',20,'bold'), 
                                borderwidth=2,
                                relief="sunken")
                  
                self.e.grid(row=i, column=j, ) 
                self.e.configure(text = lst[i]) 
Table()
  
# take the data
lst = ['Stat',
       'Record', 
       'Win%', 
       'PTS', 
       'OR', 
       'DR',  
       'FG%',
       'FGA', 
       '3P%', 
       '3PA',  
       'FTM', 
       'FTA', 
       'FT%', 
       'AST', 
       'REB', 
       'BLK', 
       'PF'] 

# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = 1 
  
# Open window having dimension 100x100 
root.geometry('100x100')  
  
# Create a Button 
btn = Button(root, text = 'Click me !', bd = '5', 
                          command = root.destroy)  
  
# Set the position of button on the top of window.    
btn.pack(side = 'top')     
  
root.mainloop() 