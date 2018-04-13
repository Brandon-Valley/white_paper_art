#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
# import Tkinter as tk

root = Tk()

class Principal():
    def __init__(self, *args, **kwargs):

        self.foo = StringVar()
        self.nac = IntVar()      
        ck1 = Checkbutton(root, text='Test',variable=self.nac, command=self.naccheck)
        ck1.pack()

        self.ent = Entry(root, width = 20, background = 'white', 
                            textvariable = self.foo, state = tk.DISABLED)       
        self.ent.pack()

    def naccheck(self):
        if self.nac.get() == 1:
            self.ent.configure(state='disabled')
        else:
            self.ent.configure(state='normal')       

app=Principal()
root.mainloop()