
import tools

uniform_char = '@'
input_filename = 'out.txt'
output_filename = 'uniform_' + input_filename

og_image_tup = tools.read_text_file(input_filename )
print(og_image_tup)

line_list = []
for og_line in og_image_tup:
    line = ''
    for og_char in og_line:
        if og_char == ' ' or og_char == uniform_char:
            line += og_char
        else:
            line += uniform_char
    line_list.append(line)
        
print(line_list)
tools.write_text_file(output_filename, line_list)