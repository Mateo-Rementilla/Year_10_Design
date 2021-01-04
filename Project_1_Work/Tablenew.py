from tkinter import*

rows = []

for i in range(5): 
	cols = []
	for f in range(4): 
		e = Entry(relief=GROOVE)
		e.grid(row = i, column = j, sticky = NSEW)
		e.insert(END, '%d.%d'%(i,j))
		cols.append(e)
	rows.append(cols)

root.mainloop()