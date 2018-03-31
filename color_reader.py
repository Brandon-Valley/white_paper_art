#might be useful later, saves image with only N most-frequent colors:  https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image

from PIL import Image



#return key whose value is highest
def high_key(d):
    high_val = 0
    high_key = 0
    for key, val in d.items():
        if val > high_val:
            high_key = key
            high_val = val
    return high_key


#returns single most common color in image
def most_common_color(rgb_image, height, width):
#     print('in color_reader, height: %s  width: %s' %(height, width))#`````````````````````````````````````````````````````````````````````
    image_colors = {}
    for x in range(width):
        for y in range(height):
            r, g, b = rgb_image.getpixel((x, y))
            #check if this color has been seen before, if not, add to list, if so, increase count
            if (r, g, b) in image_colors:
                image_colors[(r, g, b)] += 1
            else:
                image_colors[(r, g, b)] = 1

    #return the color with the highest count
    return high_key(image_colors)

# def most_common_color_odd_file(color_tile_img_BMP):
#     #.crop wants to make color_tile into .BMP which I dont feel like dealing with so save as jpg to work with it
#     temp_filename = 'color_tile.jpg'
#     color_tile_img_BMP.save(temp_filename)
#     color_tile_img = Image.open(temp_filename)
#     rgb_color_tile_img = color_tile_img.convert('RGB')#not sure if needed
# #                 rgb_color_tile_img.show()#`````````````````````````````````````````````````````````````
#     
#     tile_W, tile_H = rgb_color_tile_img.size[0], rgb_color_tile_img.size[1]
#     color_equiv = color_reader.most_common_color(rgb_color_tile_img, tile_H, tile_W)
# #                 print ('equiv color:', color_equiv)#```````````````````````````````````````````````````````````````
#     
#     #done with jpg
#     rgb_color_tile_img.close()
#     color_tile_img.close()
#     os.remove(temp_filename)
#     
#     return color_equiv



#example main
def main():
    input_image_filename = 'color_tile1.jpg'
    im = Image.open(input_image_filename)
    rgb_im = im.convert('RGB')#not sure if needed
     
    # store dimensions
    W, H = rgb_im.size[0], rgb_im.size[1]
    print("input image dims: %d x %d" % (W, H))
     
    print(most_common_color(rgb_im, H, W))


# # call main
if __name__ == '__main__':
    main()




