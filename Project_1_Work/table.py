from tkinter import *
  
  
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

   
# create root window 
root = Tk() 
t = Table(root) 
root.mainloop()






















































