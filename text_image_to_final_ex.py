import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint
import tools
# make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))

WHITE = (254,254,254)
BLACK = (0,0,0)
YELLOW = (222, 224, 68)
GREY = (200, 200, 200)

num_lines = 30
line_length = 70

text_image_filename = 'yin.txt'
data_text_filename = 'ex_data.txt'


raw_lines = tools.read_text_file(text_image_filename)
# print(raw_lines)
    
data = tools.read_text_file(data_text_filename)
# print(data)
formatted_data = tools.format_data(data)

lines = tools.make_lines(num_lines, line_length, formatted_data)
highlight_cords = tools.get_highlight_cords(raw_lines)
# print(lines)
# print(highlight_cords)
    

backround_color_1 = WHITE
backround_color_2 = GREY
default_text_color = WHITE
highlight_color = YELLOW

# choose a font (you can see more detail in my library on github)
font_path = None
large_font = 20  # get better resolution with larger size
font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
try:
    font = PIL.ImageFont.truetype(font_path, size=large_font)
except IOError:
    font = PIL.ImageFont.load_default()
    print('Could not use chosen font. Using default.')


# make the background image based on the combination of font and lines
pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
# max height is adjusted down because it's too large visually for spacing
test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_height = pt2px(font.getsize(test_string)[1])
max_width = pt2px(font.getsize(max_width_line)[0])
height = max_height * len(lines)  # perfect or a little oversized
width = int(round(max_width + 40))  # a little oversized
# image = PIL.Image.new(grayscale, (width, height), color=WHITE)
# draw = PIL.ImageDraw.Draw(image)





image = Image.new("RGB", (width, height), backround_color_2) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (width, height), backround_color_1) # final image


fill = " o "
x = 0
w_fill, y = draw.textsize(fill)

line_num = 0
for line_num in range(len(lines)):
    line = lines[line_num]
    print(line)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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



