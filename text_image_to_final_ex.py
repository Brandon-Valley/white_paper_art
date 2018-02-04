import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint
import tools
import text_image

WHITE = (254,254,254)
BLACK = (0,0,0)
ALMOST_BLACK = (5,5,5)
YELLOW = (222, 224, 68)
GREY = (200, 200, 200)

#2/3:
# a a a
# a a a
dimention_ratio = 3/4

text_image_filename = 'yin.txt'
data_text_filename = 'ex_data.txt'

#read in image and data in txt files into lists of lines
raw_lines = tools.read_text_file(text_image_filename)    
data = tools.read_text_file(data_text_filename)

#turn list of lines of data into one big string
formatted_data = tools.format_data(data)

#turn dimention_ratio into max number of lines and max chars per line
max_dimentions = tools.calc_max_dimentions(dimention_ratio, len(formatted_data))

#make list of lines to be output in final image
lines = tools.make_lines(max_dimentions['num_lines'], max_dimentions['line_length'], formatted_data)

#look at text image lines to get cords of chars to be highlighted in final image
highlight_cords = tools.get_highlight_cords(raw_lines)

    
colors = {'backround_1':  WHITE,
          'backround_2':  ALMOST_BLACK,
          'default_text': WHITE,
          'highlight':    YELLOW}

image = text_image.text_image(lines, colors, highlight_cords)
image.save('test_output.png', quality = 100)
image.show()




