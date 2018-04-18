from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

from tkinter import *

import build_image
import GUI_utils
import GUI


COLOR_TUP_TB_WIDTH = 13
COLOR_DISPLAY_TB_WIDTH = 10

DEFAULT_OUTPUT_IMAGE_BACKGROUND_COLOR = (0, 0, 0)

class Advanced_Tab():
    def __init__(self, master):
        self.master = master
        self.tabs = None
        
        self.output_background_color______widget_setup()
        
        self.grid_widgets()



    def output_background_color______widget_setup(self):
        self.output_bgnd_clr_lbl = Label(self.master, text="Output Image Background Color: ")
        self.output_bgnd_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, justify = 'center')
        self.output_bgnd_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        GUI_utils.apply_color_change(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb, DEFAULT_OUTPUT_IMAGE_BACKGROUND_COLOR)#default, sets to readonly
            
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