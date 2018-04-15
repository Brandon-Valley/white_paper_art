from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import re

import build_image
import GUI_utils


DEFAULT_FONT_NAME = "cour"
DEFAULT_FONT_SIZE = 40

DEFAULT_IMAGE_DIMENSION_RATIO_NUM = 14
DEFAULT_IMAGE_DIMENSION_RATIO_DIN = 16

DEFAULT_MAX_FONT_SIZE = 999

DEFAULT_MIN_IMAGE_SIZE = 0
DEFAULT_MAX_IMAGE_SIZE = 999

DEFAULT_MAX_IMAGE_DIM = 999999

DEFAULT_IMAGE_SIZE = 100 #REALLY need to figure something out for this!!!!!!!!!!!


DEFAULT_MAX_IMG_POS_CORD = 999
DEFAULT_MIN_IMG_POS_CORD = -999

def show_gui():
    
    window = Tk()
    window.title("Text Image Maker")
    window.geometry('900x400') #1500x700 takes up aplmost the whole screen
     
    
    
    #Location path text box 
    location_lbl = Label(window, text="Location: ")
    location_text_box = Entry(window,width=80)
    location_text_box.insert(END, GUI_utils.get_current_dir_path()) #default
         
    def location_browse_btn_clk():
        dir = filedialog.askdirectory()
        location_text_box.delete(0, "end")#clear text box
        location_text_box.insert(END, dir)
        
    location_browse_btn = Button(window, text="Browse...", command = location_browse_btn_clk)
    
    
    
    #folder name text box 
    folder_name_lbl = Label(window, text="Folder Name: ")
    folder_name_text_box = Entry(window,width=20)
    
    
    
    #create new folder check button
    def create_new_folder_btn_clk():#changes state and contents of folder name
        #not using bool_to_state because depending on what state, configure needs to be called at different times
        if create_new_folder_sel.get() == 0:
            folder_name_text_box.delete(0, "end")
            cf_path = re.split(r'[\\/]', location_text_box.get())
            folder_name_text_box.insert(END, cf_path[-1])#location_text_box.get().split('\\')
            folder_name_text_box.configure( state = 'disabled' )
        else:
            folder_name_text_box.configure( state = 'normal' )
            folder_name_text_box.delete(0, "end")
    
    create_new_folder_sel = IntVar(value = 1)#value sets default
    create_new_folder_cbtn = Checkbutton(text="Create New Folder", variable=create_new_folder_sel, command = create_new_folder_btn_clk)
    create_new_folder_btn_clk() #disabled folder name by default if create_new_folder_cbtn is 0 by default
    
     
     
    #text file path text box
    input_text_file_path_lbl = Label(window, text="Text File Input: ")
    input_text_file_path_text_box = Entry(window,width=20)
    input_text_file_path_text_box.insert(END, GUI_utils.get_defalt_text_file_path()) #default
         
    def input_text_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
        
    input_text_file_path_btn = Button(window, text="Browse...", command = input_text_file_path_clk)
     
     
     
    #image file path text box
    input_img_file_path_lbl = Label(window, text="Image File Input: ")
    input_img_file_path_text_box = Entry(window,width=10)
    input_img_file_path_text_box.insert(END, GUI_utils.get_defalt_image_file_path()) #default
     
    def input_img_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
         
    input_img_file_path_btn = Button(window, text="Browse...", command = input_img_file_path_clk)
     
     
     
    #font section labels
    font_lbl = Label(window, text="Font:")
    font_size_lbl = Label(window, text="Font Size:")
    maximize_font_size_lbl = Label(window, text="Maximize Font Size:")
    
     
     
    #font select drop-down #make read only??????????????????????????????????????????????????
    font_drop_down = Combobox(window)
    font_drop_down['values'] = GUI_utils.get_font_list()
    default_font_index = font_drop_down['values'].index(DEFAULT_FONT_NAME) #default
    font_drop_down.current(default_font_index) #set the selected item



    #font size spin box
