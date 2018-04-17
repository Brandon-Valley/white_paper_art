import tkinter as tk  # python 3.x
# import Tkinter as tk # python 2.x

class Example(tk.Frame):
    def test_func(self):
        vcmd = (self.register(self.onValidate), '%P')
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.text = tk.Text(self, height=10, width=40)
        self.entry.pack(side="top", fill="x")
        self.text.pack(side="bottom", fill="both", expand=True)


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
        self.text.delete("1.0", "end")
        self.text.insert("end","OnValidate:\n")
        print("trying to get full: " , self.entry.get())
        print('P: ', P)
        
        self.entry.insert("end", P)

        self.text.insert("end","P='%s'\n" % P)

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