from PIL import Image

import color_reader


def get_color_tile_matrix(fileName, cols, scale, moreLevels):    
    tile_color_matrix = []

    color_image = Image.open(fileName).convert('RGB')
#     image.show()#```````````````````````````````````````````````````````````````````````````

    # store dimensions
    W, H = color_image.size[0], color_image.size[1]
#     print("input image dims: %d x %d" % (W, H))

    # compute width of tile # used to be w
    tile_w = W/cols

    # compute tile height based on aspect ratio and scale #used to be h
    tile_h = tile_w / scale
    
    print('in color_matrix, tile_h: %s  tile_w: %s' %(tile_h, tile_w))#```````````````````````````````````````````````````````````````````

    # compute number of rows
    rows = int(H / tile_h)
    
#     print("cols: %d, rows: %d" % (cols, rows))
#     print("tile dims: %d x %d" % (tile_w, tile_h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # generate list of dimensions
    for j in range(rows):
        x_pos = j * tile_w
        
        tile_color_matrix.append([])
#         tile_color_matrix_line = []
        
        y1 = int(j*tile_h)
        y2 = int((j+1)*tile_h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        for i in range(cols):
#             y_pos = i * tile_h
#             
#             tile_colors = {}
#             for x in range(tile_w):
#                 for y in range(tile_h):
#                     r, g, b = rgb_image.getpixel(( x_pos + x , y_pos + y ))
#                     #check if this color has been seen before, if not, add to list, if so, increase count
#                     if (r, g, b) in image_colors:
#                         image_colors[(r, g, b)] += 1
#                     else:
#                         image_colors[(r, g, b)] = 1
#                         
#             tile_color_matrix_line.append(color_reader.high_key(tile_colors))
#         tile_color_matrix.append( tile_color_matrix_line )


 
            # crop image to tile
            x1 = int(i*tile_w)
            x2 = int((i+1)*tile_w)
    
            # correct last tile
            if i == cols-1:
                x2 = W
                
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
    
            tile_color_matrix[j].append( tile_color )

    return tile_color_matrix