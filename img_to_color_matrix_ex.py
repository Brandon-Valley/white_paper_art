# Python code to convert an image to ASCII image.
import sys, random, argparse
import numpy as np
import math
import os

from PIL import Image

import color_reader
from sympy.logic.boolalg import false




#^^^^^ not sure what need!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import tools



# gray scale level values from: 
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '

COLOR_RANGE = 20

#returns true if all elements of both tuples are within range r of each other
def within_range( tup1, tup2, r):
    in_range = True
    if len(tup1) == len(tup2):
        for i in range(len(tup1)):
            if tup1[i] < tup2[i] - r or tup1[i] > tup2[i] + r:
                in_range = False
    return in_range
    


#return greyscale_val such that the final ascii image looks as close to normal ascii art as possable but
#maintain that each char represent only 1 color
def get_color_correct_greyscale_value(scale, ideal_pos, tile_color, color_chars):
#     print('ideal_pos :', ideal_pos)#````````````````````````````````````````````````````````````````````````````````````````````
    ideal_char = scale[ideal_pos]
#     print('testing:', ideal_char, tile_color)#```````````````````````````````````````````````````````
    
    #if this char has been seen before, check to make sure the color matches, 
    #if not, check if the color is known, if color unknown, add a new char
#     if tile_color in color_chars.values():
    tile_color_in_range = False
    for c_color in color_chars.values():
        if within_range(tile_color, c_color, COLOR_RANGE):
            tile_color_in_range = True
            
#     print('am i in range:', tile_color_in_range)#`````````````````````````````````````````````````
    
    if tile_color_in_range == True:
        for c_char, color in color_chars.items():
            if within_range(tile_color, color, COLOR_RANGE):
                return c_char
    else:
        if ideal_char not in color_chars:
            return ideal_char
        else:
#             print('%s taken, need to find different char, tile_color = %s' %(ideal_char, tile_color))#````````````````````````````````````````````````````````
            #make get closest char to ideal to represent new color
            darker_flipped, lighter = scale.split(ideal_char)
            darker = darker_flipped[::-1]
            count = 0
            
            while(count < len(darker) or count < len(lighter)):
                if count < len(darker):
                    cur_char = darker[count]
                    if cur_char not in color_chars:
                        return cur_char
                    
                if count < len(lighter) and count != 0:
                    cur_char = lighter[count]
                    if cur_char not in color_chars:
                        return cur_char
                count += 1
            print('color_chars', color_chars)#```````````````````````````````````````````````````````````````````````````````````````
            raise NameError ('Ran out of colors, number of colors allowed =  %s' %(len(scale)))
            
        
#         cur_pos = ideal_pos
#         #go up the list until find un-used char for new color, loop around if necessary
#         while(ideal_char in color_chars):
#             cur_pos -= 1
#             
#             
#             if cur_pos == -1:
#                 cur_pos = len(scale) - 1
#             else:
#                 if 
            
            
    
    
    
    
#     if ideal_char in color_chars:
#         if tile_color != color_chars[ideal_char]:
#             if tile_color in c
        
        

        
#         #.crop wants to make color_tile into .BMP which I dont feel like dealing with so save as jpg to work with it
#         temp_filename = 'color_tile.jpg'
#         color_tile_img_BMP.save(temp_filename)
#         color_tile_img = Image.open(temp_filename)
#         rgb_color_tile_img = color_tile_img.convert('RGB')#not sure if needed
# #                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````
#         
#         tile_W, tile_H = rgb_color_tile_img.size[0], rgb_color_tile_img.size[1]
#         color_equiv = color_reader.most_common_color(rgb_color_tile_img, tile_H, tile_W)
# #                 print ('equiv color:', color_equiv)#```````````````````````````````````````````````````````````````
#         
#         #done with jpg
#         rgb_color_tile_img.close()
#         color_tile_img.close()
#         os.remove(temp_filename)
        
#         color_chars[gsval] = color_equiv