#     font_size_dims = GUI_utils.get_font_size_dimensions()
    font_size_sbox = Spinbox(window, from_ = 0, to = DEFAULT_MAX_FONT_SIZE, width = 5)#, state = "disabled")
    font_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    font_size_sbox.insert(0, DEFAULT_FONT_SIZE) #default 



    #maximize font size check button
    #gets called each time you click the check button, changes state of font_size_sbox
    def max_font_size_btn_sel():
        font_size_sbox_state = GUI_utils.bool_to_state(max_font_size_sel.get())
        font_size_sbox.configure(state = font_size_sbox_state )
    
    max_font_size_sel = IntVar()
    max_font_size_cbtn = Checkbutton(text="Maximize Font Size", variable=max_font_size_sel, command = max_font_size_btn_sel)
    

    
    #match input image dimensions check box
    def use_input_img_dims_btn_sel():        
        img_dims_txt_boxes_state = GUI_utils.bool_to_state(use_input_img_dims_sel.get())
         
        #if using input image dimensions, change the test boxes to show the dimensions before disabling them
        if img_dims_txt_boxes_state == 'disabled':
            in_img_dims = GUI_utils.get_input_img_dims( input_img_file_path_text_box.get() )
            output_img_dim_rat_num_sbox.delete(0, "end")
            output_img_dim_rat_din_sbox.delete(0, "end")
            output_img_dim_rat_num_sbox.insert(END, in_img_dims['num'])
            output_img_dim_rat_din_sbox.insert(END, in_img_dims['din'])
        
        #disable or enable text boxes
        output_img_dim_rat_num_sbox.configure(state = img_dims_txt_boxes_state )
        output_img_dim_rat_din_sbox.configure(state = img_dims_txt_boxes_state )
    
    use_input_img_dims_sel = IntVar()
    match_input_image_dims_cbtn = Checkbutton(text="Use Input Image Dimensions", variable=use_input_img_dims_sel, command = use_input_img_dims_btn_sel)
    
    
    
    #image dimension spin boxes 
    output_img_dim_lbl = Label(window, text="Image Dimensions:")
    slash_lbl = Label(window, text="/")
    output_img_dim_rat_num_sbox = Spinbox(window, from_ = 0, to = DEFAULT_MAX_IMAGE_DIM, width = 5) #numerator
    output_img_dim_rat_din_sbox = Spinbox(window, from_ = 0, to = DEFAULT_MAX_IMAGE_DIM, width = 5) #denominator
    output_img_dim_rat_num_sbox.delete(0, "end") 
    output_img_dim_rat_din_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
    output_img_dim_rat_num_sbox.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_NUM) #default
    output_img_dim_rat_din_sbox.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_DIN) #default
    


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
    #gets called each time you click one of the radio buttons, changes font size options
    def quality_rad_btn_sel():
        if  quality_selected.get() == 'low':
            max_font_size_sel.set(0)
            font_size_sbox.configure(state = 'normal' )
        elif quality_selected.get() == 'high':
            max_font_size_sel.set(1)
            font_size_sbox.configure(state = 'disable' )
        else:
            print('something wrong with quality thing!!!!!!!!!!!!!!!!!!!!!!!!!')#```````````````````````````````````````````````

    quality_selected  = StringVar()
    quality_selected.set("low") #defalt
    high_qual_rad_btn = Radiobutton(window,text='Show Low Quality Image (Fast)', value='low', variable = quality_selected, command = quality_rad_btn_sel)
    low_qual_rad_btn  = Radiobutton(window,text='Save High Quality Image (Slow)', value='high', variable = quality_selected, command = quality_rad_btn_sel)



    #output image path text box
    output_img_file_path_lbl = Label(window, text="Output Image File: ")
    output_img_file_path_text_box = Entry(window,width=20)
    output_img_file_path_text_box.insert(END, GUI_utils.get_defalt_output_img_file_path()) #default
         
    def output_file_path_clk():
        print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
        
    output_img_file_path_btn = Button(window, text="Browse...", command = output_file_path_clk)



    #build image button   
    def build_img_btn_clk():
        #read the current state of all arguments
        img_args = {'input_text_file_path':     input_text_file_path_text_box.get(),
                    'image_file_path':          input_img_file_path_text_box.get(),
                    'font_name':                font_drop_down.get() + '.ttf',
                    'font_size':                font_size_sbox.get(),
                    'maximize_font_size':       max_font_size_sel.get(),
                    'output_image_dim_ratio':   GUI_utils.strs_to_int_ratio( output_img_dim_rat_num_sbox.get() , output_img_dim_rat_din_sbox.get() ),
                    'image_size':               img_size_sbox.get(),
                    'image_position_cords':     {'x': x_cord_sbox.get(), 'y': y_cord_sbox.get()},
                    'quality':                  quality_selected.get(),
                    'output_image_file_path':   output_img_file_path_text_box.get()}
        
        #build final image using arguments
        build_image.build_img_test(img_args)
    build_img_btn = Button(window, text="Build Image", command = build_img_btn_clk)
    
    
    
    
