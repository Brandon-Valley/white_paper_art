from tkinter import *

root = Tk()
# sv = StringVar()
# 
# def callback():
#     print(sv.get())
#     print('bla')
#     return True
# 
# e = Entry(root, textvariable=sv, validate="key", validatecommand=callback)
# e.grid()
# 
# def callback2():
#     print(sv.get())
#     print('bla')
#     return True
# 
# # e = Entry(root)
# # e.grid()
# root.mainloop()




 
import tkinter as tk
 
class Demo1:
    def __init__(self, master):
        self.master = master
#         self.frame = tk.Frame(self.master)


        self.CONST_STR = "constant str"
         
        self.sv = StringVar()
         
        
        self.e = Entry(master, width = 30, textvariable=self.sv, validate="key", validatecommand=self.call_back)
        self.e.insert(END, "solifoi")
        self.later_var = "LATER_VAR IS HERE!"
        self.e.grid()
        
    def call_back(self):
        print('hi')
        self.CONST_STR = 'oooooooo'
        print(self.CONST_STR)
#         print(self.later_var)
        return True
             
#     def callback(self):
#         print(self.CONST_STR)
#         print(sv.get())
#         print('bla')
#         print(self.later_var)
#         return True
         

         
 
def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()