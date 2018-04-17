# from Tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
# 
# root = Tk()
# 
# def key(event):
#     print ("pressed", repr(event.char))
# 
# 
# self.tb = Entry(root,width=20)
# self.tb2 = Entry(root,width=20)
# 
# 
# self.tb.bind("<Key>", key)
# 
# 
# self.tb.grid(column=2, row=3)
# self.tb2.grid(column=1, row=4)
# 
# root.mainloop()
# 
# 
# 







import tkinter as tk
 
class Demo1:
    def __init__(self, master):
        self.master = master
        
        self.tb = Entry(master,width=20)
        self.tb2 = Entry(master,width=20)
        
        
        self.tb.bind("<Key>", self.key)
        self.tb.bind("<BackSpace>", self.backspace)
        
        
        self.tb.grid(column=2, row=3)
        self.tb2.grid(column=1, row=4)
        
#         self.tb2.delete(0, "end")#clear text box
#         self.tb2.insert(END, "snfdcklsnfdjfnsolikn")


        
    def key(self, event):
        print ("pressed", repr(event.char))
        self.tb2.delete(0, "end")#clear text box
        self.tb2.insert(END, self.tb.get() + event.char)
    
    def backspace(self, event):
#         print ("pressed", repr(event.char))
        print("pressed backspace")
        temp_txt = self.tb2.get()[:-1]
        
        self.tb2.delete(0, "end")#clear text box
        self.tb2.insert(END, temp_txt)
        

         
 
def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()