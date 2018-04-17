import re

OUTPUT_IMAGE_SUFFIX = '_text_art'

def get_current_dir_path():
    
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path#'sdfsfdfsfsd\sdffsdfsf'#"'C:\Users\Brandon\Documents\Personal Projects\white_paper_art\examples'"

def get_defalt_text_file_path():
    return 'default\text\file\path.txt'
 
def get_defalt_image_file_path():
    return 'ddddd\aaaaa\file\bitcoin.jpg'


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
    
    
    
def get_last_path_var(f_path):
    split_f_path = re.split(r'[\\/]', f_path)
    return split_f_path[-1]

    
def get_defalt_output_img_file_path(img_file_path):
    out_img_path = ''
    
    splt_path = re.split(r'[\\/]', img_file_path)
    
    filename = splt_path.pop()
    splt_filename = filename.split('.')
    splt_filename.insert(1, OUTPUT_IMAGE_SUFFIX)
    
    for e in splt_path:
        out_img_path += e
        
    for e in splt_filename:
        out_img_path += e
        
    return out_img_path
#     
#     
#     
#     folder_name_text_box.insert(END, cf_path[-1])
#     
#     
#     return "output\img\defalt\fuiles\path"
    
    
    
    
    
    
    
    
    
    
    
    
