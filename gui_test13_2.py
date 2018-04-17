# from Tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

root = Tk()

def key(event):
    print ("pressed", repr(event.char))


tb = Entry(root,width=20)
tb2 = Entry(root,width=20)


tb.bind("<Key>", key)


tb.grid(column=2, row=3)
tb2.grid(column=1, row=4)

root.mainloop()