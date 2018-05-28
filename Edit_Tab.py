from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

# import tkinter as tk

import build_image
import GUI_utils
import GUI
import Tab



FILE_PATH_TEXT_BOX_WIDTH = 80


DEFAULT_FONT_NAME = "cour"
DEFAULT_FONT_SIZE = 44

DEFAULT_IMAGE_DIMENSION_RATIO_NUM = 14
DEFAULT_IMAGE_DIMENSION_RATIO_DIN = 16

DEFAULT_MAX_FONT_SIZE = 999

MIN_IMAGE_SIZE = 0
MAX_IMAGE_SIZE = 999

MAX_IMG_DIM = 999999

DEFAULT_IMAGE_SIZE = 100 #REALLY need to figure something out for this!!!!!!!!!!!


MAX_IMG_POS_CORD = 999
MIN_IMG_POS_CORD = -999

DEFAULT_OUTPUT_IMAGE_FILE_NAME = 'output.jpg'

# DEFAULT_NUM_DIM = 1
# DEFAULT_DIN_DIM = 1


 
class Edit_Tab(Tab.Tab):    
    def __init__(self, master):
        Tab.Tab.__init__(self, master)
    
        #setup widgets
        self.location______widgets_setup()
        self.folder_name______widgets_setup()
        self.input_text_file_path______widgets_setup()
        self.input_image_file_path______widgets_setup()
        self.font______widgets_setup()
        self.image_dimensions______widgets_setup()
        self.image_size______widgets_setup()
        self.image_cords______widgets_setup()
        self.quality______widgets_setup()
        self.output_image_path______widgets_setup()
        self.build_image______widgets_setup()
        
        self.grid_widgets() 

    def location______widgets_setup(self):
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
        
        #update other widget(s) any time the contents of location_text_box change
        self.bind_to_edit(self.location_text_box, self.location_text_box_updated)
        
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
        
    def location_text_box_updated(self, event = None):
        self.update_folder_name_text_box()
        self.update_output_image_file_text_box()
    
    #can I remove event param??????????????????????????????????????????????????????????????????????????????????????
    #create new folder check button #should this be put inside something else / somewhere else????????????????????????????
    def update_folder_name_text_box(self, event = None):#changes state and contents of folder name
        self.folder_name_text_box.configure( state = 'normal' )
        self.folder_name_text_box.delete(0, "end")
        
        if self.create_new_folder_cbtn_sel.get() == 0:
            self.folder_name_text_box.insert(END, GUI_utils.get_last_path_var(self.location_text_box.get()))
            self.folder_name_text_box.configure( state = 'disabled' )


    def folder_name______widgets_setup(self):
        #folder name text box 
        self.folder_name_text_box = Entry(self.master,width=20)
        self.folder_name_lbl = Label(self.master, text="Folder Name: ")
        self.folder_name_text_box = Entry(self.master,width=20)
        self.bind_to_edit(self.folder_name_text_box, self.update_output_image_file_text_box) 
        
        #create new folder check button
        self.create_new_folder_cbtn_sel = IntVar(value = 0)#value sets default
        self.create_new_folder_cbtn = Checkbutton(self.master, text="Create New Folder", variable=self.create_new_folder_cbtn_sel, command = self.update_folder_name_text_box)
        self.update_folder_name_text_box() #disabled folder name by default if create_new_folder_cbtn is 0 by default
    
    
  
    def input_text_file_path______widgets_setup(self):
        #text file path text box
        self.input_text_file_path_lbl = Label(self.master, text="Text File Input: ")
        self.input_text_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        self.input_text_file_path_text_box.insert(END, GUI_utils.get_defalt_text_file_path()) #default
             
        def input_text_file_path_clk():
            file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
            self.input_text_file_path_text_box.delete(0, "end")#clear text box
            self.input_text_file_path_text_box.insert(END, file)
            self.input_text_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
            
        self.input_text_file_path_btn = Button(self.master, text="Browse...", command = input_text_file_path_clk)
        
        
   
    def input_image_file_path______widgets_setup(self):
        #image file path text box
        self.input_img_file_path_lbl = Label(self.master, text="Image File Input: ")
        self.input_img_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        self.input_img_file_path_text_box.insert(END, GUI_utils.get_defalt_image_file_path()) #default
        self.input_img_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
         
        def input_img_file_path_clk():
            img_file = filedialog.askopenfilename(filetypes = (("Image files","*.jpg"),("Image files","*.png"),("all files","*.*")))
            self.input_text_file_path_text_box.delete(0, "end")#clear text box
            self.input_text_file_path_text_box.insert(END, img_file)
            self.input_text_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed #need???????????????????????????????????
             
        self.input_img_file_path_btn = Button(self.master, text="Browse...", command = input_img_file_path_clk)
    
        
   
    def font______widgets_setup(self):
        #font section labels
        self.font_lbl = Label(self.master, text="Font:")
        self.font_size_lbl = Label(self.master, text="Font Size:")
        maximize_font_size_lbl = Label(self.master, text="Maximize Font Size:")
        
        #font select drop-down 
        self.font_drop_down = Combobox(self.master, state = 'readonly')
        self.font_drop_down['values'] = GUI_utils.get_font_list()
        default_font_index = self.font_drop_down['values'].index(DEFAULT_FONT_NAME) #default
        self.font_drop_down.current(default_font_index) #set the selected item
    
        #font size spin box
        self.last_known_font_size = IntVar(value = DEFAULT_FONT_SIZE)
        
        def log_current_font_size(event = None):
            self.last_known_font_size = self.font_size_sbox.get()
            
        self.font_size_sbox = Spinbox(self.master, from_ = 0, to = DEFAULT_MAX_FONT_SIZE, width = 5,
                                       validate = 'key', validatecommand = self.digits_only, command = log_current_font_size)
        
        self.font_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        self.font_size_sbox.insert(0, DEFAULT_FONT_SIZE) #default 
        log_current_font_size()
        
        #record  current font size any time the contents of font_size_sbox change
        self.bind_to_edit(self.font_size_sbox, log_current_font_size)
        
        

        #maximize font size check button
        self.max_font_size_sel = IntVar()
        self.max_font_size_cbtn = Checkbutton(self.master, text="Maximize Font Size", variable=self.max_font_size_sel, command = self.max_font_size_btn_sel)
        
    #maximize font size check button click
    def max_font_size_btn_sel(self):#gets called each time you click the check button, changes state of self.font_size_sbox
        self.font_size_sbox.configure( state = 'normal' )
        self.font_size_sbox.delete(0, "end")
        
        if self.max_font_size_sel.get() == 1:
            self.font_size_sbox.configure( state = 'disabled' )
        else:
            self.font_size_sbox.insert(0, self.last_known_font_size)
    
    
    
    def image_dimensions______widgets_setup(self):
        #match input image dimensions check box
        last_known_num_val = IntVar(value = DEFAULT_IMAGE_DIMENSION_RATIO_NUM) #default
        last_known_din_val = IntVar(value = DEFAULT_IMAGE_DIMENSION_RATIO_DIN) #default
        
        def use_input_img_dims_btn_sel():        
            self.output_img_dim_num_sbox.configure(state = 'normal' )
            self.output_img_dim_din_sbox.configure(state = 'normal' )
            self.output_img_dim_num_sbox.delete(0, "end")
            self.output_img_dim_din_sbox.delete(0, "end")

            if use_input_img_dims_cbtn_sel.get() == 1:
                in_img_dims = GUI_utils.get_input_img_dims( self.input_img_file_path_text_box.get() )
                self.output_img_dim_num_sbox.insert(END, in_img_dims['num'])
                self.output_img_dim_din_sbox.insert(END, in_img_dims['din'])
                self.output_img_dim_num_sbox.configure(state = 'disabled' )
                self.output_img_dim_din_sbox.configure(state = 'disabled' )
            else:
                self.output_img_dim_num_sbox.insert(END, last_known_num_val.get())
                self.output_img_dim_din_sbox.insert(END, last_known_din_val.get())
        
        use_input_img_dims_cbtn_sel = IntVar()
        self.match_input_image_dims_cbtn = Checkbutton(self.master, text="Use Input Image Dimensions", variable=use_input_img_dims_cbtn_sel, command = use_input_img_dims_btn_sel)
        
 
        def log_current_dim_vals(event = None):
            last_known_num_val.set(self.output_img_dim_num_sbox.get())
            last_known_din_val.set(self.output_img_dim_din_sbox.get())            
        
        
        #image dimension spin boxes 
        self.output_img_dim_lbl = Label(self.master, text="Image Dimensions:")
        self.slash_lbl = Label(self.master, text="/")
        self.output_img_dim_num_sbox = Spinbox(self.master, from_=0, to=MAX_IMG_DIM, width=5, 
                                               validate='key', validatecommand=self.digits_only, command = log_current_dim_vals) #numerator
        self.output_img_dim_din_sbox = Spinbox(self.master, from_=0, to=MAX_IMG_DIM, width=5, 
                                               validate='key', validatecommand=self.digits_only, command = log_current_dim_vals) #denominator
        self.output_img_dim_num_sbox.delete(0, "end") 
        self.output_img_dim_din_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        self.output_img_dim_num_sbox.insert(END, last_known_num_val.get()) #default
        self.output_img_dim_din_sbox.insert(END, last_known_din_val.get()) #default
        
        log_current_dim_vals()
        
        #record current dimension values any time the contents of either dim spin box changes
        self.bind_to_edit(self.output_img_dim_num_sbox, log_current_dim_vals)
        self.bind_to_edit(self.output_img_dim_din_sbox, log_current_dim_vals)
        
    
    
    def image_size______widgets_setup(self):
        #image size spin box
        self.img_size_lbl  = Label(self.master, text="Image Size:")
        self.img_size_sbox = Spinbox(self.master, from_ = MIN_IMAGE_SIZE, to = MAX_IMAGE_SIZE, width = 5, validate='key', validatecommand=self.digits_only)
        self.img_size_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        self.img_size_sbox.insert(0, DEFAULT_IMAGE_SIZE) #default 
    
    
    
    def image_cords______widgets_setup(self):
        #image cord spin boxes
        self.img_cords_lbl   = Label(self.master, text="Image Position:")
        self.prnth_open_lbl  = Label(self.master, text="(")
        self.comma_lbl       = Label(self.master, text=",")
        self.prnth_close_lbl = Label(self.master, text=")")
        self.x_cord_sbox     = Spinbox(self.master, from_ = MIN_IMG_POS_CORD, to = MAX_IMG_POS_CORD, width = 3, validate='key', validatecommand=self.digits_only)
        self.y_cord_sbox     = Spinbox(self.master, from_ = MIN_IMG_POS_CORD, to = MAX_IMG_POS_CORD, width = 3, validate='key', validatecommand=self.digits_only)
        self.x_cord_sbox.delete(0, "end") #gets rid of 0 so the next line makes the default value 40 instead of 400
        self.y_cord_sbox.delete(0, "end")
        self.x_cord_sbox.insert(0, 0) #default 
        self.y_cord_sbox.insert(0, 0) #default 
    
    
    
    def quality______widgets_setup(self):
        #quality radio buttons
        def quality_rad_btn_sel():#changes font size options
            if  self.quality_selected.get() == 'low':
                self.max_font_size_sel.set(0)
                self.max_font_size_btn_sel()
            elif self.quality_selected.get() == 'high':
                self.max_font_size_sel.set(1)
                self.max_font_size_btn_sel()
    
        self.quality_selected  = StringVar()
        self.quality_selected.set("low") #default
        self.high_qual_rad_btn = Radiobutton(self.master,text='Show Low Quality Image (Fast)', value='low', variable = self.quality_selected, command = quality_rad_btn_sel)
        self.low_qual_rad_btn  = Radiobutton(self.master,text='Save High Quality Image (Slow)', value='high', variable = self.quality_selected, command = quality_rad_btn_sel)

    #remove update param after a bit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #updates contents of output_img_file_path_text_box when contents of location_text_box change
   
    
    
    def update_output_image_file_text_box(self, event = None):
