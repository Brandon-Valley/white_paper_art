import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint

import tools
import text_image
import ascii_art
import ascii_image_editor


input_image_filename = 'bitcoin.png'
data_text_filename = 'full_paper.txt'#satoshi whitepaper in a txt file

original_ascii_art_filename = 'ascii_' + input_image_filename.split('.')[0] + '.txt'
edited_ascii_art_filename = 'EDITED_' + original_ascii_art_filename
# text_image_filename = 'EDITED_data_dash.txt'      #picture of bitcoin icon

final_image_filename = 'test_output.png'

# set scale default as 0.43 which suits
# a Courier font
scale = 0.43

# set cols
cols = 200

const_HxW_ratio = 5150/9600 #found by making a 99x99 txt file and looking at dimensions of image
image_resize_ratio = .8

#2/3:
# a a a
# a a a
desired_dimension_ratio = 1/1

#find correct image dimensions by adjusting desired ratio for the difference between the length of a char and the height of a line
true_dimension_ratio = desired_dimension_ratio * const_HxW_ratio

# WHITE = (255,255,255#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# BLACK = (0,0,0)
# ALMOST_BLACK = (5,5,5)
# YELLOW = PIL.ImageColor.getrgb('yellow')
# ORANGE = PIL.ImageColor.getrgb('orange')
# DARK_GRAY = (68,68,68) #test
# GREY = (200, 200, 200)

# DEFAULT_BACKROUND_1_COLOR = (255,255,255)#white
# DEFAULT_BACKROUND_2_COLOR = (0,0,0) #black
# DEFAULT_TEXT_COLOR = (255,255,255)#white

colors = {'backround_1':  (255,255,255),#white
          'backround_2':  (0,0,0),#black
          'default_text': (255,255,255),#white
          'highlight':    {}
                                                                        }
char_types = {'remove'      : ['.'],
              'blend'       : [':'],
              'color'       : ['-', '='],
              'whitespace'  : [' ']}


#returns lines to make an ascii art txt file of image AND returns dict matching chars to colors (awful func, should be split up)
print('Converting image to ascii art lines and getting color equivalents...')
original_ascii_lines, color_chars = ascii_art.convert_image_to_color_equiv_ascii_art(input_image_filename, cols, scale)

#writes ascii lines to a txt file, not needed for function but helpful for tinkering
print('Writing original ascii lines to txt file...')
tools.write_text_file(original_ascii_art_filename, original_ascii_lines)

#still need some way to get char_types from color_chars, probably through UI!!!!!!!!!!!!!!

#add the necessary chars with their color equivalents to highlight chars
for c_char, color in color_chars.items():
    if c_char in char_types['color']:
        colors['highlight'][c_char] = color
# print('colors:', colors)#````````````````````````````````````````````````````````````````````````

#read in the text that will be colored to show a picture
print('Reading in data text file...') 
data = tools.read_text_file(data_text_filename)

#creates new txt file by editing the original ascii txt image, removes to slim sharpen image, blends to set up for multi-color final image
print('Creating edited ascii art lines...')
edited_ascii_lines = ascii_image_editor.edit_ascii_lines(original_ascii_lines, char_types)  

#also need something to check for and correct incomplete editing - blend chars left behind, ect..., probably just UI

#writes ascii lines to a txt file, not needed for function but helpful for tinkering
print('Writing edited ascii lines to txt file...')
tools.write_text_file(edited_ascii_art_filename, edited_ascii_lines ) 


#turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
data_str = tools.format_data(data)
num_chars = len(data_str)
word_list = data_str.split(' ')



#turn true_dimension_ratio into max number of lines and max chars per line
ideal_dimentions = tools.calc_ideal_dimentions(true_dimension_ratio, num_chars)

#make list of lines to be output in final image
lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)
# print("number of lines:", len(lines))

#look at text image lines to get cords of chars to be highlighted in final image
highlight_cords = tools.get_highlight_cords(edited_ascii_lines)
# print(highlight_cords)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
# for h_char, cords in highlight_cords.items():#`````````````````````````````````````````````````````````````````````````````````````
#     print(h_char)#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#adjust the highlight cords to compensate for the difference between the width of a char and the height of a line
adjusted_highlight_cords = tools.adjust_highlight_cords(highlight_cords, image_resize_ratio)

#put it all together and what have you got?  Bippity Boppity BOO!
print('Creating Image...')
image = text_image.text_image(lines, colors, adjusted_highlight_cords)

# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
image.save(final_image_filename, subsampling=0, quality = 100)

image.show()




