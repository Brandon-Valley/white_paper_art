from tkinter import *
from tkinter.ttk import *

import build_image
import GUI_utils


def build_img_btn_clk():
    print(font_drop_down.get())


def show_gui():
    
    img_args = {'text_file_path':           None,
                'image_file_path':          None,
                'max_font_size':            None,
                'font_name':                None,
                'desired_dimension_ratio':  None,
                'image_size':               None,
                'image_position_cords':     None,
                'output_image_file_path':   None}


    window = Tk()
    window.title("Text Image Maker")
    window.geometry('350x200')
    
    #text file path text box
    text_file_path_lbl = Label(window, text="Text File Input: ")
    text_file_path_lbl.grid(column=0, row=0)
    text_file_path_text_box = Entry(window,width=10)
    text_file_path_text_box.insert(END, 'default/path')
    def clicked():
        text_file_path = 'test/file/path'

    text_file_path_btn = Button(window, text="Directory", command=clicked)
    
    
    
    
    
    #font select drop-down
    font_drop_down = Combobox(window)#,text='First', value=1, variable=selected)
    font_drop_down['values']= GUI_utils.get_font_list()
    font_drop_down.current(0) #set the selected item
    
    

        
        
    #build image button
    build_img_btn = Button(window, text="Build Image", command = build_img_btn_clk)
    
    text_file_path_text_box.grid(column=1, row=0)
    text_file_path_btn.grid(column=2, row=0)
    
    font_drop_down.grid(column=0, row=3)
    
    build_img_btn.grid(column=3, row=3)
    

    
    build_image.build_img_test(img_args)
    window.mainloop()
    
    
    
    
    

    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()