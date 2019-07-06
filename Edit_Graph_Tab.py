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

class Edit_Graph_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
        Tab.Tab.__init__(self, master)

        self.paths_____widget_setup()

        self.grid_widgets()
        
        
    def paths_____widget_setup(self):
        self.paths_lf = LabelFrame(self.master, text = " Input / Output Paths: ")
        
        self.out_path_browse_wg = self.File_System_Browse_Widget_Group(self.paths_lf, 'Output Path', BROWSE_TB_WIDTH, 'dir', None, DEFAULT_OUT_PATH)
        
    def grid_widgets(self):
#         self.master.grid_columnconfigure(3, weight=1)
  
        # input Information
        self.paths_lf              .grid(column=1, row=1, sticky='NSWE', padx=5, pady=5, ipadx=5, ipady=5)
        self.out_path_browse_wg.lbl.grid(column=1, row=1)
        self.out_path_browse_wg.tb .grid(column=2, row=1)
        self.out_path_browse_wg.btn.grid(column=3, row=1)

        

        
if __name__ == '__main__':
    GUI.main()