import tkinter as tk


from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

from tkinter import *



DIGITS = '0123456789.-+'

class window2:
    def __init__(self, master1):
        self.master = master1
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()
        self.button2 = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.text1 = tk.Entry(self.panel2, validate = 'key', validatecommand = lambda: self.validate_input(DIGITS))# vcmd)
        self.text1.grid()
        self.text1.focus()

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
        
    def validate_input(self, allowed_chars):
        print('in validate input')
        
        
        def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
            
        vcmd = (self.master.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        
        
        

root1 = tk.Tk()
window2(root1)
root1.mainloop()