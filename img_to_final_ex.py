
import tools
import text_image
import color_cords
import offset
import font_tools


#IF IMAGE STARTS LOOKING WEIRD, LOOK INTO WHY SOMETIMES IN COLOR_CORDS, 
#THERE ARE 2 OF THE SAME CORD IN ONE COLOR'S LIST, COULD HAVE TO DO WITH ROUNDING? NOT SURE IF IT EFFECTS OTHER THINGS

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
# the oringinal image instead of croping out a tile, then checking that for it's most common color
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


input_image_filename = 'test_pics/bitcoin2046.png'
data_text_filename = 'full_paper.txt'

# background_change_needed = True

final_image_filename = 'TEST_OUTPUT.png'

# set cols
cols = 110#made smaller for testing, was 200

#'cour.ttf'
# 'Consolas.ttf'
font_path = 'fonts/' + 'Consolas.ttf'

#found by making a 99x99 txt file and looking at dimensions of image,
#used to get the best dimentions for laying out text, nothing to do with the image
const_HxW_ratio = 5150 / 9600  
  
font_size = 40# get better resolution with larger size  

#2/3:
# a a a
# a a a
desired_dimension_ratio = 1/1

#find correct image dimensions by adjusting desired ratio for the difference between the length of a char and the height of a line
true_dimension_ratio = desired_dimension_ratio * const_HxW_ratio

# 0, 0 = centered
image_position = {'x_pos': 0,
                  'y_pos': 0}

#set this to None for no background color seperation
input_image_background_color = (255, 255, 255)

#background 
#replace this bull shit with something to  deal with whitespace
default_colors = {'background_image':  (255,255,255),#white
                  'final_image_background':  (0,0,0),#black
                  'default_text': (255, 255, 255)}#white





print('getting font properties...')
font = font_tools.load_font(font_path, font_size)
aspect_ratio = font_tools.get_aspect_ratio(font)


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
color_cords = color_cords.get_color_cords(input_image_filename, cols, aspect_ratio, input_image_background_color)
# print(img_color_matrix)#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print('calculating and adding user defined offset to adjusted_color_cords...')
offset_color_cords = offset.offset_color_cords(color_cords, image_position, lines)
 
#put it all together and what have you got?  Bippity Boppity BOO!
print('creating final image...')
image = text_image.text_image(lines, offset_color_cords, default_colors, font)#offset_adjusted_
 
# image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
print('saving high-resolution image...')
image.save(final_image_filename, subsampling = 0, quality = 100)
 
print('showing low-resolution image...')
image.show()
 
print('done!')
 


