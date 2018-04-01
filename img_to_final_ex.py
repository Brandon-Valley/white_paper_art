import PIL.ImageFont
from PIL import Image, ImageDraw
from random import randint

import tools
import text_image
import ascii_art
import ascii_image_editor
import color_cords
import offset
# from test.datetimetester import OTHERSTUFF
import font_size

#MUST USE MONO-SPACED FONTS
#high resolution images will give better results


# from IPython.testing.iptest import have
# from scipy.sparse.linalg.eigen.arpack.tests.test_arpack import CheckingLinearOperator


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


input_image_filename = 'test_pics/bitcoin.png'
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
cols = 150#made smaller for testing, was 200

#found by making a 99x99 txt file and looking at dimensions of image,
#used to get the best dimentions for laying out text, nothing to do with the image
const_HxW_ratio = 5150/9600 
                    
                    
#THE REASON COUR AND DEFAULT WERE WORKING IS BECAUSE THEY ARE BOTH MONOSPACE FONTS,
#THIS MEANS THAT ALL THE CHARS ALWAYS HAVE THE SAME WIDTH, FOR SOME DUMB REASON,
#THE CODE YOU COPIED DOESNT COMPENSATE FOR NON-MONOSPACE FONTS, YOU CAN PROBABLY
#GOOGLE HOW TO CORRECTLY SPACE OUT A NON-MONOSPACE FONT, IT MIGHT BE MORE COMPLICATEDED
#THAN JUST FINDING THE WIDEST CHAR AND ADDING EAQUAL SPACES TO THE FRONT AND BACK TO MAKE
#EACH CHAR THE SAME WIDTH, IDK JUST THOUGHT OF THAT OFF THE TOP OF MY HEAD, DO SOME GOOGLING
#WIKI LINK:                     https://en.wikipedia.org/wiki/Monospaced_font
#MIGHT BE EASIER JUST TO ONLY USE MONOSPACE FONTS IDK
#'cour.ttf'
#'Verdana.ttf'
#'Calibri.ttf'
font_path = 'fonts/' + 'cour.ttf'
# font_path = 'fonts/' + 'cour.ttf'


               
# test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# font_h = font.getsize(test_string)[1]
# font_h = pt2px(font.getsize(test_string)[0])
                                
# font_w = 156
# font_h = 11

font_dims = font_size.get_font_size(font_path)

font_h = font_dims[1]
font_w = font_dims[0]

image_resize_ratio = ( font_h / font_w ) * 12.8   #HAVE NOT FULLY TESTED YET, JUST A GUESS!!!!!!!!!!!!!!!!!!!



font_size = 40#works with 40  # get better resolution with larger size  
                            
# image_resize_ratio = .9 #courier works with .8

#2/3:
# a a a
# a a a
desired_dimension_ratio = 1/1

#find correct image dimensions by adjusting desired ratio for the difference between the length of a char and the height of a line
true_dimension_ratio = desired_dimension_ratio * const_HxW_ratio


offset_type = 'centered'

#set this to None for no background color seperation
input_image_background_color = (255, 255, 255)

#background 
#replace this bull shit with something to  deal with whitespace
default_colors = {'background_image':  (255,255,255),#white
                  'final_image_background':  (0,0,0),#black
                  'default_text': (55,55,55)}#white




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

print('building color_cords from input image...')
color_cords = color_cords.get_color_cords(input_image_filename, cols, scale, input_image_background_color)
# print(img_color_matrix)#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#adjust the color cords to compensate for the difference between the width of a char and the height of a line
print('adjusting color cords to fit the image_risize_ratio...')
adjusted_color_cords = tools.adjust_color_cords(color_cords, image_resize_ratio)

print('adding offset to adjusted_color_cords THIS FUNCTION IS INCOMPLETE!!!!!!!!!!!!')
offset_adjusted_color_cords = offset.offset_color_cords(adjusted_color_cords, offset_type)

#put it all together and what have you got?  Bippity Boppity BOO!
print('creating final image...')
image = text_image.text_image(lines, offset_adjusted_color_cords, default_colors, font_size, font_path)

# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
print('saving high-resolution image...')
image.save(final_image_filename, subsampling = 0, quality = 100)

print('showing low-resolution image...')
image.show()

print('done!')



