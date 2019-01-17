import math
from _regex_core import WORD


#from twisted.conch.scripts.conch import old

#return the length of the longest element in lines
def find_longest_line(lines):
    longest_line = ''
    for line in lines:
        cur_len = len(line)
        if cur_len > len(longest_line):
            longest_line = line
    return longest_line

#this func dosnt compensate for the chars that will be moved down to the next line when a full word is moved
#and the extra bottom lines this will result in, throwing off the ratio
#this problem will get worse as the length of text increases, might need to fix eventually
def calc_ideal_dimentions(dim_ratio, num_chars):
    num_lines = int( round( (math.sqrt( num_chars * dim_ratio) ) ) )
    inverse_dim_ratio = 1 / dim_ratio
    line_length = int( round( num_lines * inverse_dim_ratio ) ) 
    dims = {'num_lines'  : num_lines,
            'line_length': line_length}
    return dims

#returns true or false whether num1 is closer to ideal_num than 
#num2, true if num1 and num2 equal distance from ideal_num
def closer(num1, num2, ideal_num):
    diff1 = abs( ideal_num - num1 )
    diff2 = abs( ideal_num - num2 )
    if diff1 < diff2:
        return True
    else:#if <=
        return False

#because of the problems with calc_ideal_dimentions, this function will continue making sets of lines
#increasing the width each time until the closest situation to the 
def make_correct_lines(ideal_num_lines, ideal_line_length, word_list):
    try:
        ideal_ratio = ideal_num_lines / ideal_line_length 
    except:#if get 0x0
        ideal_ratio = 1
        
    try_num = 0
    prev_ratio = 0
    new_ratio = 0
    prev_lines = []
    new_lines = []
    while(try_num <= 1 or closer(new_ratio, prev_ratio, ideal_ratio)):
        prev_ratio = new_ratio
        prev_lines = new_lines
        
        new_line_length = ideal_line_length + try_num
        new_lines = make_lines(new_line_length, word_list)
        new_ratio = len(new_lines) / new_line_length

        try_num +=1
    return prev_lines

def make_lines(line_length, word_list):
    lines = []
    word_count = 0
    while(word_count < len(word_list)):
        line = ''
        end_line = False
        while(end_line == False):
            if word_count < len(word_list):
                word = word_list[word_count]
                if len(line + ' ' + word) < line_length:
                   line += ' ' + word 
                   word_count += 1
                else:
                    end_line = True
            else:
                end_line = True
        lines.append(line)        
    return lines               



#makes broken up list of strings into one big string
def format_data(data):
    formatted_data = ''
    
    for data_line in data:
        if len(data_line) > 0:
            if data_line[0] == ' ' or formatted_data == '':
                formatted_data += data_line
            else:
                formatted_data += ' ' + data_line
    return formatted_data
    
#     try:
#         for data_line in data:
#             if data_line[0] == ' ' or formatted_data == '':
#                 formatted_data += data_line
#             else:
#                 formatted_data += ' ' + data_line
#         return formatted_data
#     except:
#         raise Exception('ERROR  You probably have some extra lines of spaces in your data text file')


# def apply_offset(og_color_cords, offset_d, background_text_color):
#     new_c_cords = og_color_cords
#     for color, new_c_cord_list in new_c_cords.items():
#         for new_c_cord in new_c_cord_list:
#             new_c_cord[0] += offset_d['y_offset']
#             new_c_cord[1] += offset_d['x_offset']
#     return new_c_cords


def calc_img_dims(lines, font):
    img_dims = {}
    
    longest_line = find_longest_line(lines)
    max_line_width = (font.getsize(longest_line)[0])

    # max height is adjusted down because it's too large visually for spacing
    test_string = 'a' #if I use this string instead, it adds like 10 blank lines to end of pic, no clue why:  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = (font.getsize(test_string)[1])
        
    height = ( max_height * len(lines) ) + 5  # perfect or a little over sized
    
    width  = int(round(max_line_width + 1 + 0))  # a little over sized , needs to be exactly this # or cuts off text
    
    return (width, height)


def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False


def char_2_unicode(char):
    return hex(ord(char))


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
#just for testing
def write_text_file(file_path, line_list):
    f = open(file_path, 'w', encoding='utf-8')
    # write to file
    for line in line_list:
        f.write(line + '\n')
    # cleanup
    f.close()
    




    
    
    
    
    
import GUI
if __name__ == '__main__':
    GUI.main()    