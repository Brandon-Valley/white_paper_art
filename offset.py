import tools

def offset_color_cords(original_color_cords, img_pos, lines):
    lines_dims = get_lines_dimensions(lines)
    offset_dict = calc_offset(original_color_cords, img_pos, lines_dims)
    new_color_cords = tools.apply_offset(original_color_cords, offset_dict)
    return new_color_cords
    
def calc_offset(color_cords, img_pos_dict, lines_dims_dict):
    img_dim_dict = get_dimentions(color_cords)
    
    x_0 = ( lines_dims_dict['lenght_of_longest_line'] - img_dim_dict['width'] ) / 2
    y_0 = ( lines_dims_dict['num_lines'] - img_dim_dict['height'] ) /2
    
    img_offset_dict = {'x_offset': int( x_0 ) + img_pos_dict['x_pos'],
                       'y_offset': int( y_0 ) + img_pos_dict['y_pos']}

    return img_offset_dict
    
    
#returns a dict with the number of lines and the length of the longest line
def get_lines_dimensions(lines):
    max_len = 0
    
    for line in lines:
        if max_len < len(line):
            max_len = len(line)
    
    l_dims = {'num_lines': len(lines),
              'lenght_of_longest_line': max_len}
    return l_dims

    
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
                    
                    
                    
                    
                    
                    
                    
                    

