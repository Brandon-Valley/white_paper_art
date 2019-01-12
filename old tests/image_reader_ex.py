import ascii_art
import tools



input_image_filename = 'bitcoin.png'#args.imgFile
output_ascii_art_filename = 'ascii_' + input_image_filename.split('.')[0] + '.txt'

# set scale default as 0.43 which suits
# a Courier font
scale = 0.43

# set cols
cols = 100

#makes ascii art txt file of image and returns dict matching chars to colors (awful func, should be split up)
color_chars = ascii_art.convert_image_to_color_equiv_ascii_art(input_image_filename, output_ascii_art_filename, cols, scale)
print('color_chars:', color_chars)#`````````````````````````````````````````````````````````````````````````````````````

