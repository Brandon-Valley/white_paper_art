from tkinter.ttk import *
from tkinter import *







class Border_Width_WG():
    def __init__(self, 
                 master, 
                 init_border_tup,
                 max,
                 min,
                 sbox_width,
                 digits_only):
        
        self.t_sbox = Spinbox(master, from_ = min, to = max, width = sbox_width, validate = 'key', validatecommand = digits_only)#, command = log_rating)
    
if __name__ == '__main__':
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
    #from parent dir
    import GUI
    GUI.main()
    
    
    