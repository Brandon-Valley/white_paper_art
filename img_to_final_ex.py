import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint

import tools
import text_image
import ascii_art
import ascii_image_editor
import color_matrix
import offset
from test.datetimetester import OTHERSTUFF
# from IPython.testing.iptest import have
# from scipy.sparse.linalg.eigen.arpack.tests.test_arpack import CheckingLinearOperator


# might be able to get more colors if you stop making all the information passed by making new ascii pics, num colors currently limited
# by num ascii chars, should pass list of colors insted
# 
# need to find out why it reads whitespace as non-whitepace before doing ^^^^^^^^
# 
# will still need to be able to make color based and greyscale based ascii art for testing purposes
# 
# maybe not having to find a free ascii char for each color will save some time?
# 
# time saver: when finding the most common color in a tile, check every once and a shile if you need to be gathering colors still, if you have
# already read 51% of all the pixles and they are all the same, should just return that color and quit CheckingLinearOperator
# 
# need way to test funcs for time to see if i am even speeding things up at all
# 
# time saver:  if croping takes a long time, maybe I can check for the most common color in a tile sized region of 
# the oringinal image instead of chroping out a tile, then checking that for it's most common color
# 
# why is there a space in front of every line?


# todo:
# 
# figure out font stuff
# 
# finish offset
#     -need to make trimming
#         -need to add whitespace stuff
#         
# make tinker tool
# 
# figure out UI / final file structure stuff
# 
# not needed for whitepapers:
#     figure out how to use larger text file inputs like full_paper10x
#     


input_image_filename = 'test_pics/zzz_change_png_background_output.png'
data_text_filename = 'full_paper.txt'#satoshi whitepaper in a txt file

background_change_needed = True

# original_ascii_art_filename = 'ascii_' + input_image_filename.split('.')[0] + '.txt'#need???????????????????????????????????????
# edited_ascii_art_filename = 'EDITED_' + original_ascii_art_filename#need?????????????????????????????????????????????
# text_image_filename = 'EDITED_data_dash.txt'      #picture of bitcoin icon

final_image_filename = 'TEST_OUTPUT.png'

# set scale default as 0.43 which suits
# a Courier font
scale = 0.43

# set cols
cols = 150 #made smaller for testing, was 200

const_HxW_ratio = 5150/9600 #found by making a 99x99 txt file and looking at dimensions of image
image_resize_ratio = .8

#2/3:
# a a a
# a a a
desired_dimension_ratio = 1/1

#find correct image dimensions by adjusting desired ratio for the difference between the length of a char and the height of a line
true_dimension_ratio = desired_dimension_ratio * const_HxW_ratio


offset_type = 'centered'

#replace this bull shit with something to  deal with whitespace
default_colors = {'backround_1':  (255,255,255),#white
                  'backround_2':  (0,0,0),#black
                  'default_text': (255,255,255)}#white

#                                                                         }
# char_types = {'remove'      : [':>{"'],
#               'blend'       : [''],
#               'color'       : "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.",#['-', '=','+','*','#','%', '@'],
#               'whitespace'  : [' ']}

# tinker = False

# #returns lines to make an ascii art txt file of image AND returns dict matching chars to colors (awful func, should be split up)
# print('Converting image to ascii art lines and getting color equivalents...')
# original_ascii_lines, color_chars = ascii_art.convert_image_to_color_equiv_ascii_art(input_image_filename, cols, scale)

# #writes ascii lines to a txt file, not needed for function but helpful for tinkering
# print('Writing original ascii lines to txt file...')
# tools.write_text_file(original_ascii_art_filename, original_ascii_lines)

#still need some way to get char_types from color_chars, probably through UI!!!!!!!!!!!!!!

# #add the necessary chars with their color equivalents to highlight chars
# for c_char, color in color_chars.items():
#     if c_char in char_types['color']:
#         colors['highlight'][c_char] = color
# print('colors:', colors)#````````````````````````````````````````````````````````````````````````
# print('num_highlight_cords:', len(colors['highlight']))#```````````````````````````````````````````````````````````


# if tinker == False:    
# #creates new txt file by editing the original ascii txt image, removes to slim sharpen image, blends to set up for multi-color final image
# print('Creating edited ascii art lines...')
# edited_ascii_lines = ascii_image_editor.edit_ascii_lines(original_ascii_lines, char_types)  

#also need something to check for and correct incomplete editing - blend chars left behind, ect..., probably just UI

# #writes ascii lines to a txt file, not needed for function but helpful for tinkering
# print('Writing edited ascii lines to txt file...')
# tools.write_text_file(edited_ascii_art_filename, edited_ascii_lines ) 
    
# else:
# #read in tinkered with edited txt file
# print('Reading in data text file...') 
# edited_ascii_lines = tools.read_text_file(edited_ascii_art_filename)



#read in the text that will be colored to show a picture
print('reading in data text file...') 
data = tools.read_text_file(data_text_filename)

#turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
print('formatting data into word list...')
data_str = tools.format_data(data)
num_chars = len(data_str)
word_list = data_str.split(' ')


#turn true_dimension_ratio into max number of lines and max chars per line
print('calculating ideal text image dimensions...')
ideal_dimentions = tools.calc_ideal_dimentions(true_dimension_ratio, num_chars)

#make list of lines to be output in final image
print('creating text lines...')
lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)
# print("number of lines:", len(lines))

#gets matrix of colors from image
print('building color_matrix from original image...')
img_color_matrix = color_matrix.get_color_tile_matrix(input_image_filename, cols, scale, True)
# print(img_color_matrix)#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#look at text image lines to get cords of chars to be highlighted in final image
print('making first round of color cords...')
color_cords = tools.get_color_cords(img_color_matrix)
# print(color_cords)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
# for h_char, cords in highlight_cords.items():#`````````````````````````````````````````````````````````````````````````````````````
#     print(h_char)#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#adjust the highlight cords to compensate for the difference between the width of a char and the height of a line
print('adjusting color cords to fit the image_risize_ratio...')
adjusted_color_cords = tools.adjust_color_cords(color_cords, image_resize_ratio)

print('adding offset to adjusted_color_cords THIS FUNCTION IS INCOMPLETE!!!!!!!!!!!!')
offset_adjusted_color_cords = offset.offset_color_cords(adjusted_color_cords, offset_type)

#put it all together and what have you got?  Bippity Boppity BOO!
print('creating final image...')
image = text_image.text_image(lines, offset_adjusted_color_cords, default_colors)

# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
print('saving high-resolution image...')
image.save(final_image_filename, subsampling=0, quality = 100)

print('showing low-resolution image...')
image.show()




