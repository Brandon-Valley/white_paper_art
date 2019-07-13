from tkinter.ttk import *
from tkinter import *




WIDTH = 13



class RGB_Display_Entry(Entry):
    def __init__(self, master=None, cnf={}):
        Entry.__init__(self, master, cnf)
        self.configure(width = WIDTH)
        self.configure(justify = 'center')
        
        
        
    def set_rgb(self, rgb_tup):
        self.configure(state = 'normal')
     
        rgb_tup_str = "#%02x%02x%02x" % rgb_tup
     
        self.delete(0, "end")
        self.insert(END, str(rgb_tup))
     
#     #     tk_rgb = "#%02x%02x%02x" % round_color(color_tuple)#(0, 0, 0)
#         tk_rgb = tk_color(color_tuple)
#      
#         color_tb.configure(readonlybackground = tk_rgb)
        tk_rgb = "#%02x%02x%02x" % rgb_tup

        self.configure(readonlybackground = tk_rgb)
        self.configure(state = 'readonly')
        
    
    
if __name__ == '__main__':
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..')) # to import from parent dir
    #from parent dir
    import GUI
    GUI.main()
    
    
    