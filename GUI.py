from tkinter import *
from tkinter.ttk import *

import build_image
import GUI_utils


# def build_img_btn_clk(image_args):
# # #     print(font_drop_down.get())
# # #     print('in GUI, image_args: ', image_args)
# #     build_image.build_img_test(image_args)
#     print('out of build_image')


    

    
    
    
DEFAULT_FONT_NAME = "cour"
DEFAULT_FONT_SIZE = 40



def show_gui():
    
    window = Tk()
    window.title("Text Image Maker")
    window.geometry('350x200')
     
     
    #text file path text box
    input_text_file_path_lbl = Label(window, text="Text File Input: ")
    input_text_file_path_text_box = Entry(window,width=10)
    input_text_file_path_text_box.insert(END, GUI_utils.get_defalt_text_file_path()) #default
         
    def input_text_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
        
    input_text_file_path_btn = Button(window, text="Directory", command = input_text_file_path_clk)
     
     
     
    #image file path text box
    input_img_file_path_lbl = Label(window, text="Image File Input: ")
    input_img_file_path_text_box = Entry(window,width=10)
    input_img_file_path_text_box.insert(END, GUI_utils.get_defalt_image_file_path()) #default
     
    def input_img_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
         
    input_img_file_path_btn = Button(window, text="Directory", command = input_img_file_path_clk)
     
     
     
    #font section labels
    font_lbl = Label(window, text="Font:")
    font_size_lbl = Label(window, text="Font Size:")
    maximize_font_size_lbl = Label(window, text="Maximize Font Size:")
    
     
     
    #font select drop-down #make read only??????????????????????????????????????????????????
    font_drop_down = Combobox(window)
    font_drop_down['values'] = GUI_utils.get_font_list()
    default_font_index = font_drop_down['values'].index(DEFAULT_FONT_NAME) #default
    font_drop_down.current(default_font_index) #set the selected item


    #font size spinbox
    font_size_dims = GUI_utils.get_font_size_dimensions()
    font_size_sbox = Spinbox(window, from_ = font_size_dims['min'], to = font_size_dims['max'], width = 5)#, state = "disabled")
    font_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    font_size_sbox.insert(0, DEFAULT_FONT_SIZE) #default 

    font_size_sbox.configure(state='disabled')
    font_size_sbox.configure(state='normal')
#     self.ent.configure(state='disabled')
#     '   # Disable the button.
    

    #build image button   
    def build_img_btn_clk():
        #read the current state of all arguments
        img_args = {'input_text_file_path':     input_text_file_path_text_box.get(),
                    'image_file_path':          input_img_file_path_text_box.get(),
                    'font_name':                font_drop_down.get() + '.ttf',
                    'font_size':                font_size_sbox.get(),
                    'desired_dimension_ratio':  None,
                    'image_size':               None,
                    'image_position_cords':     None,
                    'output_image_file_path':   None}
        
        #build final image using arguments
        build_image.build_img_test(img_args)
    
    build_img_btn = Button(window, text="Build Image", command = build_img_btn_clk)
    
    
    #blank label (for spacing)
    blank_lbl = Label(window, text=" ")
    
    #input text file path
    input_text_file_path_lbl        .grid(column=0, row=0)
    input_text_file_path_text_box   .grid(column=1, row=0)
    input_text_file_path_btn        .grid(column=2, row=0)
     
    #input image file path
    input_img_file_path_lbl         .grid(column=0, row=1)
    input_img_file_path_text_box    .grid(column=1, row=1)
    input_img_file_path_btn         .grid(column=2, row=1)
     
    #space between
    blank_lbl                        .grid(column=0, row=2)
    
    #font section labels
    font_lbl                        .grid(column=0, row=3)
    font_size_lbl                   .grid(column=1, row=3)
    
    #font inputs
    font_drop_down                  .grid(column=0, row=4) 
    font_size_sbox                  .grid(column=1, row=4)
    
    #build image button
    build_img_btn.grid(column=2, row=9)
    
    
    window.mainloop()
    print('after mainloop, should only het here after closing gui')
    
    
    
    
    

    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()