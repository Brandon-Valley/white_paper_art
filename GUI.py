# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

import threading
from threading import Thread


import build_image
import GUI_utils

#Tabs
import Edit_Tab
import Advanced_Tab




#this whole thing needs to be cleaned up really bad!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def main(): 
#     build_image_immediately = GUI_utils.check_build_image_immediately()#``````````````````````````````````````````````````````````
    
    
    root = Tk()
    root.title("Text Image Maker")

    tab_control = ttk.Notebook(root)
    tab_control.grid(row=1, column=0, columnspan=999, rowspan=999, sticky='NESW')
    
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab_control.add(tab1, text='Edit')
    tab_control.add(tab2, text='Advanced Edit')

    tab_dict = {'edit': Edit_Tab.Edit_Tab(tab1),
                'advanced': Advanced_Tab.Advanced_Tab(tab2)}
    
    #let all the tabs use each other's member variables
    for tab_name, tab in tab_dict.items():
        tab.tabs = tab_dict
    
    print('in GUI:  self.build_image_immeadiately: ', tab_dict['edit'].build_image_immeadiately, type(tab_dict['edit'].build_image_immeadiately))#````````````````````````````````````````````````````````

#     if tab_dict['edit'].build_image_immeadiately == True:
#         print('BUILDING IMAGE IMEADIATELY RIGHT NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')#``````````````````````````````````````````````````````````````````````
#         image_kwargs = tab_dict['edit'].build_kwargs()
#         build_image.build_final_image(image_kwargs)
# 
# #     print('build the image here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')#`````````````````````````````````````````````
#     
#     
#     #why the hell are you doing that??????   why not just make a seperate thread to build the image while you also make the gui??????????? 1!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     def build_image_immeadiately_if_needed():
#         if True: #make this less dumb!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     #     if tab_dict['edit'].build_image_immeadiately == True:
#             print('BUILDING IMAGE IMEADIATELY RIGHT NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')#``````````````````````````````````````````````````````````````````````
#             image_kwargs = tab_dict['edit'].build_kwargs()
#             build_image.build_final_image(image_kwargs)
#     
#     
#     root.after(500, build_image_immeadiately_if_needed)  # add_letter will run as soon as the mainloop starts.
    
    
    
    # if need to build image immediately, make 2 threads, 1 for the gui,
    # and one for building the image, need this so you don't have to wait forever
    # for the image to build before getting to see/interact with the gui
    if tab_dict['edit'].build_image_immeadiately == True:
        print('threading needed')#``````````````````````````````````````````````````````````````````````````````````````````````````````
#         image_kwargs = tab_dict['edit'].build_kwargs()
#         build_image.build_final_image(image_kwargs)    
        
        Thread(target = root.mainloop).start()
#         Thread(target = lambda: build_image.build_final_image(image_kwargs)).start()
        
    else:
        root.mainloop()
    
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    