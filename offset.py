import tools


def offset_color_cords(original_color_cords, img_pos, lines, background_text_color):
    lines_dims = get_lines_dimensions(lines)
    offset_dict = calc_offset(original_color_cords, img_pos, lines_dims)
#     new_color_cords = tools.apply_offset(original_color_cords, offset_dict)
    new_color_cords = []
    og_c_cords_len = len(original_color_cords)

    for line_num, line in enumerate(lines):
        new_color_cords_line = []
        for char_num in range(len(line)):
            if (line_num < offset_dict['y_offset'] or
               line_num > offset_dict['y_offset'] + og_c_cords_len - 1 or
               char_num < offset_dict['x_offset'] or
               char_num > offset_dict['x_offset'] + len(original_color_cords[line_num - offset_dict['y_offset']])):
                new_color_cords_line.append(background_text_color)
            else:
                char_color = original_color_cords[line_num - offset_dict['y_offset']][char_num - offset_dict['x_offset'] - 1]
                new_color_cords_line.append(char_color)
        new_color_cords.append(new_color_cords_line)

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
    dims = {'width': len(tools.find_longest_line(c_cords)),
            'height': len(c_cords)}
    return dims
                    
                    
                    
                    
                    
                    
                    
                    
import GUI
if __name__ == '__main__':
    GUI.main()