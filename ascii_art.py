# Python code to convert an image to ASCII image.
import sys, random, argparse
import numpy as np
import math
import os

from PIL import Image

import color_reader

# gray scale level values from: 
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '





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
def covertImageToAsciiAndGetColors(fileName, cols, scale, moreLevels):
    count_ = 0#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    
    color_chars = {}
    
    # declare globals
    global gscale1, gscale2

    # open image and convert to grayscale
    greyscale_image = Image.open(fileName).convert('L')
    color_image = Image.open(fileName).convert('RGB')
#     image.show()#```````````````````````````````````````````````````````````````````````````

    # store dimensions
    W, H = greyscale_image.size[0], greyscale_image.size[1]
    print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W/cols

    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(H/h)
    
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
        aimg.append("")

        for i in range(cols):

            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

            # crop image to extract tile
            grey_img = greyscale_image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(grey_img))

            # look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

               
            #if haven't seen this char before, add it to color_chars
            if gsval not in color_chars:
                count_ +=1#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print('new color char found:', gsval)#````````````````````````````````````````````````````````
                color_tile_img_BMP = color_image.crop((x1, y1, x2, y2))
                
                #.crop wants to make color_tile into .BMP which I dont feel like dealing with so save as jpg to work with it
                temp_filename = 'color_tile' + str(count_) + '.jpg'
                color_tile_img_BMP.save(temp_filename)
                color_tile_img = Image.open(temp_filename)
                rgb_color_tile_img = color_tile_img.convert('RGB')#not sure if needed
#                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````
    
                tile_W, tile_H = rgb_color_tile_img.size[0], rgb_color_tile_img.size[1]
                color_equiv = color_reader.most_common_color(rgb_color_tile_img, tile_H, tile_W)
                print ('equiv color:', color_equiv)#```````````````````````````````````````````````````````````````
                
                #done with jpg
                rgb_color_tile_img.close()
                color_tile_img.close()
                os.remove(temp_filename)
                
                color_chars[gsval] = color_equiv
                print('color_chars:', color_chars)#`````````````````````````````````````````````````````````````
                print('')#`````````````````````````````````````````````````````````````````````````````````````
#                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````````
#                 rgb_color_tile_img.save('color_tile_' + gsval + '_.jpg')#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
                
#             if gsval == '-':#?|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                 img2 = color_image.crop((x1, y1, x2, y2))
#                 img2.show()
            
            # append ascii char to string
            aimg[j] += gsval
    print('count_:' , count_)#````````````````````````````````````````````````````````````````````````
    # return txt image
    return aimg, color_chars

# main() function
def convert_image_to_color_equiv_ascii_art(imgFile, outFile, cols, scale):
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=False)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
# 
    # parse args
    args = parser.parse_args()#are these used?????????????????????????????????????????
  
#     imgFile = 'bitcoin.png'#args.imgFile
# 
#     # set output file
#     outFile = 'out.txt'
# #     if args.outFile:
# #         outFile = args.outFile
# 
#     # set scale default as 0.43 which suits
#     # a Courier font
#     scale = 0.43
# #     if args.scale:
# #         scale = float(args.scale)
# 
#     # set cols
#     cols = 100
#     if args.cols:
#         cols = 120#int(args.cols)

    print('generating ASCII art...')
    # convert image to ascii txt
    aimg, color_chars = covertImageToAsciiAndGetColors(imgFile, cols, scale, args.moreLevels)
#     print(aimg)#```````````````````````````````````````````````````````````````````````````

    # open file
    f = open(outFile, 'w')

    # write to file
    for row in aimg:
        f.write(row + '\n')

    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)
    
    return color_chars

# # call main
# if __name__ == '__main__':
#     main()