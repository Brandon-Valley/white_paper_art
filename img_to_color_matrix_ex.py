
from PIL import Image

# import color_reader
import tools
import color_cords

import time






# #for testing
# def colors_to_ascii(tile_color_matrix):
#     ascii_chars = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"
#     leftover_ascii_char = '$'
#     ascii_matrix = []
#     ascii_color_equivs = {}
#     
#     for row_list in tile_color_matrix:
#         ascii_row_str = ''
#         for tile_color in row_list:
#             
#             if tile_color in ascii_color_equivs:
#                 pass
#             elif len(ascii_chars) != 0:
#                 ascii_color_equivs[tile_color] = ascii_chars[0]
#                 ascii_chars = ascii_chars[1:] #pop front
#             else:#if all ascii_chars have been used up
#                 ascii_color_equivs[tile_color] = leftover_ascii_char
#                 
#             ascii_row_str += (ascii_color_equivs[tile_color])
#         ascii_matrix.append(ascii_row_str)
#         
#     return ascii_matrix




def main():
    input_image_filename = 'test_pics/bitcoin2046.png'
    output_filename = 'zzz_img_to_color_test_OUTPUT.txt'
    scale = 0.43
    cols = 200
    input_image_background_color = (255, 255, 255)
    
    print('working...')
    start_time = time.time()
#     tile_color_matrix = color_matrix.get_color_tile_matrix(input_image_filename, cols, scale, True)
    c_cords = color_cords.get_color_cords(input_image_filename, cols, scale, input_image_background_color)
    end_time = time.time()
    print('func took: ' , end_time - start_time)
    
    print('color_cords:  ', c_cords)
    
#     count = 0
#     for row_list in color_tile_matrix:
#         print('%s:  %s' %(count, row_list))
#         count +=1

#     ascii_matrix = colors_to_ascii(tile_color_matrix)
#     print(ascii_matrix)
#     
#     tools.write_text_file(output_filename,ascii_matrix)
    print('done!')



# call main
if __name__ == '__main__':
    main()