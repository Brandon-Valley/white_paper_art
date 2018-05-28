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
        self.input_background_color______widget_setup()
        
        self.grid_widgets()



    def output_background_color______widget_setup(self):
        self.output_bgnd_clr_lbl = Label(self.master, text="Output Image Background Color: ")
        self.output_bgnd_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, justify = 'center')
        self.output_bgnd_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        GUI_utils.apply_color_change(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb, DEFAULT_OUTPUT_IMAGE_BACKGROUND_COLOR)#default, sets to read only
            
        self.output_bgnd_clr_change_clr_btn = Button(self.master, text="Change Color", 
                command = lambda: GUI_utils.change_color(self.output_bgnd_clr_tup_tb, self.output_bgnd_clr_display_tb))
        
    def background_text_color______widget_setup(self):
        self.bgnd_text_clr_lbl = Label(self.master, text="Background Text Color: ")
        self.bgnd_text_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, justify = 'center')
        self.bgnd_text_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        GUI_utils.apply_color_change(self.bgnd_text_clr_tup_tb, self.bgnd_text_clr_display_tb, DEFAULT_BACKGROUND_TEXT_COLOR)#default, sets to read only
            
        self.bgnd_text_clr_change_clr_btn = Button(self.master, text="Change Color", 
                command = lambda: GUI_utils.change_color(self.bgnd_text_clr_tup_tb, self.bgnd_text_clr_display_tb))
        
    def input_background_color______widget_setup(self):

        def update_color_display_with_selected_color(): #event = None #dont remove until tested to make sure you dont need!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #update tuple text box
            self.input_bgnd_clr_tup_tb.configure(state = 'normal')
            self.input_bgnd_clr_tup_tb.delete(0, END)
            self.input_bgnd_clr_tup_tb.insert(END, self.input_bgnd_clr_lbox.get(ACTIVE))
            self.input_bgnd_clr_tup_tb.configure(state = 'readonly')
            #update display text box
            active_color = GUI_utils.str_to_tup(self.input_bgnd_clr_lbox.get(ACTIVE))
            GUI_utils.apply_color_change(self.input_bgnd_clr_tup_tb, self.input_bgnd_clr_display_tb, active_color)#default, sets to read only
            
            log_current_input_bgnd_clr_vars()
            print('this is what just got inserted correctly: %s    this is its type: %s' %(self.input_bgnd_clr_lbox.get(ACTIVE), type(self.input_bgnd_clr_lbox.get(ACTIVE))))#```````````````````````````````````````


        self.last_known_bgnd_clr_tup = StringVar() #this can probably be made not self!@@!@!!!!!!!!!!!!!!!!! maybe not?????????????????????????????????????
        def log_current_input_bgnd_clr_vars():
            print('self.input_bgnd_clr_tup_tb.get(): ', self.input_bgnd_clr_tup_tb.get())#````````````````````````````````````````````````````````
#             self.last_known_font_size = self.font_size_sbox.get()#`````````````````````````````````````````````````````````````````
            self.last_known_bgnd_clr_tup = self.input_bgnd_clr_tup_tb.get()
            print('last_known_bgnd_clr_tup: ', self.last_known_bgnd_clr_tup)#````````````````````````````````````````````````````````
            print('    type: ', type(self.last_known_bgnd_clr_tup))#````````````````````````````````````````````````````````


        #trim input background color check button
        def trim_input_bgnd_clr_cbtn_clk():
            print('cbtn clicked, last_known_bgnd_clr_tup: ', self.last_known_bgnd_clr_tup)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
            
            self.input_bgnd_clr_tup_tb.configure( state = 'normal' )
            self.input_bgnd_clr_tup_tb.delete(0, "end")
            
            if trim_input_bgnd_clr_cbtn_sel.get() == 0:
                self.input_bgnd_clr_sel_btn.configure( state = 'disabled' )
                self.input_bgnd_clr_tup_tb.configure( state = 'disabled' )
            else:
                self.input_bgnd_clr_sel_btn.configure( state = 'normal' )
                
                self.input_bgnd_clr_tup_tb.insert(0, self.last_known_bgnd_clr_tup) 
                self.input_bgnd_clr_tup_tb.configure(state = 'readonly')
                            
