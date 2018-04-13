from tkinter import *
from tkinter.ttk import *

import build_image


def show_gui():

    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('350x200')
    combo = Combobox(window)
    combo['values']= (1, 2, 3, 4, 5, "Text")
    combo.current(1) #set the selected item
    combo.grid(column=0, row=0)
    
    build_image.build_img_test()
    window.mainloop()
    
    
    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()