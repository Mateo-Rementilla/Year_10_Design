from tkinter import *
  
  
class Table: 
      
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=20, fg='black', 
                               font=('Arial',20,'bold')) 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j]) 
  
# take the data
lst = [(('Stat',)),
       ('Record',), 
       ('Win%',), 
       ('PTS',), 
       ('OR',), 
       ('DR',),  
       ('FG%',),
       ('FGA',), 
       ('3P%',), 
       ('3PA',),  
       ('FTM',), 
       ('FTA',), 
       ('FT%',), 
       ('AST',), 
       ('REB',), 
       ('BLK',), 
       ('PF',)] 

# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0]) 
   
# create root window 
root = Tk() 
t = Table(root) 
root.mainloop() 