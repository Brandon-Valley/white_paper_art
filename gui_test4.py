import tkinter as tk  # python 3.x
# import Tkinter as tk # python 2.x

class Example(tk.Frame):
    def test_func(self):
        update_e2 = (self.register(self.onValidate), '%P')
        
        
        
#                 self.sv = StringVar()
#          
#         
#         self.e = Entry(master, width = 30, textvariable=self.sv, validate="key", validatecommand=self.call_back)
#         self.e.insert(END, "solifoi")
#         self.later_var = "LATER_VAR IS HERE!"
#         self.e.grid()
        
        
        
        
        self.l_path = tk.StringVar()
        
        self.e1 = tk.Entry(self, textvariable=self.l_path, validate="key", validatecommand=self.print_thing)#update_e2)
        self.e2 = tk.Entry(self)
#         self.text = tk.Text(self, height=10, width=40)
#         self.e1.pack(side="top", fill="x")
#         self.text.pack(side="bottom", fill="both", expand=True)
        self.e1                      .grid(column=1, row=2)
        self.e2                      .grid(column=2, row=3)


    def print_thing(self):
        print("hi")
        a = (self.register(self.onValidate), '%P')
        return True

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        self.test_func()


    def onValidate(self,P):
        print('in onValidate')
        self.e2.delete(0, "end")
#         self.e2.insert("end","OnValidate:\n")
#         print("trying to get full: " , self.e1.get())
#         print('P: ', P)
        
        self.e1.insert("end", P)
        self.e2.insert("end", self.e1.get() )

#         self.text.insert("end","P='%s'\n" % P)

        return True
#         # Disallow anything but lowercase letters
#         if S == S.lower():
#             return True
#         else:
#             self.bell()
#             return False

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()