# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks

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
import Edit_Graph_Tab

#  
# def main(msg = None): 
#     print('msg: ', msg)#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#     root = Tk()
#     
#     root.title("Text Image Maker")
# 
#     tab_control = ttk.Notebook(root)
#     tab_control.grid(row=1, column=0, columnspan=999, rowspan=999, sticky='NESW')
#     
#     tab1 = Frame(tab_control)
#     tab2 = Frame(tab_control)
#     tab_control.add(tab1, text='Edit')
#     tab_control.add(tab2, text='Advanced Edit')
# 
#     tab_dict = {'edit': Edit_Tab.Edit_Tab(tab1),
#                 'advanced': Advanced_Tab.Advanced_Tab(tab2)}
#     
#     #let all the tabs use each other's member variables
#     for tab_name, tab in tab_dict.items():
#         tab.tabs = tab_dict
# 
#     print('build the image here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')#`````````````````````````````````````````````
#     root.mainloop()
#  
# if __name__ == '__main__':
#     main()
#     
    

def main(msg = None): 
    root = Tk()
    
    root.title("Text Image Maker")

    tab_control = ttk.Notebook(root)
    tab_control.grid(row=1, column=0, sticky='NESW')
    
    
    tab_tup_l = [('Edit Graph', 'edit_graph', Edit_Graph_Tab.Edit_Graph_Tab),
                 ('Edit'      , 'edit' , Edit_Tab.Edit_Tab),
                 ('Advanced'  , 'advanced'  , Advanced_Tab.Advanced_Tab)]
    
    tab_list = []
    tab_dict = {}
    for tab_tup in tab_tup_l:
        tab = Frame(tab_control)
        tab_control.add(tab, text=tab_tup[0])
        tab_dict[tab_tup[1]] = tab_tup[2](tab, tab_control)
        tab_list.append(tab)


    #let all the tabs use each other's member variables
    for tab_name, tab in tab_dict.items():
        tab.tabs = tab_dict

    # run functions where one tab needs to use another tab's
    # members after all tabs have been loaded,
    # but before any user input
    
    

    print('starting gui...')
    root.mainloop()
 
if __name__ == '__main__':
    print('in gui main')
    main()
    
    
    
    
    
    
    
    
    
    
    
    