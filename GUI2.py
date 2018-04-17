from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk

import build_image
import GUI_utils



FILE_PATH_TEXT_BOX_WIDTH = 80


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

 
class Main_Window():        
    
    """location path is the home directory for everything 
       else, contents of location_text_box will be reflected in
       the contents / state of folder_name_text_box"""
    def location_setup(self):
        self.l_path = StringVar()
        self.location_lbl = Label(self.master, text="Location: ")

        #if focus leaves location_text_box while ending in a \, folder_name_text_box should be enabled if not already
        def enable_folder_name_text_box_if_needed(event):
            if GUI_utils.get_last_path_var(self.location_text_box.get()) == '':
                self.create_new_folder_cbtn_sel.set(1) 
                self.update_folder_name_text_box()
#                 
        self.location_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        self.location_text_box.insert(END, GUI_utils.get_current_dir_path()) #default
        
        self.location_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
        
        #update folder name text box any time any of the following keys are pressed
        self.location_text_box.bind("<KeyRelease>", self.update_folder_name_text_box)
        self.location_text_box.bind("<KeyRelease-BackSpace>", self.update_folder_name_text_box)
        self.location_text_box.bind("<KeyRelease-Delete>", self.update_folder_name_text_box)
        self.location_text_box.bind("<KeyRelease-space>", self.update_folder_name_text_box)
        
        #update any time focus leaves text box, meant to help make sure that if you leave
        #location_text_box ending in a \, new_folder_text_box will enable itself if disabled
        self.location_text_box.bind("<FocusOut>", enable_folder_name_text_box_if_needed)
             
        def location_browse_btn_clk():
            #get file path and place it in text box
            dir = filedialog.askdirectory()
            self.location_text_box.delete(0, "end")
            self.location_text_box.insert(END, dir)
            
            self.update_folder_name_text_box()
            
        self.location_browse_btn = Button(self.master, text="Browse...", command = location_browse_btn_clk)
        
    #create new folder check button #should this be put inside something else / somewhere else????????????????????????????
    def update_folder_name_text_box(self, event = None):#changes state and contents of folder name
        self.folder_name_text_box.configure( state = 'normal' )
        self.folder_name_text_box.delete(0, "end")
        
        if self.create_new_folder_cbtn_sel.get() == 0:
            self.folder_name_text_box.insert(END, GUI_utils.get_last_path_var(self.location_text_box.get()))
            self.folder_name_text_box.configure( state = 'disabled' )


    """folder_name_text_box used to get name of new folder
       to be make and put at the end of location path,
        can be enabled/disabled with create_new_folder_cbutn 
        as well as from conditions inside location_text_box"""
    def folder_name_setup(self):
        #folder name text box 
        self.folder_name_text_box = Entry(self.master,width=20)
        self.folder_name_lbl = Label(self.master, text="Folder Name: ")
        self.folder_name_text_box = Entry(self.master,width=20)
        
        self.create_new_folder_cbtn_sel = IntVar(value = 1)#value sets default
        self.create_new_folder_cbtn = Checkbutton(text="Create New Folder", variable=self.create_new_folder_cbtn_sel, command = self.update_folder_name_text_box)
        self.update_folder_name_text_box() #disabled folder name by default if create_new_folder_cbtn is 0 by default
    
    
    
    def __init__(self, master):
#         tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Text Image Maker")
        self.master.geometry('900x400') #1500x700 takes up aplmost the whole screen


        self.location_setup()
        self.folder_name_setup()
        
