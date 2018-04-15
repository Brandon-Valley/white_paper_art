from tkinter import *
from tkinter import ttk
# root = Tk()

# root.title("Text Image Maker")
# root.geometry('900x400') #1500x700 takes up aplmost the whole screen
# 
# 
# 
# e = ttk.Entry(root, width=20)
# e.pack()
# e.insert(0, 'widget')
# e.xview(2)
# 
# 
# e                   .grid(column=1, row=7)




def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')

a = Tk()
text = StringVar(a, value='qwertyuiopasdfghjklzxcvbnm1234567890')
b = ttk.Entry(a, textvariable=text)

b.bind('<Expose>', xview_event_handler)
b.grid(column=1, row=7)

a.mainloop()


