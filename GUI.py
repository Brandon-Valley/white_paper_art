from tkinter import *
from tkinter.ttk import *

import build_image
import GUI_utils


DEFAULT_FONT_NAME = "cour"
DEFAULT_FONT_SIZE = 40

DEFAULT_IMAGE_DIMENSION_RATIO_NUM = 14
DEFAULT_IMAGE_DIMENSION_RATIO_DIN = 16

DEFAULT_MAX_FONT_SIZE = 999

DEFAULT_MIN_IMAGE_SIZE = 0
DEFAULT_MAX_IMAGE_SIZE = 999

DEFAULT_IMAGE_SIZE = 100 #REALLY need to figure something out for this!!!!!!!!!!!


DEFAULT_MAX_IMG_POS_CORD = 999
DEFAULT_MIN_IMG_POS_CORD = -999

def show_gui():
    
    window = Tk()
    window.title("Text Image Maker")
    window.geometry('800x400')
     
     
    #text file path text box
    input_text_file_path_lbl = Label(window, text="Text File Input: ")
    input_text_file_path_text_box = Entry(window,width=20)
    input_text_file_path_text_box.insert(END, GUI_utils.get_defalt_text_file_path()) #default
         
    def input_text_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
        
    input_text_file_path_btn = Button(window, text="Browse", command = input_text_file_path_clk)
     
     
     
    #image file path text box
    input_img_file_path_lbl = Label(window, text="Image File Input: ")
    input_img_file_path_text_box = Entry(window,width=10)
    input_img_file_path_text_box.insert(END, GUI_utils.get_defalt_image_file_path()) #default
     
    def input_img_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
         
    input_img_file_path_btn = Button(window, text="Browse", command = input_img_file_path_clk)
     
     
     
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
#     font_size_dims = GUI_utils.get_font_size_dimensions()
    font_size_sbox = Spinbox(window, from_ = 0, to = DEFAULT_MAX_FONT_SIZE, width = 5)#, state = "disabled")
    font_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    font_size_sbox.insert(0, DEFAULT_FONT_SIZE) #default 



    #maximize font size radio buttons
    #gets called each time you click one of the radio buttons, changes state of font_size_sbox
    def font_size_radio_btn_sel():
        font_size_sbox_state = GUI_utils.bool_to_state(font_size_option_sel.get())
        font_size_sbox.configure(state = font_size_sbox_state )

    font_size_option_sel = IntVar()
    max_font_size_true_btn = Radiobutton(window,text='True', value=1, variable=font_size_option_sel, command = font_size_radio_btn_sel)
    max_font_size_false_btn = Radiobutton(window,text='False', value=0, variable=font_size_option_sel, command = font_size_radio_btn_sel)
    
    
    
    #output image dimension ratio text boxes and match input image dimensions option radio buttons
        #gets called each time you click one of the radio buttons, changes state of font_size_sbox
    def img_dims_radio_btn_sel():
        img_dims_txt_boxes_state = GUI_utils.bool_to_state(img_dims_option_sel.get())
        
        #if using input image dimensions, change the test boxes to show the dimensions before disabling them
        if img_dims_txt_boxes_state == 'disabled':
            in_img_dims = GUI_utils.get_input_img_dims( input_img_file_path_text_box.get() )
            output_img_dim_rat_num_text_box.delete(0, "end")
            output_img_dim_rat_din_text_box.delete(0, "end")
            output_img_dim_rat_num_text_box.insert(END, in_img_dims['num'])
            output_img_dim_rat_din_text_box.insert(END, in_img_dims['din'])
        
        #disable or enable text boxes
        output_img_dim_rat_num_text_box.configure(state = img_dims_txt_boxes_state )
        output_img_dim_rat_din_text_box.configure(state = img_dims_txt_boxes_state )

    img_dims_option_sel = IntVar()
    match_input_img_dims_btn = Radiobutton(window,text='Use Input Image Dimensions', value=1, variable=img_dims_option_sel, command = img_dims_radio_btn_sel)
    user_def_img_dims_btn    = Radiobutton(window,text='Image Dimensions: ', value=0, variable=img_dims_option_sel, command = img_dims_radio_btn_sel)
        
    slash_lbl = Label(window, text="/")
    output_img_dim_rat_num_text_box = Entry(window,width=10) #numerator
    output_img_dim_rat_din_text_box = Entry(window,width=10) #denominator
    output_img_dim_rat_num_text_box.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_NUM) #default
    output_img_dim_rat_din_text_box.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_DIN) #default
    


    #image size spinbox
    img_size_lbl  = Label(window, text="Image Size:")
    img_size_sbox = Spinbox(window, from_ = DEFAULT_MIN_IMAGE_SIZE, to = DEFAULT_MAX_IMAGE_SIZE, width = 5)
    img_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    img_size_sbox.insert(0, DEFAULT_IMAGE_SIZE) #default 



    #image cord spinboxes
    img_cords_lbl   = Label(window, text="Image Position:")
    prnth_open_lbl  = Label(window, text="(")
    comma_lbl       = Label(window, text=",")
    prnth_close_lbl = Label(window, text=")")
    x_cord_sbox     = Spinbox(window, from_ = DEFAULT_MIN_IMG_POS_CORD, to = DEFAULT_MAX_IMG_POS_CORD, width = 3)
    y_cord_sbox     = Spinbox(window, from_ = DEFAULT_MIN_IMG_POS_CORD, to = DEFAULT_MAX_IMG_POS_CORD, width = 3)
    x_cord_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    y_cord_sbox.delete(0, "end")
    x_cord_sbox.insert(0, 0) #default 
    y_cord_sbox.insert(0, 0) #default 
    


    #quality radio buttons
    #gets called each time you click one of the radio buttons, changes state of font_size_sbox
