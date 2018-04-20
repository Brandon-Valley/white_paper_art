from tkinter import *

window = Tk()




frame = Frame(window)
frame.pack()


l_lbl = Label(frame, text="L")
r_lbl = Label(frame, text="R")
t_lbl = Label(frame, text="T")
b_lbl = Label(frame, text="B")



listNodes = Listbox(frame, width=20, height=20, font=("Helvetica", 12))
# listNodes.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listNodes.yview)
# scrollbar.pack(side="right", fill="y")

listNodes.config(yscrollcommand=scrollbar.set)

for x in range(100):
    listNodes.insert(END, str(x))
    


listNodes.grid(column=1, row=1)
scrollbar.grid(column=2, row=1, rowspan=1,  sticky=N+S+W)

l_lbl.grid(column=0, row=1)
r_lbl.grid(column=3, row=1)
t_lbl.grid(column=1, row=0)
b_lbl.grid(column=1, row=2)



window.mainloop()