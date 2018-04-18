from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

import build_image
import GUI_utils

#Tabs
import Edit_Tab
import Advanced_Tab

 
def main(): 
    root = Tk()
    
    root.title("Text Image Maker")

    tab_control = ttk.Notebook(root)
    tab_control.grid(row=1, column=0, columnspan=100, rowspan=100, sticky='NESW')
    
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab_control.add(tab1, text='Edit')
    tab_control.add(tab2, text='Advanced Edit')

    tab_dict = {'edit': Edit_Tab.Edit_Tab(tab1),
                'advanced': Advanced_Tab.Advanced_Tab(tab2)}
    
    #let all the tabs use each other's member variables
    for tab_name, tab in tab_dict.items():
        tab.tabs = tab_dict

    root.mainloop()
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    