from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

import build_image
import GUI_utils
import GUI




class Advanced_Tab():
    def __init__(self, master):
        self.master = master
        self.tabs = None
        lbl2 = Label(master, text= 'label2')
        lbl2.grid(column=0, row=0)
        
        self.tb = Entry(self.master,width=20)
        self.tb.grid(column=1, row=1)
        
        
        
if __name__ == '__main__':
    GUI.main()