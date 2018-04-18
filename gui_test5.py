from tkinter import*

#from PIL import Image, ImageTk

#import time

#import os

class Welcome:
    def __init__(self, master):

        # let's store the master with the object
        self.master = master

        # you won't (usually) need the label objects again.  remove the storage
        Label(master, text="Enter Person's Name").grid(row=0)
        Label(master, text="Enter Starting Town").grid(row=1)
        Label(master, text="Enter Ending Town").grid(row=2)
        Label(master, text="Choose Transportation").grid(row=3)

        # You need to store the Entry, not the result of the grid method.
        self.e2 = Entry(master)
        self.e2.grid(row=1, column=2)

        self.e1 = Entry(master)
        self.e1.grid(row=0, column=2)

        self.e3 = Entry(master)
        self.e3.grid(row=2, column=2)

        self.e4 = Entry(master)
        self.e4.grid(row=3, column=2)

        # probably don't need the button objects preserved
        Button(master, text="Add Person", command=self.AddPerson).grid(row=5)
        Button(master, text="Quit").grid(row=6)
        Button(master, text="Graph").grid(row=7)

    def AddPerson(self):
        master = self.master
        window = Toplevel(master)
        Name = self.e1.get()
        StartTown = self.e2.get()
        EndTown = self.e3.get()
        Transportation = self.e4.get()

        self.list = Listbox(master)
        self.list.append(Name)
        self.list.grid(row=8)

root = Tk()
welcome_screen = Welcome(root)
root.mainloop()