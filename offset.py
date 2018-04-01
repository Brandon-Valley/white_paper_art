

def offset_color_cords(original_color_cords, img_pos):
    offset_dict = calc_offset(original_color_cords, img_pos)
    new_color_cords = tools.apply_offset(original_color_cords, offset_dict)
    return new_color_cords
    
#inclomlete, will probably need line dimentions to do this right!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
def calc_offset(color_cords, img_pos_dict):
    dim_dict = get_dimentions(color_cords)
    if offset_type_str == 'centered':
        bad_default_offset_dict = {'x_offset': 10,
                                   'y_offset': 10}
        return bad_default_offset_dict
    else:
        raise Exception('ERROR  Unknown offset type: ', offset_type_str)
    

def get_dimentions(c_cords):
    print('in offset, c_cords: ', c_cords)#`````````````````````````````````````````````````````````````````````````
    print('in offset, fancy print c_cords: VVVVV')
    for color, cord_list in c_cords.items():
        print("%s : %s" %(cord_list, color))