#             self.input_bgnd_clr_lbox.configure( state = 'normal' )
#             self.input_bgnd_clr_lbox.delete(0, "end")
#              
#             if self.max_font_size_sel.get() == 1:
#                 self.font_size_sbox.configure( state = 'disabled' )
#             else:
#                 self.font_size_sbox.insert(0, self.last_known_font_size)
        
        trim_input_bgnd_clr_cbtn_sel = IntVar(value = 1) #default to value
        self.trim_input_bgnd_clr_cbtn   = Checkbutton(self.master, text="Trim Input Background Color: ", variable=trim_input_bgnd_clr_cbtn_sel, command=trim_input_bgnd_clr_cbtn_clk)
        
        
        #input background color list box
        self.input_bgnd_clr_lbl         = Label(self.master, text="Input Background Color: ")
        self.input_bgnd_clr_lbox        = Listbox(self.master, width=COLOR_TUP_TB_WIDTH, height=5)#, font=("Helvetica", 12))
        self.input_bgnd_clr_sel_btn     = Button(self.master, text="Select", command = update_color_display_with_selected_color) 
        self.input_bgnd_clr_sbar        = Scrollbar(self.master, orient="vertical", command=self.input_bgnd_clr_lbox.yview)
        
        self.input_bgnd_clr_lbox.config(yscrollcommand=self.input_bgnd_clr_sbar.set)
        self.input_bgnd_clr_lbox.bind("<Return>",update_color_display_with_selected_color)
        self.input_bgnd_clr_lbox.bind("<Double-Button>",update_color_display_with_selected_color)
    
    



        #load colors
        for color_num in range(len(TEST_COLOR_LIST)):
            color = TEST_COLOR_LIST[color_num]
            self.input_bgnd_clr_lbox.insert(END, str(color))
            bg_color = GUI_utils.tk_color(color)
            font_color = GUI_utils.tk_color( GUI_utils.highest_contrast_label_color(color) )
            self.input_bgnd_clr_lbox.itemconfig(color_num, bg=bg_color, fg = font_color)
            
        #input background color display text boxes
        self.input_bgnd_clr_tup_tb = Entry(self.master,width=COLOR_TUP_TB_WIDTH, state = 'readonly', justify = 'center')
        self.input_bgnd_clr_display_tb = Entry(self.master,width=COLOR_DISPLAY_TB_WIDTH, state = 'readonly')
        
        update_color_display_with_selected_color()#sets default to first color in the list             #can these 2 be put together???????????   VVVVVVVVVVVV ???????????????
        log_current_input_bgnd_clr_vars()
        print('here')#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
        trim_input_bgnd_clr_cbtn_clk()


        
    def grid_widgets(self):
        blank_lbl = Label(self.master, text="") #for spacing 
        
        row_num = 10
        
        #output_background_color
        self.output_bgnd_clr_lbl                .grid(column=1, row=row_num)
        self.output_bgnd_clr_tup_tb             .grid(column=2, row=row_num)
        self.output_bgnd_clr_display_tb         .grid(column=3, row=row_num)
        self.output_bgnd_clr_change_clr_btn     .grid(column=4, row=row_num)
        
        row_num += 10
        
        #background text color
        self.bgnd_text_clr_lbl                  .grid(column=1, row=row_num)
        self.bgnd_text_clr_tup_tb               .grid(column=2, row=row_num)
        self.bgnd_text_clr_display_tb           .grid(column=3, row=row_num)
        self.bgnd_text_clr_change_clr_btn       .grid(column=4, row=row_num)
        
        row_num += 10
        
        blank_lbl                               .grid(column=1, row=row_num)
        
        row_num += 10
        
        #input image background color
        self.input_bgnd_clr_lbl                 .grid(column=1, row=row_num)
        self.input_bgnd_clr_lbox                .grid(column=2, row=row_num)
        self.input_bgnd_clr_sbar                .grid(column=3, row=row_num, sticky=N+S+W)
        self.input_bgnd_clr_sel_btn             .grid(column=2, row=row_num + 1)
        
        self.input_bgnd_clr_tup_tb              .grid(column=4, row=row_num)
        self.input_bgnd_clr_display_tb          .grid(column=5, row=row_num)
        
        self.trim_input_bgnd_clr_cbtn           .grid(column=2, row=row_num + 2)
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    GUI.main()