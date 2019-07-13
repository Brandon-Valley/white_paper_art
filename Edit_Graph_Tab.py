
from tkinter.ttk import *
from tkinter import *

import font_tools
from GUI_tools import Tab
from GUI_tools.custom_widgets.RGB_Display_Entry import *


BROWSE_TB_WIDTH = 80
DEFAULT_OUT_PATH = 'DEFAULT AOUTPUT_PTAH'
DEFAULT_IN_PATH = 'DEFAULT in_PTAH'
DEFAULT_TITLE_FONT_SIZE = 25
DEFAULT_FONT_NAME = "LiberationMono-Bold"
DEFAULT_TITLE_RGB_TUP = (255,255,255)


class Edit_Graph_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
        Tab.Tab.__init__(self, master)

        self.paths_____widget_setup()
        self.title_____widget_setup()
        self.graph_colors_____widget_setup()

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
        
        
        self.font_wg = self.Font_Config_WG(self.title_lf)
        self.font_wg = self.Font_Config_WG(self.title_lf, fonts_dir_path=font_tools.FONTS_PATH, default_font_size=DEFAULT_TITLE_FONT_SIZE,
                                           default_font=DEFAULT_FONT_NAME)
        
#         self.title_color_rgbd = RGB_Display_Entry(self.title_lf)
#         self.title_color_rgbd.set_rgb((255,255,255))
        
        self.title_color_wg = self.Color_Select_WG(self.title_lf, lbl_txt = 'Title Color:', default_rgb_tup = DEFAULT_TITLE_RGB_TUP)

#         

    def graph_colors_____widget_setup(self):
        self.graph_colors_lf = LabelFrame(self.master, text = " Graph Colors: ")

        self.invert_clrs_cbtn_sel = IntVar(value = 1) #default to value
        self.invert_clrs_cbtn = Checkbutton(self.graph_colors_lf, text="Invert Colors:", variable=self.invert_clrs_cbtn_sel)
    
    def grid_widgets(self):
        self.master.grid_columnconfigure(2, weight=1)
  
        # input Information
        self.paths_lf              .grid(column=1, row=1, sticky='NSW', padx=5, pady=5, ipadx=5, ipady=5, columnspan=2)
#         self.paths_lf.grid_columnconfigure(1, weight=1)
        self.in_path_browse_wg.lbl .grid(column=1, row=1)
        self.in_path_browse_wg.tb  .grid(column=2, row=1)
        self.in_path_browse_wg.btn .grid(column=3, row=1, pady=5)
        self.out_path_browse_wg.lbl.grid(column=1, row=2)
        self.out_path_browse_wg.tb .grid(column=2, row=2)
        self.out_path_browse_wg.btn.grid(column=3, row=2)
        
        # title 
        self.title_lf              .grid(column=1, row=2, sticky='NSWE', padx=5, pady=5, ipadx=5, ipady=5)
        self.title_tb_lbl          .grid(column=1, row=1)
        self.title_tb              .grid(column=2, row=1, sticky='W', columnspan = 2)
        self.font_wg.sbox_lbl      .grid(column=1, row=2)
        self.font_wg.sbox          .grid(column=2, row=2, sticky='W')
        self.font_wg.cbox_lbl      .grid(column=1, row=3)
        self.font_wg.cbox          .grid(column=2, row=3, sticky='W', columnspan = 2)
        self.title_color_wg.lbl    .grid(column=1, row=4            , pady=5)
        self.title_color_wg.rgbd_tb.grid(column=2, row=4, sticky='W', pady=5)
        self.title_color_wg.btn    .grid(column=3, row=4, sticky='W', pady=5)
        
        # graph colors
        self.graph_colors_lf       .grid(column=2, row=2, sticky='NW', padx=5, pady=5, ipadx=5, ipady=5)
        self.invert_clrs_cbtn      .grid(column=1, row=1)

        
if __name__ == '__main__':
    import GUI
    GUI.main()