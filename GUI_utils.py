

def get_defalt_text_file_path():
    return 'default/text/file/path'
 
def get_defalt_image_file_path():
    return 'default/image/file/path'


def get_font_list():
    return['font1', 'font2', 'cour', "font22222222222222222222222222222222222222222222222222222222"]
    
    
def get_font_size_dimensions():
    f_size_dims = {'min': 0,
                   'max': 100}
    return f_size_dims


def bool_to_state(bool_int):
    if   bool_int == 1:
        return 'disabled'
    elif bool_int == 0:
        return 'normal'
    else:
        raise Exception('ERROR    bool_str_to_state in GUI_utils received an invalid argument: ', bool_int)


def get_input_img_dims(img_path):
    img_dimensions = {'num': 22,
                      'din': 333}
    return img_dimensions


def strs_to_int_ratio(str1, str2):
    i1 = int(str1)
    i2 = int(str2)
    return i1 / i2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
