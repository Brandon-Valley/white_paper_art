import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint
import tools
import text_image


WHITE = (254,254,254)
BLACK = (0,0,0)
ALMOST_BLACK = (5,5,5)
YELLOW = (222, 224, 68)
DARK_GRAY = (68,68,68)
GREY = (200, 200, 200)

colors = {'backround_1':  WHITE,
          'backround_2':  ALMOST_BLACK,
          'default_text': WHITE,
          'highlight':    DARK_GRAY}

const_HxW_ratio = 5150/9600 #found by making a 99x99 txt file and looking at dimensions of image
image_resize_ratio = .75

#2/3:
# a a a
# a a a
desired_dimension_ratio = 1/1#why dosnt 1/1 make square??????????????????????????????????????????????????
#ratios seem messed up, fix/why????????????????????????????????????????????????????????????????

text_image_filename = 'out.txt'      #picture of bitcoin icon
data_text_filename = 'full_paper.txt'#satoshi whitepaper in a txt file

#read in image and data in txt files into lists of lines
print('Reading in image text file...') 
raw_lines = tools.read_text_file(text_image_filename)   
print('Reading in data text file...') 
data = tools.read_text_file(data_text_filename)

#turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
data_str = tools.format_data(data)
num_chars = len(data_str)
word_list = data_str.split(' ')

#find correct image dimensions by adjusting desired ratio for the difference between the length of a char and the height of a line
true_dimension_ratio = desired_dimension_ratio * const_HxW_ratio

#turn true_dimension_ratio into max number of lines and max chars per line
ideal_dimentions = tools.calc_ideal_dimentions(true_dimension_ratio, num_chars)

#make list of lines to be output in final image
lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)
print("number of lines:", len(lines))

#look at text image lines to get cords of chars to be highlighted in final image
highlight_cords = tools.get_highlight_cords(raw_lines)

#adjust the highlight cords to compensate for the difference between the width of a char and the height of a line
adjusted_highlight_cords = tools.adjust_highlight_cords(highlight_cords, image_resize_ratio)

#put it all together and what have you got?  Bippity Boppity BOO!
print('Creating Image...')
image = text_image.text_image(lines, colors, adjusted_highlight_cords)

# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
image.save('test_output.png', subsampling=0, quality = 100)

image.show()




