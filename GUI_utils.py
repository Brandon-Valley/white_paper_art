



def get_current_dir_path():
    return 'defaut\home?dir\hfolder_name'

def get_defalt_text_file_path():
    return 'default\text\file\path'
 
def get_defalt_image_file_path():
    return 'default\image\file\path'


def get_font_list():
    return['font1', 'font2', 'cour', "font22222222222222222222222222222222222222222222222222222222"]
    


def bool_to_state(bool_int, active_low = True):

    if active_low == True:
        if   bool_int == 1:
            return 'disabled'
        elif bool_int == 0:
            return 'normal'
        
    elif active_low == False:
        if   bool_int == 0:
            return 'disabled'
        elif bool_int == 1:
            return 'normal'
        
    raise Exception('ERROR    bool_str_to_state in GUI_utils received an invalid argument: ', bool_int)


def get_input_img_dims(img_path):
    img_dimensions = {'num': 22,
                      'din': 333}
    return img_dimensions


def strs_to_int_ratio(str1, str2):
    i1 = int(str1)
    i2 = int(str2)
    return i1 / i2
    
    
def get_defalt_output_img_file_path():
    return "output\img\defalt\fuiles\path"
    
    
    
    
    
    
    
    
    
    
    
    
