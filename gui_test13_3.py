# from Tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


import tkinter as tk
 
class Demo1:
    def __init__(self, master):
        self.master = master
        
        self.tb = Entry(master,width=20)
        self.tb2 = Entry(master,width=20)
        
        
        self.tb.bind("<KeyRelease>", self.key)
        self.tb.bind("<KeyRelease-BackSpace>", self.backspace)
        
        
        self.tb.grid(column=2, row=3)
        self.tb2.grid(column=1, row=4)

        
    def key(self, event):
        print ("pressed", repr(event.char))
        self.tb2.delete(0, "end")#clear text box
        self.tb2.insert(END, self.tb.get() + event.char)
    
    def backspace(self, event):
#         print ("pressed", repr(event.char))
        print("pressed backspace")
        temp_txt = self.tb2.get()[:-1]
        
        self.tb2.delete(0, "end")#clear text box
#         self.tb2.insert(END, temp_txt)
        self.tb2.insert(END, self.tb2.get())
        
        
import time
def t_print():
    print('print t1...')
    time.sleep(1)
    print('t2')
        
 
def main(): 
    root = tk.Tk()
    app = Demo1(root)
    
    
    root.after(54, t_print)  # add_letter will run as soon as the mainloop starts.

    root.mainloop()
 
if __name__ == '__main__':
    main()