#         print('update_output_image_file_text_box() called')#`````````````````````````````````````````````````````````````````````
#         print("test, self.output_image_file_name: ", self.output_image_file_name)#`````````````````````````````````````````````
#         print('self.create_new_folder_cbtn_sel.get(): ', self.create_new_folder_cbtn_sel.get())#`````````````````````````````````````
# #         print('self.folder_name_text_box:', self.folder_name_text_box.get())#`````````````````````````````````````````````````````````
        self.output_img_file_path_text_box.delete(0, "end")

        NEW_FOLDER_VALID_NEED__MAKE_A_REAL_THING_FOR_THIS = True#make a thing for this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self.create_new_folder_cbtn_sel.get() == 1:# and NEW_FOLDER_VALID_NEED__MAKE_A_REAL_THING_FOR_THIS == True:
#             print('box is checked')#```````````````````````````````````````````````````````````````````````````````````````````````
            self.output_img_file_path_text_box.insert(END, self.location_text_box.get() + '\\' + self.folder_name_text_box.get() + '\\' + self.output_image_file_name)
        else:
            self.output_img_file_path_text_box.insert(END, self.location_text_box.get() + '\\' + self.output_image_file_name)
            
   
   #change to filename not path?????????????????????????????????????????????????????????????????????????????????????
    def output_image_path______widgets_setup(self):
        self.output_image_file_name = StringVar()
        self.output_image_file_name = DEFAULT_OUTPUT_IMAGE_FILE_NAME
        
        #output image path text box
        self.output_img_file_path_lbl = Label(self.master, text="Output Image File Path: ")
        self.output_img_file_path_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)
        self.output_img_file_path_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
        
        def update_output_img_file_name(event):
            filename = GUI_utils.get_last_path_var(self.output_img_file_path_text_box.get())
            self.output_image_file_name = filename

        #updates output_image_file_name any time you edit output_img_file_path_text_box
        self.bind_to_edit(self.output_img_file_path_text_box, update_output_img_file_name)
             
        def output_file_path_clk():
            print('dict_method:', self.tabs['advanced'].tb.get())
            print('pretend to go into directory to get text file path')#`````````````````````````````````````````````````````
            
        #set initial contents of text box
        self.update_output_image_file_text_box()  
          