#     def font_size_radio_btn_sel():
#         font_size_sbox_state = GUI_utils.bool_to_state(font_size_option_sel.get())
#         font_size_sbox.configure(state = font_size_sbox_state )

    quality_selected  = StringVar()
    quality_selected.set("low")
    high_qual_rad_btn = Radiobutton(window,text='Show Low Quality Image (Fast)', value='low', variable = quality_selected)
    low_qual_rad_btn  = Radiobutton(window,text='Save High Quality Image (Slow)', value='high', variable = quality_selected)



    #build image button   
    def build_img_btn_clk():
        #read the current state of all arguments
        img_args = {'input_text_file_path':     input_text_file_path_text_box.get(),
                    'image_file_path':          input_img_file_path_text_box.get(),
                    'font_name':                font_drop_down.get() + '.ttf',
                    'font_size':                font_size_sbox.get(),
                    'maximize_font_size':       font_size_option_sel.get(),
                    'output_image_dim_ratio':   GUI_utils.strs_to_int_ratio( output_img_dim_rat_num_text_box.get() , output_img_dim_rat_din_text_box.get() ),
                    'image_size':               img_size_sbox.get(),
                    'image_position_cords':     {'x': x_cord_sbox.get(), 'y': y_cord_sbox.get()},
                    'quality':                  quality_selected.get(),
                    'output_image_file_path':   None}
        
        #build final image using arguments
        build_image.build_img_test(img_args)
    
    build_img_btn = Button(window, text="Build Image", command = build_img_btn_clk)
    
    
    
    #blank label (for spacing)
    blank_lbl = Label(window, text=" ")
    
    #input text file path
    input_text_file_path_lbl        .grid(column=0, row=0)
    input_text_file_path_text_box   .grid(column=1, row=0, columnspan = 2)
    input_text_file_path_btn        .grid(column=3, row=0)
     
    #input image file path
    input_img_file_path_lbl         .grid(column=0, row=1)
    input_img_file_path_text_box    .grid(column=1, row=1)
    input_img_file_path_btn         .grid(column=2, row=1)
     
    #space between
    blank_lbl                       .grid(column=0, row=2)
    
    #font section labels
    font_lbl                        .grid(column=0, row=3)
    font_size_lbl                   .grid(column=1, row=3)
    maximize_font_size_lbl          .grid(column=2, row=3)
    
    #font inputs
    font_drop_down                  .grid(column=0, row=4) 
    font_size_sbox                  .grid(column=1, row=4)
    max_font_size_true_btn          .grid(column=3, row=4)
    max_font_size_false_btn         .grid(column=5, row=4)
    
    #space between
    blank_lbl                       .grid(column=0, row=5)
    
    #image dimension ratio boxes
    match_input_img_dims_btn        .grid(column=0, row=8)
    user_def_img_dims_btn           .grid(column=0, row=9)
    output_img_dim_rat_num_text_box .grid(column=1, row=9)
    slash_lbl                       .grid(column=2, row=9)
    output_img_dim_rat_din_text_box .grid(column=3, row=9)
    
    #font size spinbox
    img_size_lbl                    .grid(column=1, row=10)
    img_size_sbox                   .grid(column=2, row=10)
    
    #image position cords
    img_cords_lbl                   .grid(column=1, row=13)
    prnth_open_lbl                  .grid(column=2, row=13)
    x_cord_sbox                     .grid(column=3, row=13)
    comma_lbl                       .grid(column=4, row=13)
    y_cord_sbox                     .grid(column=5, row=13)
    prnth_close_lbl                 .grid(column=6, row=13)
    
    #quality radio buttons
    high_qual_rad_btn               .grid(column=3, row=16)
    low_qual_rad_btn                .grid(column=3, row=17)
    
    
    #build image button
    build_img_btn                   .grid(column=2, row=20)
    
    
    window.mainloop()
    print('after mainloop, should only het here after closing gui')
    
    
    
    
    

    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()