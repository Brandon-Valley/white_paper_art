# https://dzone.com/articles/python-gui-examples-tkinter-tutorial-like-geeks

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

import threading #need????????????????????????????????????????????????????????????????????????????????
from   threading import Thread
from queue import Queue

import time

# from logger import txt_logger

import build_image
import GUI_utils

#Tabs
import Edit_Tab
import Advanced_Tab


VAR_LOG_FILE_NAME           = 'variables.txt'
BUILD_IMAGE_IMMEDIATELY_KEY = 'build_image_immediately'


def build_gui(common_q):    
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

    # this is here to allow the image to be built outside this thread
    image_kwargs = tab_dict['edit'].build_kwargs()
    common_q.put(tab_dict['edit'].build_image_immeadiately)
    common_q.put(image_kwargs)

    root.mainloop()





        



#this whole thing needs to be cleaned up really bad!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def main(): 
    common_queue = Queue()
#     t1 = Thread(target=producer, args=(q,))
    
    Thread(target = build_gui, args = (common_queue,)).start()
#     print('after thread1: ', common_queue.get())#````````````````````````````````````````````````````````````````````````````````````````````````
#     common_queue.task_done()
#     print('after thread1: ', common_queue.get())#````````````````````````````````````````````````````````````````````````````````````````````````

    
    
    # if need to build image immediately, make 2 threads, 1 for the gui,
    # and one for building the image, need this so you don't have to wait forever
    # for the image to build before getting to see/interact with the gui
    
#     prev_vars = txt_logger.readVars(VAR_LOG_FILE_NAME)#````````````````````````````````````````````````````````````````````````````````````
      
    # if build_image_immeadiately == True
    if common_queue.get() == True:
        time.sleep(10)#````````````````````````````````````````````````````````````````````````````````````
        common_queue.task_done()
        print('more threading needed')#``````````````````````````````````````````````````````````````````````````````````````````````````````
#         img_kwargs = tab_dict['edit'].build_kwargs()#```````````````````````````````````````````````````````````````````
#         build_image.build_final_image(common_queue.get()) # image_kwargs  
#         img_kwargs = common_queue.get() ) #````````````````````````````````````````````````````````````````````````````````` 
          
#         Thread(target = build_image.build_final_image, args = common_queue.get()).start() # args = image_kwargs

          
        Thread(target = lambda: build_image.build_final_image(common_queue.get())).start()
    
    

    
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    