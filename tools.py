def make_lines(num_lines, line_length, data_str):
    lines = []
    data_count = 0
    for line_num in range(num_lines):
        line = ''
        for letter_num in range(line_length):
            if data_count < len(data_str):
                letter = data_str[data_count]
            else:
                letter = ' '
            line += letter
            data_count += 1
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
                
            
#need?????????????????????????????????????????
def format_data(data):
    formatted_data = ''
    for data_line in data:
        print(data_line)#!!!!!!!!!!!
        print(data_line[0])#!!!!!!!!!!!!!!!!!!!!!!
        if data_line[0] == ' ' or formatted_data == '':
            formatted_data += data_line
        else:
            formatted_data += ' ' + data_line
    return formatted_data

def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result