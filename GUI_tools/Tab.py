from tkinter import END
from tkinter import filedialog


import GUI #only need for testing

import sys
import os
sys.path.insert(1, os.path.dirname(__file__)) # so you can import relative to this file even when it is called from elsewhere

from widget_groups import File_System_Browse_WG
from widget_groups import Font_Config_WG





DIGITS = '0123456789.-'


class Tab():
    def __init__(self, master):
        self.master = master
        self.tabs = None
        
        self.digits_only = (self.master.register(self.validate), DIGITS, '%P')
         
    def validate(self, allowed_chars, value_if_allowed):
        #need this to make delete work
        if (value_if_allowed == ''):
            return True
    
        for char in value_if_allowed:
            if char not in allowed_chars:
                return False
        return True
    
    #bind keys to widget such that func gets called any time the contents of the widget change
    def bind_to_edit(self, widget, func):
        widget.bind("<KeyRelease>", func)
        widget.bind("<KeyRelease-BackSpace>", func)
        widget.bind("<KeyRelease-Delete>", func)
        widget.bind("<KeyRelease-space>", func)
        
    def bind_to_click(self, widget, func):
        widget.bind("<ButtonRelease>", func)
        widget.bind("<Enter>", func)
        
    # returns length of longest str in a list,
    # useful for making combo boxes match length of contents
    # if useing for a combo box, will need to add + 1 so V part
    # of box doesnt cover end of longest str
    def max_str_len_in_l(self, str_list):
        len_max = 0
        for m in str_list:
            if len(m) > len_max:
                len_max = len(m)
        return len_max + 1

    # fills list box widget from list of strings in order
    def fill_list_box(self, list_box_widget, str_list):
        if str_list != None:
            for str in str_list:
                list_box_widget.insert(END, str)

# DONT DELETE UNTIL YOU KNOW IT WONT BE NEEDED EVER AGAIN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     def path_tb_browse_btn_clk(self, path_txt_box_widget, browse_for, file_type = None):
#         #get file path and place it in text box
#         
#         if browse_for == 'file':
#             if file_type == None:
#                 file_system_item = filedialog.askopenfilename()
# 
#             else:
#                 file_system_item = filedialog.askopenfilename(filetypes = (("Images", "*" + file_type), ("All files", "*")))#filetypes = (("Images", '*.png|*.jpg'), ("All files", "*")))#"*" + file_types   #,("Template files", '*.jpg'), 
#         elif browse_for == 'dir':
#             file_system_item = filedialog.askdirectory()
#         else:
#             raise Exception('ERROR:  In Tab.py, in path_tb_browse_btn_clk, invalid value for browse_for: ', browse_for)
#         path_txt_box_widget.delete(0, "end")
#         path_txt_box_widget.insert(END, file_system_item)
#         
# #         output_path_text_box_updated()
        
        
    def File_System_Browse_WG(   self,
                                 master,
                                 lbl_txt, 
                                 tb_width              = None, 
                                 browse_for            = 'dir',  # 'dir' or 'file'
                                 file_type             = None,   # '.jpg', '.mp4', ect...
                                 init_path             = None, 
                                 focus_tb_after_browse = False,
                                 tb_edit_func          = None,
                                 browse_btn_txt        = 'Browse...'):
        
        return File_System_Browse_WG.File_System_Browse_WG(master, lbl_txt, tb_width, browse_for, file_type, init_path, focus_tb_after_browse, tb_edit_func, browse_btn_txt)
        
        
        
    def Font_Config_WG(  self,
                         master,
                         fonts_dir_path         = None, 
                         default_font_size      = 20,
                         default_font           = None,
                         font_size_sbox_command = None,
                         font_size_sbox_width   = 5,
                         max_font_size          = 9999,
                         min_font_size          = 0,
                         font_size_sbox_lbl_txt = 'Font Size:',
                         font_cbox_lbl_txt      = 'Font:'):

        return Font_Config_WG.Font_Config_WG(
                         master,
                         fonts_dir_path, 
                         default_font_size,
                         default_font,
                         font_size_sbox_command,
                         font_size_sbox_width,
                         max_font_size,
                         min_font_size,
                         font_size_sbox_lbl_txt,
                         font_cbox_lbl_txt,
                         self.digits_only,
                         self.max_str_len_in_l)

         
        
        
        
        
        
        
if __name__ == '__main__':
    GUI.main()



# import GUI #only need for testing
# 
# 
# DIGITS = '0123456789.-'
# 
# 
# class Tab():
#     def __init__(self, master):
#         self.master = master
#         self.tabs = None
#         
#         self.digits_only = (self.master.register(self.validate), DIGITS, '%P')
#          
#     def validate(self, allowed_chars, value_if_allowed):
#         #need this to make delete work
#         if (value_if_allowed == ''):
#             return True
#     
#         for char in value_if_allowed:
#             if char not in allowed_chars:
#                 return False
#         return True
#     
#     #bind keys to widget such that func gets called any time the contents of the widget change
#     def bind_to_edit(self, widget, func):
#         widget.bind("<KeyRelease>", func)
#         widget.bind("<KeyRelease-BackSpace>", func)
#         widget.bind("<KeyRelease-Delete>", func)
#         widget.bind("<KeyRelease-space>", func)
#         
#     def bind_to_click(self, widget, func):
#         widget.bind("<ButtonRelease>", func)
#         widget.bind("<Enter>", func)
# 
#     
# 
#         
#         
#         
#         
#         
#         
#         
#         
#         
#         
#         
# if __name__ == '__main__':
#     GUI.main()