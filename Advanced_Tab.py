from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

import build_image
import GUI_utils
import GUI


COLOR_TUP_TB_WIDTH = 30
COLOR_DISPLAY_TB_WIDTH = 10

class Advanced_Tab():
    def __init__(self, master):
        self.master = master
        self.tabs = None
        
        self.output_background_color______widget_setup()
        
        self.grid_widgets()
#         lbl2 = Label(master, text= 'label2')
#         lbl2.grid(column=0, row=0)
#         
#         self.tb = Entry(self.master,width=20)
#         self.tb.grid(column=1, row=1)

    def change_color(self, tup_tb, color_tb):
        color = askcolor()
        print(color)
        print(color[0])
        
        tup_tb.configure(state = 'normal')
        color_tb.configure(state = 'normal')
        
        tup_tb.delete(0, "end")
        tup_tb.insert(END, str(color[0]))
        
        tup_tb.configure(state = 'readonly')
        color_tb.configure(state = 'readonly')


    def output_background_color______widget_setup(self):
        self.output_bgnd_clr_lbl = Label(self.master, text="Output Image Background Color: ")
        self.output_bgnd_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, state = 'readonly')
        self.output_bgnd_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        
#         def change_clr_btn_clk():
            
            
            
            
            #get file path and place it in text box
            
#             dir = filedialog.askdirectory()
#             self.location_tb.delete(0, "end")
#             self.location_tb.insert(END, dir)
#             
#             self.update_folder_name_tb()
            
        self.output_bgnd_clr_change_clr_btn = Button(self.master, text="Change Color", 
                command = lambda: GUI_utils.change_color(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb))
        
        
        

        

        
    def grid_widgets(self):
        
        row_num = 10
        
        #output_background_color
        self.output_bgnd_clr_lbl              .grid(column=1, row=row_num)
        self.output_bgnd_clr_tup_tb           .grid(column=2, row=row_num)
        self.output_bgnd_clr_display_tb       .grid(column=3, row=row_num)
        self.output_bgnd_clr_change_clr_btn   .grid(column=4, row=row_num)
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    GUI.main()