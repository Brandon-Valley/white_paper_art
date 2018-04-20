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
import Tab


COLOR_TUP_TB_WIDTH = 13
COLOR_DISPLAY_TB_WIDTH = 10

DEFAULT_OUTPUT_IMAGE_BACKGROUND_COLOR = (0, 0, 0)
DEFAULT_BACKGROUND_TEXT_COLOR = (255, 255, 255)

TEST_COLOR_LIST = [(2,3,4),
                   (44,55,66),
                   (32,76,90),
                   (225,0,0),
                   (0,0,0),
                   (255,0,255),
                   (255, 255,255),
                   (225,225,0)]


class Advanced_Tab(Tab.Tab):
    def __init__(self, master):
        Tab.Tab.__init__(self, master)
        
        self.output_background_color______widget_setup()
        self.background_text_color______widget_setup()
        self.input_image_background_color______widget_setup()
        
        self.grid_widgets()



    def output_background_color______widget_setup(self):
        self.output_bgnd_clr_lbl = Label(self.master, text="Output Image Background Color: ")
        self.output_bgnd_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, justify = 'center')
        self.output_bgnd_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        GUI_utils.apply_color_change(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb, DEFAULT_OUTPUT_IMAGE_BACKGROUND_COLOR)#default, sets to readonly
            
        self.output_bgnd_clr_change_clr_btn = Button(self.master, text="Change Color", 
                command = lambda: GUI_utils.change_color(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb))
        
    def background_text_color______widget_setup(self):
        self.bgnd_text_clr_lbl = Label(self.master, text="Background Text Color: ")
        self.bgnd_text_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, justify = 'center')
        self.bgnd_text_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        GUI_utils.apply_color_change(self.bgnd_text_clr_tup_tb, self.bgnd_text_clr_display_tb, DEFAULT_BACKGROUND_TEXT_COLOR)#default, sets to readonly
            
        self.bgnd_text_clr_change_clr_btn = Button(self.master, text="Change Color", 
                command = lambda: GUI_utils.change_color(self.bgnd_text_clr_tup_tb, self.bgnd_text_clr_display_tb))
        
    def input_image_background_color______widget_setup(self):

        #input image background color list box
        self.in_img_bgnd_clr_lbox = Listbox(self.master, width=COLOR_TUP_TB_WIDTH, height=5)#, font=("Helvetica", 12))
        
        self.in_img_bgnd_clr_sbar = Scrollbar(self.master, orient="vertical")
        self.in_img_bgnd_clr_sbar.config(command=self.in_img_bgnd_clr_lbox.yview)
        
        self.in_img_bgnd_clr_lbox.config(yscrollcommand=self.in_img_bgnd_clr_sbar.set)
        
        for color_num in range(len(TEST_COLOR_LIST)):
            color = TEST_COLOR_LIST[color_num]
            self.in_img_bgnd_clr_lbox.insert(END, str(color))
            bg_color = GUI_utils.tk_color(color)
            font_color = GUI_utils.tk_color( GUI_utils.highest_contrast_label_color(color) )
            self.in_img_bgnd_clr_lbox.itemconfig(color_num, bg=bg_color, fg = font_color)
            

            
        

        


        

        
    def grid_widgets(self):
        blank_lbl = Label(self.master, text="") #for spacing 
        
        row_num = 10
        
        #output_background_color
        self.output_bgnd_clr_lbl              .grid(column=1, row=row_num)
        self.output_bgnd_clr_tup_tb           .grid(column=2, row=row_num)
        self.output_bgnd_clr_display_tb       .grid(column=3, row=row_num)
        self.output_bgnd_clr_change_clr_btn   .grid(column=4, row=row_num)
        
        row_num += 10
        
        #background text color
        self.bgnd_text_clr_lbl              .grid(column=1, row=row_num)
        self.bgnd_text_clr_tup_tb           .grid(column=2, row=row_num)
        self.bgnd_text_clr_display_tb       .grid(column=3, row=row_num)
        self.bgnd_text_clr_change_clr_btn   .grid(column=4, row=row_num)
        
        row_num += 10
        
        blank_lbl                           .grid(column=1, row=row_num)
        
        row_num += 10
        
        #input image background color
        self.in_img_bgnd_clr_lbox           .grid(column=2, row=row_num)
        self.in_img_bgnd_clr_sbar           .grid(column=3, row=row_num, sticky=N+S+W)
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    GUI.main()