def getAverageL(image):

    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)

    # get shape
    w,h = im.shape

    # get average
    return np.average(im.reshape(w*h))

#horible func name, should be broken up, but this way is just too easy
def get_color_tile_matrix(fileName, cols, scale, moreLevels):
#     count_ = 0#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    tile_color_matrix = []
    
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    
#     color_chars = {}
    
    # declare globals
#     global gscale1, gscale2

    # open image and convert to grayscale
#     greyscale_image = Image.open(fileName).convert('L')
    color_image = Image.open(fileName).convert('RGB')
#     image.show()#```````````````````````````````````````````````````````````````````````````

    # store dimensions
    W, H = color_image.size[0], color_image.size[1]
#     print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W/cols

    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(H/h)
    
#     print("cols: %d, rows: %d" % (cols, rows))
#     print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
#     aimg = []
    # generate list of dimensions
    for j in range(rows):
        print("j:  " , j)#```````````````````````````````````````````````````````````````````````````````````````````
        tile_color_matrix.append([])
        
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
#         aimg.append("")

        for i in range(cols):

            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

#             # crop image to extract tile
#             grey_img = greyscale_image.crop((x1, y1, x2, y2))
# 
#             # get average luminance
#             avg = int(getAverageL(grey_img))
            
            #crop color tile then convert to jpg
            color_tile_img_BMP = color_image.crop((x1, y1, x2, y2))
            
            
            #.crop wants to make color_tile into .BMP which I dont feel like dealing with so save as jpg to work with it
            temp_filename = 'color_tile'  + '.jpg' #+ str(count_)
            color_tile_img_BMP.save(temp_filename)
            color_tile_img = Image.open(temp_filename)
            rgb_color_tile_img = color_tile_img.convert('RGB')#not sure if needed
#                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````
            
            #get most common color in the color tile 
            tile_W, tile_H = rgb_color_tile_img.size[0], rgb_color_tile_img.size[1]
            tile_color = color_reader.most_common_color(rgb_color_tile_img, tile_H, tile_W)
            
#             print('got new tile color: ', tile_color)#``````````````````````````````````````````````````````````````````
        
        

#             # look up ascii char
#             if moreLevels:
#                 gsval = get_color_correct_greyscale_value(gscale1, int((avg*69)/255), tile_color, color_chars)
# #                 gsval = gscale1[int((avg*69)/255)]
#             else:
#                 gsval = get_color_correct_greyscale_value(gscale2, int((avg*9)/255), tile_color, color_chars)
# #                 gsval = gscale2[int((avg*9)/255)]

#             if gsval == None:
#                 print('gsval NONE - -  color:', tile_color)#```````````````````````````````````````````````````````````````````````````````
#                 print('color_chars:', color_chars)#````````````````````````````````````````````````````````````````````````````````````


            tile_color_matrix[j].append( tile_color )
               
#             #if haven't seen this char before, add it to color_chars
#             if gsval not in color_chars:
#                 count_ +=1#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# #                 print('new color char found:', gsval)#````````````````````````````````````````````````````````
#                 color_tile_img_BMP = color_image.crop((x1, y1, x2, y2))
#                 
#                 #.crop wants to make color_tile into .BMP which I dont feel like dealing with so save as jpg to work with it
#                 temp_filename = 'color_tile' + str(count_) + '.jpg'
#                 color_tile_img_BMP.save(temp_filename)
#                 color_tile_img = Image.open(temp_filename)
#                 rgb_color_tile_img = color_tile_img.convert('RGB')#not sure if needed
# #                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````
#                 
#                 tile_W, tile_H = rgb_color_tile_img.size[0], rgb_color_tile_img.size[1]
#                 color_equiv = color_reader.most_common_color(rgb_color_tile_img, tile_H, tile_W)
# #                 print ('equiv color:', color_equiv)#```````````````````````````````````````````````````````````````
#                 
#                 #done with jpg
#                 rgb_color_tile_img.close()
#                 color_tile_img.close()
#                 os.remove(temp_filename)
#                 
#                 color_chars[gsval] = color_equiv
#                 print('color_chars:', color_chars)#`````````````````````````````````````````````````````````````
#                 print('')#`````````````````````````````````````````````````````````````````````````````````````
#                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````````
#                 rgb_color_tile_img.save('color_tile_' + gsval + '_.jpg')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
                
