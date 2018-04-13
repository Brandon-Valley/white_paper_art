

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


def get_font_size_state(bool_str):
    if   bool_str == 'True':
        return 'disabled'
    elif bool_str == 'False':
        return 'normal'
    else:
        raise('ERROR    get_font_size_state in GUI_utils received an invalid argument: ', bool_str)


