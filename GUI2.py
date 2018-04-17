from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk

import re

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

def show_gui():
    
    window = Tk()
    window.title("Text Image Maker")
    window.geometry('900x400') #1500x700 takes up aplmost the whole screen
     
    

    
    
    
    window.mainloop()
    print('after mainloop, should only het here after closing gui')
    
    
def set_output_img_txt_box_contents(text_box, file_path):
#     output_img_file_path_text_box.insert(END, GUI_utils.get_defalt_output_img_file_path(input_img_file_path_text_box.get())) #default
    text_box.insert(END, GUI_utils.get_defalt_output_img_file_path(file_path)) #default
    
#makes xview (scrolling within an entry text box) work
def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')
    
    

    
# if __name__ == "__main__":
#     print('GUI MAIN')
#     show_gui()
    
    
    
    
    
    

 
class Main_Window():
    
#     def onValidate(self, P):
#         return True
#         self.folder_name_text_box.delete("1.0", "end")
#     #             self.text.insert("end","OnValidate:\n")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         print("trying to get full: " , self.entry.get())
#     #             print('P: ', P)
#     #             
#         self.location_text_box.insert("end", P)
#     
#         self.text.insert("end", self.location_text_box.get() + P)
#     
#         return True
    
    def location_set_up(self):
        def callback():#`````````````````````````````````````````````````````
            print('skidhniush')
            return True
        #Location path text box 
        self.l_path = StringVar()
        self.location_lbl = Label(self.master, text="Location: ")
        
        
        
#         self.e = Entry(master, textvariable=self.sv, validate="key", validatecommand=self.call_back)
#         self.e.insert(END, "solifoi")

        #to make sure the copied text box isn't always one character behind, there is probably a less stupid way to do this
#         vcmd = (self.register(self.onValidate), '%P')    
        
#         def onValidate(self, P):
#             self.folder_name_text_box.delete("1.0", "end")
# #             self.text.insert("end","OnValidate:\n")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             print("trying to get full: " , self.entry.get())
# #             print('P: ', P)
# #             
#             self.location_text_box.insert("end", P)
#     
#             self.text.insert("end", self.location_text_box.get() + P)
#     
#             return True

        #modify folder name text box
#         def key_press_loc(event):
#             if self.create_new_folder_sel.get() == 0:#if new folder disabled
#                 self.folder_name_text_box.configure( state = 'normal' )
#                 self.folder_name_text_box.insert(END, event.char)
#                 self.folder_name_text_box.configure( state = 'disabled' )
#         
#         def backspace_press_loc(event):
#             if self.create_new_folder_sel.get() == 0:#if new folder disabled
#                 self.folder_name_text_box.configure( state = 'normal' )
#                 temp_txt = self.folder_name_text_box.get()[:-1]#maybe change this to something that gets the last file name from location?????????????????????????
#                 self.folder_name_text_box.delete(0, "end")#clear text box
#                 self.folder_name_text_box.insert(END, temp_txt)  
#                 self.folder_name_text_box.configure( state = 'disabled' )


#         def update_new_folder_text_box():
#             if self.create_new_folder_sel.get() == 0:#if new folder disabled
#                 self.folder_name_text_box.configure( state = 'normal' )
#                 self.folder_name_text_box.delete(0, "end")#clear text box
#                 self.folder_name_text_box.insert(END, self.folder_name_text_box.get())
#                 self.folder_name_text_box.configure( state = 'disabled' )


        
        
        self.location_text_box = Entry(self.master,width=FILE_PATH_TEXT_BOX_WIDTH)#, textvariable=self.l_path, validate="key", validatecommand=vcmd)#self.double_click_folder_name_cbtn)#update_folder_name_text_box)
        self.location_text_box.insert(END, GUI_utils.get_current_dir_path()) #default #put back!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         self.location_text_box.set('3333333333333333')
        self.location_text_box.bind('<Expose>', xview_event_handler)#scrolls text to end if needed
        self.location_text_box.bind("<Key>", self.update_folder_name_text_box)
        self.location_text_box.bind("<BackSpace>", self.update_folder_name_text_box)