#             if gsval == '-':#?|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                 img2 = color_image.crop((x1, y1, x2, y2))
#                 img2.show()
            
            # append ascii char to string
            
#             aimg[j] += gsval
#     print('count_:' , count_)#````````````````````````````````````````````````````````````````````````
    # return txt image

    return tile_color_matrix

# # old main() function
# def convert_image_to_color_equiv_ascii_art(imgFile, cols, scale):
#     # create parser
#     descStr = "This program converts an image into ASCII art."#can i remove?????????????????????????????
#     parser = argparse.ArgumentParser(description=descStr)
#     # add expected arguments
#     parser.add_argument('--file', dest='imgFile', required=False)
#     parser.add_argument('--scale', dest='scale', required=False)
#     parser.add_argument('--out', dest='outFile', required=False)
#     parser.add_argument('--cols', dest='cols', required=False)
#     parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
# # 
#     # parse args
#     args = parser.parse_args()#are these used?????????????????????????????????????????
#   
# #     imgFile = 'bitcoin.png'#args.imgFile
# # 
# #     # set output file
# #     outFile = 'out.txt'
# # #     if args.outFile:
# # #         outFile = args.outFile
# # 
# #     # set scale default as 0.43 which suits
# #     # a Courier font
# #     scale = 0.43
# # #     if args.scale:
# # #         scale = float(args.scale)
# # 
# #     # set cols
# #     cols = 100
# #     if args.cols:
# #         cols = 120#int(args.cols)
# 
# #     print('generating ASCII art...')
#     # convert image to ascii txt
#     color_tile_matrix = get_color_tile_matrix(imgFile, cols, scale, True)
# #     print(aimg)#```````````````````````````````````````````````````````````````````````````
# 
# #     # open file
# #     f = open(outFile, 'w')
# # 
# #     # write to file
# #     for row in aimg:
# #         f.write(row + '\n')
# # 
# #     # cleanup
# #     f.close()
# #     print("ASCII art written to %s" % outFile)
#     
#     return aimg, color_chars


#for testing
def colors_to_ascii(tile_color_matrix):
    ascii_chars = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"
    leftover_ascii_char = '$'
    ascii_matrix = []
    ascii_color_equivs = {}
    
    for row_list in tile_color_matrix:
        ascii_row_str = ''
        for tile_color in row_list:
            
            if tile_color in ascii_color_equivs:
                pass
            elif len(ascii_chars) != 0:
                ascii_color_equivs[tile_color] = ascii_chars[0]
                ascii_chars = ascii_chars[1:] #pop front
            else:#if all ascii_chars have been used up
                ascii_color_equivs[tile_color] = leftover_ascii_char
                
            ascii_row_str += (ascii_color_equivs[tile_color])
        ascii_matrix.append(ascii_row_str)
        
    

    return ascii_matrix




def main():
    input_image_filename = 'bitcoin.png'
    output_filename = 'zzz_img_to_color_test_OUTPUT.txt'
    scale = 0.43
    cols = 200
    
    tile_color_matrix = get_color_tile_matrix(input_image_filename, cols, scale, True)
    
#     count = 0
#     for row_list in color_tile_matrix:
#         print('%s:  %s' %(count, row_list))
#         count +=1

    ascii_matrix = colors_to_ascii(tile_color_matrix)
    print(ascii_matrix)
    
    tools.write_text_file(output_filename,ascii_matrix)
    print('done!')



# call main
if __name__ == '__main__':
    main()