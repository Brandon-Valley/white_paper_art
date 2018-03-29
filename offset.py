

def offset_color_cords(original_color_cords, offset_type):
    offset_dict = calc_offset(original_color_cords, offset_type)
    new_color_cords = apply_offset(original_color_cords, offset_dict)
    return new_color_cords
    
#inclomlete, will probably need line dimentions to do this right!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
def calc_offset(color_cords, offset_type_str):
    if offset_type_str == 'centered':
        bad_default_offset_dict = {'x_offset': 10,
                                   'y_offset': 10}
        return bad_default_offset_dict
    else:
        raise Exception('ERROR  Unknown offset type: ', offset_type_str)
    
def apply_offset(og_color_cords, offset_d):
    new_c_cords = og_color_cords
    for color, new_c_cord_list in new_c_cords.items():
        for new_c_cord in new_c_cord_list:
            new_c_cord[0] += offset_d['y_offset']
            new_c_cord[1] += offset_d['x_offset']
    return new_c_cords