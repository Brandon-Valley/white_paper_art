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
    try_num = 0
    ideal_ratio = ideal_num_lines / ideal_line_length 
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
    print('winning line len:', new_line_length -1)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
    

def get_highlight_cords(lines):
    h_cords = []
    for line_num in range(len(lines)):
        line = lines[line_num]
        for letter_num in range(len(line)):
            letter = line[letter_num]
            if letter != ' ':
                h_cords.append( [line_num, letter_num])
    return h_cords
    
            
#makes broken up list of strings into one big string
def format_data(data):
    formatted_data = ''
    for data_line in data:
        if data_line[0] == ' ' or formatted_data == '':
            formatted_data += data_line
        else:
            formatted_data += ' ' + data_line
    return formatted_data

def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result