#         self.folder_name_text_box = Entry(self.master,width=20)
        
        
        
        
#         #folder name text box 
#         folder_name_lbl = Label(self.master, text="Folder Name: ")
#         self.folder_name_text_box = Entry(self.master,width=20)
        
        
        

        
#         self.create_new_folder_cbtn_sel = IntVar(value = 1)#value sets default
#         create_new_folder_cbtn = Checkbutton(text="Create New Folder", variable=self.create_new_folder_cbtn_sel, command = self.update_folder_name_text_box)
#         self.update_folder_name_text_box() #disabled folder name by default if create_new_folder_cbtn is 0 by default
        
         
         
        #text file path text box
        input_text_file_path_lbl = Label(self.master, text="Text File Input: ")
        input_text_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        input_text_file_path_text_box.insert(END, GUI_utils.get_defalt_text_file_path()) #default
             
        def input_text_file_path_clk():
            file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
            input_text_file_path_text_box.delete(0, "end")#clear text box
            input_text_file_path_text_box.insert(END, file)
            input_text_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
            
        input_text_file_path_btn = Button(self.master, text="Browse...", command = input_text_file_path_clk)
         
         
         
        #image file path text box
        input_img_file_path_lbl = Label(self.master, text="Image File Input: ")
        input_img_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)#, command = set_output_img_txt_box_contents())#modify output image contents every time this changes
        input_img_file_path_text_box.insert(END, GUI_utils.get_defalt_image_file_path()) #default
        input_img_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
         
        def input_img_file_path_clk():
            img_file = filedialog.askopenfilename(filetypes = (("Image files","*.jpg"),("Image files","*.png"),("all files","*.*")))
            input_text_file_path_text_box.delete(0, "end")#clear text box
            input_text_file_path_text_box.insert(END, img_file)
            input_text_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
             
        input_img_file_path_btn = Button(self.master, text="Browse...", command = input_img_file_path_clk)
         
         
         
        #font section labels
        font_lbl = Label(self.master, text="Font:")
        font_size_lbl = Label(self.master, text="Font Size:")
        maximize_font_size_lbl = Label(self.master, text="Maximize Font Size:")
        
         
         
        #font select drop-down #make read only??????????????????????????????????????????????????
        font_drop_down = Combobox(self.master)
        font_drop_down['values'] = GUI_utils.get_font_list()
        default_font_index = font_drop_down['values'].index(DEFAULT_FONT_NAME) #default
        font_drop_down.current(default_font_index) #set the selected item
    
    
    
        #font size spin box
    #     font_size_dims = GUI_utils.get_font_size_dimensions()
        font_size_sbox = Spinbox(self.master, from_ = 0, to = DEFAULT_MAX_FONT_SIZE, width = 5)#, state = "disabled")
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
        output_img_dim_lbl = Label(self.master, text="Image Dimensions:")
        slash_lbl = Label(self.master, text="/")
        output_img_dim_rat_num_sbox = Spinbox(self.master, from_ = 0, to = DEFAULT_MAX_IMAGE_DIM, width = 5) #numerator
        output_img_dim_rat_din_sbox = Spinbox(self.master, from_ = 0, to = DEFAULT_MAX_IMAGE_DIM, width = 5) #denominator
        output_img_dim_rat_num_sbox.delete(0, "end") 
        output_img_dim_rat_din_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        output_img_dim_rat_num_sbox.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_NUM) #default
        output_img_dim_rat_din_sbox.insert(END, DEFAULT_IMAGE_DIMENSION_RATIO_DIN) #default
        
    
    
        #image size spinbox
        img_size_lbl  = Label(self.master, text="Image Size:")
        img_size_sbox = Spinbox(self.master, from_ = DEFAULT_MIN_IMAGE_SIZE, to = DEFAULT_MAX_IMAGE_SIZE, width = 5)
        img_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        img_size_sbox.insert(0, DEFAULT_IMAGE_SIZE) #default 
    
    
    
        #image cord spinboxes
        img_cords_lbl   = Label(self.master, text="Image Position:")
        prnth_open_lbl  = Label(self.master, text="(")
        comma_lbl       = Label(self.master, text=",")
        prnth_close_lbl = Label(self.master, text=")")
        x_cord_sbox     = Spinbox(self.master, from_ = DEFAULT_MIN_IMG_POS_CORD, to = DEFAULT_MAX_IMG_POS_CORD, width = 3)
        y_cord_sbox     = Spinbox(self.master, from_ = DEFAULT_MIN_IMG_POS_CORD, to = DEFAULT_MAX_IMG_POS_CORD, width = 3)
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
        high_qual_rad_btn = Radiobutton(self.master,text='Show Low Quality Image (Fast)', value='low', variable = quality_selected, command = quality_rad_btn_sel)
        low_qual_rad_btn  = Radiobutton(self.master,text='Save High Quality Image (Slow)', value='high', variable = quality_selected, command = quality_rad_btn_sel)
    
    
    
        #output image path text box
        output_img_file_path_lbl = Label(self.master, text="Output Image File: ")
        output_img_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        output_img_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
        
        def set_output_img_txt_box_contents():
            output_img_file_path_text_box.insert(END, GUI_utils.get_defalt_output_img_file_path(input_img_file_path_text_box.get())) #default
             
        def output_file_path_clk():
            print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
            
        set_output_img_txt_box_contents()
        output_img_file_path_btn = Button(self.master, text="Browse...", command = output_file_path_clk)
    
    
    
        #build image button   
        def build_img_btn_clk():
            #read the current state of all arguments
            image_kwargs = {'input_text_file_path':     input_text_file_path_text_box.get(),
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
            build_image.build_img_test(image_kwargs)
        build_img_btn = Button(self.master, text="Build Image", command = build_img_btn_clk)
        
        
        
        
    #     blank_lbl = Label(self.master, text=" ")     
        
        
        #blank label (for spacing)
        blank_lbl = Label(self.master, text=" ")
        
        
        
        #physical GUI layout
        row_num = 10
    
        
        #location
        self.location_lbl                    .grid(column=1, row=row_num)
        self.location_text_box               .grid(column=2, row=row_num, columnspan = 3)
        self.location_browse_btn             .grid(column=5, row=row_num)
        
        row_num += 10
        
        #create new folder check button
        self.create_new_folder_cbtn          .grid(column=1, row=row_num)
        
        row_num += 10
        
        #folder_name
        self.folder_name_lbl                 .grid(column=1, row=row_num)
        self.folder_name_text_box            .grid(column=2, row=row_num)
        
        row_num += 10
        
        #input text file path
        input_text_file_path_lbl        .grid(column=1, row=row_num)
        input_text_file_path_text_box   .grid(column=2, row=row_num, columnspan = 3)
        input_text_file_path_btn        .grid(column=5, row=row_num)
         
        row_num += 10 
        
        #input image file path
        input_img_file_path_lbl         .grid(column=1, row=row_num)
        input_img_file_path_text_box    .grid(column=2, row=row_num, columnspan = 3)
        input_img_file_path_btn         .grid(column=5, row=row_num)
         
        row_num += 10
         
        #space between
        blank_lbl                       .grid(column=1, row=row_num)
        
        row_num += 10
        
        #font section labels
        font_lbl                        .grid(column=1, row=row_num)
        font_size_lbl                   .grid(column=2, row=row_num)
        
        row_num += 10 
        
        #font inputs
        font_drop_down                  .grid(column=1, row=row_num) 
        font_size_sbox                  .grid(column=2, row=row_num)  
        max_font_size_cbtn              .grid(column=4, row=row_num)
        
        row_num += 10 
        
        #space between
        blank_lbl                       .grid(column=1, row=row_num)
        
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
        output_img_file_path_text_box   .grid(column=2, row=row_num, columnspan = 3)
        output_img_file_path_btn        .grid(column=5, row=row_num)
        
        
        row_num += 10
        
        #build image button
        build_img_btn                   .grid(column=2, row=row_num)
         
def set_output_img_txt_box_contents(text_box, file_path):
#     output_img_file_path_text_box.insert(END, GUI_utils.get_defalt_output_img_file_path(input_img_file_path_text_box.get())) #default
    text_box.insert(END, GUI_utils.get_defalt_output_img_file_path(file_path)) #default
    
#makes xview (scrolling within an entry text box) work
def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')
         
 
def main(): 
    root = Tk()
    Main_Window(root)#.pack(fill="both", expand=True)
    
#     app = Main_Window(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    