from tkinter import *
from tkinter.ttk import *

import build_image
import GUI_utils


def build_img_btn_clk(image_args):
#     print(font_drop_down.get())
    print('in GUI, image_args: ', image_args)
    build_image.build_img_test(image_args)


def show_gui():
    
    #default arguments
    input_text_file_path = GUI_utils.get_defalt_text_file_path()
    input_img_file_path= GUI_utils.get_defalt_image_file_path()
    
    #initialize img_args
    img_args = {'input_text_file_path':           None,
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
    input_text_file_path_lbl = Label(window, text="Text File Input: ")
    input_text_file_path_text_box = Entry(window,width=10)
    input_text_file_path_text_box.insert(END, input_text_file_path)
    
    def input_text_file_path_clk():
        input_text_file_path = input_text_file_path_text_box.get()

    input_text_file_path_btn = Button(window, text="Directory", command = input_text_file_path_clk)
    
    
    #image file path text box
    input_img_file_path_lbl = Label(window, text="Text File Input: ")
    input_img_file_path_text_box = Entry(window,width=10)
    input_img_file_path_text_box.insert(END, input_img_file_path)
    
    def input_img_file_path_clk():
        input_img_file_path = input_img_file_path_text_box.get()

    input_img_file_path_btn = Button(window, text="Directory", command = input_img_file_path_clk)
    
    
    
    
    #font select drop-down
    font_drop_down = Combobox(window)#,text='First', value=1, variable=selected)
    font_drop_down['values']= GUI_utils.get_font_list()
    font_drop_down.current(0) #set the selected item
    
    

        
        
    #build image button
    build_img_btn = Button(window, text="Build Image", command = build_img_btn_clk(img_args))
    
    
    
    #input text file path
    input_text_file_path_lbl        .grid(column=0, row=0)
    input_text_file_path_text_box   .grid(column=1, row=0)
    input_text_file_path_btn        .grid(column=2, row=0)
    
    #input image file path
    input_img_file_path_lbl         .grid(column=0, row=1)
    input_img_file_path_text_box    .grid(column=1, row=1)
    input_img_file_path_btn         .grid(column=2, row=1)
    
    #font drop down
    font_drop_down                  .grid(column=0, row=3)
    
    #build image button
    build_img_btn                   .grid(column=2, row=4)
    

    
    
    window.mainloop()
    
    
    
    
    

    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()