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

colors = {'backround_1':  WHITE,
          'backround_2':  ALMOST_BLACK,
          'default_text': WHITE,
          'highlight':    YELLOW}

#2/3:
# a a a
# a a a
dimention_ratio = 5/4

text_image_filename = 'yin.txt'
data_text_filename = 'ex_data.txt'

#read in image and data in txt files into lists of lines
raw_lines = tools.read_text_file(text_image_filename)    
data = tools.read_text_file(data_text_filename)

#turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
data_str = tools.format_data(data)
num_chars = len(data_str)
word_list = data_str.split(' ')

#turn dimention_ratio into max number of lines and max chars per line
ideal_dimentions = tools.calc_ideal_dimentions(dimention_ratio, num_chars)

#make list of lines to be output in final image
lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)
print(lines)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#look at text image lines to get cords of chars to be highlighted in final image
highlight_cords = tools.get_highlight_cords(raw_lines)

#put it all together and what have you got?  Bippity Boppity BOO!
image = text_image.text_image(lines, colors, highlight_cords)

# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
image.save('test_output.png', subsampling=0, quality = 100)
image.show()




