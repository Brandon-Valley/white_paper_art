
import tools

uniform_char = '@'
input_filename = 'out.txt'
output_filename = 'uniform_' + input_filename

og_image_dict = tools.read_text_file(input_filename )

line_dict = []
for og_line in og_image_dict:
    line = ''
    for og_char in og_line:
        if og_char == ' ' or og_char == uniform_char:
            line += og_char
        else:
            line += uniform_char
    line_dict.append(line)
        
tools.write_text_file(output_filename, line_dict)