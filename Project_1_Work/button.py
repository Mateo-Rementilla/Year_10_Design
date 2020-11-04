# import everything from tkinter module 
from tkinter import *    
  
# create a tkinter window 
root = Tk()               
  
# Open window having dimension 100x100 
root.geometry('100x100')  
  
# Create a Button 
btn = Button(root, text = 'Click me !', bd = '5', 
                          command = root.destroy)  
  
# Set the position of button on the top of window.    
btn.pack(side = 'top')     
  
root.mainloop() 

'''

import requests
import json

url = "https://www.balldontlie.io/api/v1/teams "
response = requests.get(url)
print (response.text) 

'''