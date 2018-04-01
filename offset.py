

def offset_color_cords(original_color_cords, img_pos):
    offset_dict = calc_offset(original_color_cords, img_pos)
    new_color_cords = tools.apply_offset(original_color_cords, offset_dict)
    return new_color_cords
    
#inclomlete, will probably need line dimentions to do this right!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
def calc_offset(color_cords, img_pos_dict):
    dim_dict = get_dimentions(color_cords)
    
    print('in offsed, dims: ', dim_dict)#``````````````````````````````````````````````````````````
    if offset_type_str == 'centered':
        bad_default_offset_dict = {'x_offset': 10,
                                   'y_offset': 10}
        return bad_default_offset_dict
    else:
        raise Exception('ERROR  Unknown offset type: ', offset_type_str)
    
#get height and width, mins are 0 because of trim in color_cords so only need to find max
def get_dimentions(c_cords):
    #find x and y max
    x_max = None
    y_max = None
    
    for color, cord_list in c_cords.items():
        for cord in cord_list:
            x = cord[1]
            y = cord[0]
            if x_max == None and y_max == None:
                x_max = x
                y_max = y
            else:
                if x_max < x:
                    x_max = x
                if y_max < y:
                    y_max = y
                    
    dims = {'width': x_max,
            'height': y_max}
    return dims
                    
                    
                    
                    
                    
                    
                    
                    