#         self.location_text_box.bind("<Key>", update_new_folder_text_box)
#         self.location_text_box.bind("<BackSpace>", update_new_folder_text_box)
#         self.location_text_box.bind("<Key>", key_press_loc)
#         self.location_text_box.bind("<BackSpace>", backspace_press_loc)
             
        def location_browse_btn_clk():
            #get file path and place it in text box
            dir = filedialog.askdirectory()
            self.location_text_box.delete(0, "end")#clear text box
            self.location_text_box.insert(END, dir)
            
            #make sure new folder text box updates correctly
            folder_name_text_box.configure( state = 'normal' )
            update_folder_name_text_box()
            
        self.location_browse_btn = Button(self.master, text="Browse...", command = location_browse_btn_clk)
        
#     def double_click_folder_name_cbtn(self):
#         try:
#             print('trying to print full: %P')
#             self.create_new_folder_sel.set(1)
#             self.update_folder_name_text_box()
#             self.create_new_folder_sel.set(0)
#             self.update_folder_name_text_box()
#         except:
#             print("HIT EXCEPTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")#`````````````````````````````````````````````
#             pass
#         return True
        
    
    #create new folder check button
    def update_folder_name_text_box(self, event = None):#changes state and contents of folder name
#         print('in update_folder_name)texrwsgfndkjfgnkjn')#``````````````````````````````````````````````````````````````````````````````````
#         return True
        #not using bool_to_state because depending on what state, configure needs to be called at different times
        try: #wont work the first time because folder_name_text_box hasn't been declared yet
            if self.create_new_folder_sel.get() == 0:
                self.folder_name_text_box.configure( state = 'normal' )#`````````````````````````````````````````````````
                self.folder_name_text_box.delete(0, "end")#``````````````````````````````````````````````````
                print(self.location_text_box.get())
                print('0')#````````````````````````````````````````````````````````````````````````````````````````````````````````````
                self.folder_name_text_box.delete(0, "end")
                print('after')
                cf_path = re.split(r'[\\/]', self.location_text_box.get())
                self.folder_name_text_box.insert(END, cf_path[-1])
                self.folder_name_text_box.configure( state = 'disabled' )
            else:
                print(1)
                self.folder_name_text_box.configure( state = 'normal' )
                self.folder_name_text_box.delete(0, "end")
            print('about to return ture!!!!!!!!!!!!!!!!!!!!!')#```````````````````````````````````````````````````
        except:
            pass
        return True #so that this can be called by validatecommand in location
    
    
    def __init__(self, master):
#         tk.Frame.__init__(self, master)
        self.master = master



        self.folder_name_text_box = Entry(self.master,width=20)
        self.location_set_up()
        
        
        
        #folder name text box 
        folder_name_lbl = Label(self.master, text="Folder Name: ")
        self.folder_name_text_box = Entry(self.master,width=20)
        
        
        

        
        self.create_new_folder_sel = IntVar(value = 1)#value sets default
        create_new_folder_cbtn = Checkbutton(text="Create New Folder", variable=self.create_new_folder_sel, command = self.update_folder_name_text_box)
        self.update_folder_name_text_box() #disabled folder name by default if create_new_folder_cbtn is 0 by default
        
         
         
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
        create_new_folder_cbtn          .grid(column=1, row=row_num)
        
        row_num += 10
        
        #folder_name
        folder_name_lbl                 .grid(column=1, row=row_num)
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
         

         
 
def main(): 
    root = Tk()
    root.title("Text Image Maker")
    root.geometry('900x400') #1500x700 takes up aplmost the whole screen
    Main_Window(root)#.pack(fill="both", expand=True)
    
#     app = Main_Window(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    