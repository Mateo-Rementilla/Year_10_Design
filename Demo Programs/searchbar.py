import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app_FRAME=tk.Frame(app,relief=tk.GROOVE)    
app_FRAME.pack()


def clicked_on_arrow():
    print("see the list")

def var_changed():
    print("var changed")

_list = ["Toronto Raptors","Los Angeles Lakers","Miami Heat"]
_var = tk.StringVar()
_var.trace("w", lambda name, index, mode, x=_var: var_changed())

_COMBOBOX = ttk.Combobox(app_FRAME, postcommand=clicked_on_arrow(), values=_list, textvariable=_var)
_COMBOBOX.pack()
random_BUTTON = tk.Button(app_FRAME, text="the list can overlap over me !")
random_BUTTON.pack(fill=tk.BOTH, expand=True)

app.mainloop()
#This code (more complicated and custom) can't overlap (cause I'm not really sure how to implement it to create a custom widget without knowing the root frame) but it really help the user by visualising the list in real time:

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:25:59 2020

@author: aymeric LAUGEL
"""

import tkinter as tk

class Search_Bar:

    def create_new_list(self,string_given, string_list):
        new_list = []
        for string in string_list:
            if(len(string_given) <=len(string)):
                if(string.find(string_given) != -1):
                    new_list.append(string)
        return new_list      

    def update_display_list(self):
        if(self.listboxExist):
            self.m_LISTBOX.delete(0,tk.END)
            for string in self.m_list_to_display: self.m_LISTBOX.insert('end', string)
        else:
            print("listbox should exist...")


    def maybe_update_display_LISTBOX(self):
        possible_new_list_to_display = self.create_new_list(self.m_text_entry_object.get(), self.m_list)
        print()
        print("#############")
        print("LISTBOX exist:",self.listboxExist)
        print("var: |"+self.m_text_entry_object.get()+"|")
        print("old list:",self.m_list_to_display)