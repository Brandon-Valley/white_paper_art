from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

def clicked():
#     print(selected.get())
    print("sldkfnklsjrnh")
btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=3, row=0)
window.mainloop()