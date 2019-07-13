from tkinter.ttk import *
from tkinter import *

import os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..')) # to import from parent dir relative to this file

# from parent dir
from custom_widgets.RGB_Display_Entry import *





class Color_Select_WG():
    def __init__(   self, 
                    master,
                    lbl_txt,
                    default_rgb_tup,
                    btn_txt):
        
        self.lbl = Label(master, text = lbl_txt)
        
        self.rgbd_tb = RGB_Display_Entry(master)
        self.rgbd_tb.set_rgb(default_rgb_tup)
        
        def change_color():
            float_rgb_tup = colorchooser.askcolor()[0]
            
            if float_rgb_tup != None:
                self.rgbd_tb.set_rgb(float_rgb_tup)
        
        
        
        
        self.btn = Button(master, text=btn_txt, command = change_color)#, command = lambda: GUI_utils.change_color(self.bgnd_text_clr_tup_tb, self.bgnd_text_clr_display_tb))

                 
 
 
 
 
 
 
 
if __name__ == '__main__':
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..')) # to import from parent dir
    #from parent dir
    import GUI
    GUI.main()
    
    
    