#     blank_lbl = Label(window, text=" ")     
    
    
    #blank label (for spacing)
    blank_lbl = Label(window, text=" ")
    
    
    
    #physical GUI layout
    row_num = 10

    
    #location
    location_lbl                    .grid(column=0, row=row_num)
    location_text_box               .grid(column=1, row=row_num, columnspan = 3)
    location_browse_btn             .grid(column=5, row=row_num)
    
    row_num += 10
    
    #create new folder check button
    create_new_folder_cbtn          .grid(column=0, row=row_num)
    
    row_num += 10
    
    #folder_name
    folder_name_lbl                 .grid(column=0, row=row_num)
    folder_name_text_box            .grid(column=1, row=row_num)
    
    row_num += 10
    
    #input text file path
    input_text_file_path_lbl        .grid(column=0, row=row_num)
    input_text_file_path_text_box   .grid(column=1, row=row_num, columnspan = 2)
    input_text_file_path_btn        .grid(column=3, row=row_num)
     
    row_num += 10 
    
    #input image file path
    input_img_file_path_lbl         .grid(column=0, row=row_num)
    input_img_file_path_text_box    .grid(column=1, row=row_num)
    input_img_file_path_btn         .grid(column=2, row=row_num)
     
    row_num += 10
     
    #space between
    blank_lbl                       .grid(column=0, row=row_num)
    
    row_num += 10
    
    #font section labels
    font_lbl                        .grid(column=0, row=row_num)
    font_size_lbl                   .grid(column=1, row=row_num)
    
    row_num += 10 
    
    #font inputs
    font_drop_down                  .grid(column=0, row=row_num) 
    font_size_sbox                  .grid(column=1, row=row_num)  
    max_font_size_cbtn              .grid(column=3, row=row_num)
    
    row_num += 10 
    
    #space between
    blank_lbl                       .grid(column=0, row=row_num)
    
    row_num += 10
    
    #image dimensions
    output_img_dim_lbl              .grid(column=1, row=row_num)
    output_img_dim_rat_num_sbox     .grid(column=2, row=row_num)
    slash_lbl                       .grid(column=3, row=row_num)
    output_img_dim_rat_din_sbox     .grid(column=4, row=row_num)
    match_input_image_dims_cbtn     .grid(column=5, row=row_num)
    
    row_num += 10
    
    #font size spinbox
    img_size_lbl                    .grid(column=1, row=row_num)
    img_size_sbox                   .grid(column=2, row=row_num)
    
    row_num += 10
    
    #image position cords
    img_cords_lbl                   .grid(column=1, row=row_num)
    prnth_open_lbl                  .grid(column=2, row=row_num)
    x_cord_sbox                     .grid(column=3, row=row_num)
    comma_lbl                       .grid(column=4, row=row_num)
    y_cord_sbox                     .grid(column=5, row=row_num)
    prnth_close_lbl                 .grid(column=6, row=row_num)
    
    row_num += 10
    
    #quality radio buttons
    high_qual_rad_btn               .grid(column=3, row=row_num - 1)
    low_qual_rad_btn                .grid(column=3, row=row_num)
    
    row_num += 10
    
    #output image file path text box
    output_img_file_path_lbl        .grid(column=1, row=row_num)
    output_img_file_path_text_box   .grid(column=2, row=row_num)
    output_img_file_path_btn        .grid(column=3, row=row_num)
    
    
    row_num += 10
    
    #build image button
    build_img_btn                   .grid(column=2, row=row_num)
    
    
    
    window.mainloop()
    print('after mainloop, should only het here after closing gui')
    
    
    
    
    

    
if __name__ == "__main__":
    print('GUI MAIN')
    show_gui()