from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

from tkinter import *



import GUI
import Tab

BROWSE_TB_WIDTH = 80
DEFAULT_OUT_PATH = 'DEFAULT AOUTPUT_PTAH'
DEFAULT_IN_PATH = 'DEFAULT in_PTAH'

class Edit_Graph_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
        Tab.Tab.__init__(self, master)

        self.paths_____widget_setup()
        self.title_____widget_setup()

        self.grid_widgets()
        
        
    def paths_____widget_setup(self):
        self.paths_lf = LabelFrame(self.master, text = " Input / Output Paths: ")
        
        self.in_path_browse_wg  = self.File_System_Browse_WG(self.paths_lf, 'Input Path', BROWSE_TB_WIDTH, 'file', 
                                                             None, DEFAULT_IN_PATH, focus_tb_after_browse=False)
        self.out_path_browse_wg = self.File_System_Browse_WG(self.paths_lf, 'Output Path', BROWSE_TB_WIDTH, 'dir', 
                                                             None, DEFAULT_OUT_PATH, focus_tb_after_browse=True)
        
    def title_____widget_setup(self):
        self.title_lf = LabelFrame(self.master, text = " Graph Title: ")
        
        # title text box and label
        self.title_tb_lbl = Label(self.title_lf, text="Title: ")
        self.title_tb = Entry(self.title_lf)

        
    def grid_widgets(self):
#         self.master.grid_columnconfigure(3, weight=1)
  
        # input Information
        self.paths_lf              .grid(column=1, row=1, sticky='NSWE', padx=5, pady=5, ipadx=5, ipady=5)
        self.in_path_browse_wg.lbl .grid(column=1, row=1)
        self.in_path_browse_wg.tb  .grid(column=2, row=1)
        self.in_path_browse_wg.btn .grid(column=3, row=1, pady=5)
        self.out_path_browse_wg.lbl.grid(column=1, row=2)
        self.out_path_browse_wg.tb .grid(column=2, row=2)
        self.out_path_browse_wg.btn.grid(column=3, row=2)
        
        # title 
        self.title_lf              .grid(column=1, row=2, sticky='NSW', padx=5, pady=5, ipadx=5, ipady=5)
        self.title_tb_lbl          .grid(column=1, row=1)
        self.title_tb              .grid(column=2, row=1)



        

        
if __name__ == '__main__':
    GUI.main()