from tkinter import *

master = Tk()

var = IntVar()


def print_var():
    print(var.get())
    

c = Checkbutton(master, text="Expand", variable=var, command = print_var)
c.pack()



mainloop()