import tools


def offset_color_cords(original_color_cords, img_pos, lines, background_text_color):
    print('len og color cords', len(original_color_cords))#````````````````````````````````````````````````````````````````````````
    lines_dims = get_lines_dimensions(lines)
    offset_dict = calc_offset(original_color_cords, img_pos, lines_dims)
    print('offset_dict: ', offset_dict)#    ```````````````````````````````````````````````````````````````````````````````````````````
#     new_color_cords = tools.apply_offset(original_color_cords, offset_dict)
    new_color_cords = []
    og_c_cords_len = len(original_color_cords)

    for line_num, line in enumerate(lines):
        print('line_num: ', line_num)#`````````````````````````````````````````````````````````````````````````````
        new_color_cords_line = []
        for char_num in range(len(line)):
            print('  char_num: ', char_num)#````````````````````````````````````````````````````````````````````````````
            if (line_num < offset_dict['y_offset'] or
               line_num > offset_dict['y_offset'] + og_c_cords_len - 1 or
               char_num < offset_dict['x_offset'] or
               char_num > offset_dict['x_offset'] + len(original_color_cords[line_num - offset_dict['y_offset']])):
                new_color_cords_line.append(background_text_color)
            else:
                print('len of this line in og color cords: ',len(original_color_cords[line_num - offset_dict['y_offset']] ))#```````````````````````````
                char_color = original_color_cords[line_num - offset_dict['y_offset']][char_num - offset_dict['x_offset'] - 1]
                new_color_cords_line.append(char_color)
        new_color_cords.append(new_color_cords_line)
        
    
#     left_background_text_color_list = make_color_list(background_text_color, offset_dict['x_offset'])
#     for line_cord_list in new_color_cords:
#         
#         
#     
#     
#     
#     #add lines of background_text_color to top
#     for line_num in range(offest_dict['y_offest']):
#         new_color_cords.insert(0, make_color_list(background_text_color, len( lines[0] ) ))
        

    return new_color_cords


def make_color_list(color, list_len):
    color_list = []
    for ele in range(list_len):
        color_list.append(color)
    return color_list

    
def calc_offset(color_cords, img_pos_dict, lines_dims_dict):
    img_dim_dict = get_dimentions(color_cords)
#     print('in offset, dims: ', img_dim_dict)#````````````````````````````````````````````````````````````````````````````````````
    
    
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
#     #find x and y max
#     x_max = None
#     y_max = None
#     
#     for color, cord_list in c_cords.items():
#         for cord in cord_list:
#             x = cord[1]
#             y = cord[0]
#             if x_max == None and y_max == None:
#                 x_max = x
#                 y_max = y
#             else:
#                 if x_max < x:
#                     x_max = x
#                 if y_max < y:
#                     y_max = y

    
                    
    dims = {'width': len(tools.find_longest_line(c_cords)),
            'height': len(c_cords)}
    return dims
                    
                    
                    
                    
                    
                    
                    
                    
import GUI
if __name__ == '__main__':
    GUI.main()