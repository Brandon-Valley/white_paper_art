
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
#!/usr/bin/python
 
from tkinter import *
from tkinter import ttk
 
 
main = Tk()
main.title('Notebook Demo')
main.geometry('500x500')
 
 
# gives weight to the cells in the grid
# rows = 0
# while rows < 50:
#     main.rowconfigure(rows, weight=1)
#     main.columnconfigure(rows, weight=1)
#     rows += 1
 
# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Tab1')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Tab2')
 
 
main.mainloop()