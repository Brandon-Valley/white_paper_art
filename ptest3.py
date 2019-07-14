from tkinter import *

def callback(sv):
    print (sv.get())
#     e.insert(END, 'i')

def btn_clk(event=None):
    e.insert(END, 'i')



root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()


btn = Button(root, text = 'Generate Edited Graph', command = btn_clk)

btn.pack()
root.mainloop()  