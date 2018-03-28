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
    
#to speed things up maybe do something to not need to record whitespace
def get_color_cords(color_matrix):
    c_cords = {}
    for line_num in range(len(color_matrix)):
        line = color_matrix[line_num]
        for color_num in range(len(line)):
            color = line[color_num]
            #to add something for whitespace put something like if not whitespace here!!!!!!!
            
            #check if this color is already a key in highlight_cords
            color_known = False
            for known_color, cord_list in c_cords.items():
                if color == known_color:
                    color_known = True
                    break
            #add color to keys in c_cords if new
            if color_known == False:
                c_cords[color] = []
            #add cord
            c_cords[color].append( [line_num, color_num] )
    return c_cords
    
    
def adjust_highlight_cords(h_cords, image_resize_ratio):
    adjusted_h_cords = {}
    #add h_chars from original h_cords 
    for h_char, cords in h_cords.items():
        adjusted_h_cords[h_char] = []
    
    for h_char, h_cords in h_cords.items():
        for h_cord in h_cords:
            
            line_float = h_cord[0] * (1 / image_resize_ratio)
            letter_float = h_cord[1] * image_resize_ratio
               
            line_num = int (line_float)
            letter_num = int (letter_float)
            
            #if pos taken, must find another
    #         if [line_num, letter_num] in h_cords:
    #             if line_float % 1 < 0.5:
    #                 line_num = int( (h_cord[0] - 0.5) * (1 / image_resize_ratio) ) 
    #             else:
    #                 line_num = int( (h_cord[0] + 0.5) * (1 / image_resize_ratio) ) 
    
            adjusted_h_cords[h_char].append( [line_num, letter_num])

            #compensate for skipping lines
            if line_float % 1 == 0.75:
                extra_line_num = round (line_float)
                adjusted_h_cords[h_char].append( [extra_line_num, letter_num])
        
#     print('lost %s h_chars' %(len(h_cords) - len(list(set(adjusted_h_cords)))))#`````````````````````````````````````````````````````````
    return adjusted_h_cords


#makes broken up list of strings into one big string
def format_data(data):
    formatted_data = ''
    
    try:
        for data_line in data:
            if data_line[0] == ' ' or formatted_data == '':
                formatted_data += data_line
            else:
                formatted_data += ' ' + data_line
        return formatted_data
    except:
        raise Exception('ERROR  You probably have some extra lines of spaces in your data text file')

def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
#just for testing
def write_text_file(file_path, line_list):
    f = open(file_path, 'w')
    # write to file
    for line in line_list:
        f.write(line + '\n')
    # cleanup
    f.close()
    
    
    
    