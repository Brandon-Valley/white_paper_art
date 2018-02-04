from PIL import Image, ImageDraw
from random import randint
make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))

WHITE = (254,254,254)
BLACK = (0,0,0)
YELLOW = (222, 224, 68)

num_lines = 20
line_length = 200



text_image_filename = 'yin.txt'
data_text_filename = 'ex_data.txt'


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
            if letter == ' ':
                h_cords.append( [line_num, letter_num])
    return h_cords
                
            
#need?????????????????????????????????????????
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

raw_lines = read_text_file(text_image_filename)
print(raw_lines)
    
data = read_text_file(data_text_filename)
print(data)
formatted_data = format_data(data)

lines = make_lines(num_lines, line_length, formatted_data)
highlight_cords = get_highlight_cords(raw_lines)
print(lines)
print(highlight_cords)
    
# lines = translate(raw_lines, data)

# highlight_cords = [    [0,3],
#                        [0,4],
#                        [0,7],
#                        [1,3],
#                        [1,9] ]
# 
# 
# lines = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
#          'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
#          'cccccccccccccccccccccccccccccccccccccc']

backround_color = BLACK
default_text_color = WHITE
highlight_color = YELLOW


image = Image.new("RGB", (1200,400), backround_color) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (1200, 200), (0,0,0)) # final image


fill = " o "
x = 0
w_fill, y = draw.textsize(fill)



line_num = 0
for line_num in range(len(lines)):
    line = lines[line_num]
    x_draw, x_paste = 0, 0
    
    for letter_num in range(len(line)):
        letter = line[letter_num]
        w_full = draw.textsize(fill + letter)[0]
        w = w_full - w_fill     # the width of the character on its own
        
        letter_cords = [line_num, letter_num]
        if letter_cords in highlight_cords:
            color = highlight_color
        else:
            color = default_text_color
        draw.text((x_draw, y * line_num), fill + letter, color)
    
        iletter = image.crop((x_draw + w_fill, 0, x_draw + w_full, y * len(lines)))
        image2.paste(iletter, (x_paste, 0))
        x_draw += w_full
        x_paste += w
    line_num += 1
image2.show()



def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result