#         set_output_img_txt_box_contents() #need????????????????????????????????????????????????????????????????????????????????????
        self.output_img_file_path_btn = Button(self.master, text="Browse...", command = output_file_path_clk)
        
  
    def build_image______widgets_setup(self):
                #build image button   
        def build_img_btn_clk():
            #read the current state of all arguments
            image_kwargs = {'input_text_file_path':         self.input_text_file_path_text_box.get(),
                            'image_file_path':              self.input_img_file_path_text_box.get(),
                            'font_name':                    self.font_drop_down.get() + '.ttf',
                            'font_size':                    self.font_size_sbox.get(),
                            'maximize_font_size':           self.max_font_size_sel.get(),
                            'output_image_dim_ratio':       GUI_utils.strs_to_int_ratio( self.output_img_dim_num_sbox.get() , self.output_img_dim_din_sbox.get() ),
                            'image_size':                   self.img_size_sbox.get(),
                            'image_position_cords':         {'x': self.x_cord_sbox.get(), 'y': self.y_cord_sbox.get()},
                            'quality':                      self.quality_selected.get(),
                            'output_image_file_path':       self.output_img_file_path_text_box.get(),
                            
                            #from Advanced_Tab
                            'final_image_background_color': self.tabs['advanced'].output_bgnd_clr_tup_tb.get(),
                            'input_image_background_color': self.tabs['advanced'].bgnd_text_clr_tup_tb.get(),
                            'background_text_color':        self.tabs['advanced'].bgnd_text_clr_tup_tb.get()}  #does this line work???????????????????????????
            
            #build final image using arguments
            build_image.build_img_test(image_kwargs)
        self.build_img_btn = Button(self.master, text="Build Image", command = build_img_btn_clk)


        #MAYBE USE LABELFRAMES???????????????????????????????????????????????????????????????????????????????????????????????????????????
    
    def grid_widgets(self):
            blank_lbl = Label(self.master, text=" ") #for spacing 
     
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
            self.input_text_file_path_lbl        .grid(column=1, row=row_num)
            self.input_text_file_path_text_box   .grid(column=2, row=row_num, columnspan = 3)
            self.input_text_file_path_btn        .grid(column=5, row=row_num)
              
            row_num += 10 
             
            #input image file path
            self.input_img_file_path_lbl         .grid(column=1, row=row_num)
            self.input_img_file_path_text_box    .grid(column=2, row=row_num, columnspan = 3)
            self.input_img_file_path_btn         .grid(column=5, row=row_num)
              
            row_num += 10
              
            #space between
            blank_lbl                            .grid(column=1, row=row_num)
             
            row_num += 10
             
            #font section labels
            self.font_lbl                        .grid(column=1, row=row_num)
            self.font_size_lbl                   .grid(column=2, row=row_num)
             
            row_num += 10 
             
            #font inputs
            self.font_drop_down                  .grid(column=1, row=row_num) 
            self.font_size_sbox                  .grid(column=2, row=row_num)  
            self.max_font_size_cbtn              .grid(column=4, row=row_num)
             
            row_num += 10 
             
            #space between
            blank_lbl                            .grid(column=1, row=row_num)
             
            row_num += 10
             
            #image dimensions
            self.output_img_dim_lbl              .grid(column=1, row=row_num)
            self.output_img_dim_num_sbox         .grid(column=2, row=row_num)
            self.slash_lbl                       .grid(column=3, row=row_num)
            self.output_img_dim_din_sbox         .grid(column=4, row=row_num)
            self.match_input_image_dims_cbtn     .grid(column=5, row=row_num)
             
            row_num += 10
             
            #font size spinbox
            self.img_size_lbl                    .grid(column=1, row=row_num)
            self.img_size_sbox                   .grid(column=2, row=row_num)
             
            row_num += 10
             
            #image position cords
            self.img_cords_lbl                   .grid(column=1, row=row_num)
            self.prnth_open_lbl                  .grid(column=2, row=row_num)
            self.x_cord_sbox                     .grid(column=3, row=row_num)
            self.comma_lbl                       .grid(column=4, row=row_num)
            self.y_cord_sbox                     .grid(column=5, row=row_num)
            self.prnth_close_lbl                 .grid(column=6, row=row_num)
             
            row_num += 10
             
            #quality radio buttons
            self.high_qual_rad_btn               .grid(column=3, row=row_num - 1)
            self.low_qual_rad_btn                .grid(column=3, row=row_num)
             
            row_num += 10
             
            #output image file path text box
            self.output_img_file_path_lbl        .grid(column=1, row=row_num)
            self.output_img_file_path_text_box   .grid(column=2, row=row_num, columnspan = 3)
            self.output_img_file_path_btn        .grid(column=5, row=row_num)
             
            row_num += 10
             
            #build image button
            self.build_img_btn                   .grid(column=2, row=row_num)

    

        
    
#makes xview (scrolling within an entry text box) work



def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')
         
 
 
if __name__ == '__main__':
    GUI.main()    