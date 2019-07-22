from tkinter.ttk import *
from tkinter import *







class Border_Width_WG():
    def __init__(self, 
                 master, 
                 init_border_tup,
                 max,
                 min,
                 sbox_width,
                 
                 digits_only,
                 fresh_insert):
        
        self.l_sbox = Spinbox(master, from_ = min, to = max, width = sbox_width, validate = 'key', validatecommand = digits_only)#, command = log_rating)
        self.t_sbox = Spinbox(master, from_ = min, to = max, width = sbox_width, validate = 'key', validatecommand = digits_only)#, command = log_rating)
        self.r_sbox = Spinbox(master, from_ = min, to = max, width = sbox_width, validate = 'key', validatecommand = digits_only)#, command = log_rating)
        self.b_sbox = Spinbox(master, from_ = min, to = max, width = sbox_width, validate = 'key', validatecommand = digits_only)#, command = log_rating)
        
        fresh_insert(self.l_sbox, init_border_tup[0])
        fresh_insert(self.t_sbox, init_border_tup[1])
        fresh_insert(self.r_sbox, init_border_tup[2])
        fresh_insert(self.b_sbox, init_border_tup[3])
        
#         self.l_sbox.insert(0, init_border_tup[0]) #default (init_border_tup[0])
        
    
    # (left, top, right, bottom)
    def get(self):
        return (self.l_sbox.get(), self.t_sbox.get(), self.r_sbox.get(), self.b_sbox.get())
        
if __name__ == '__main__':
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
    #from parent dir
    import GUI
    GUI.main()
    
    
    