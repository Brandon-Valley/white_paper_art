from PIL import Image

import color_reader


def get_color_tile_matrix(fileName, cols, scale, moreLevels):    
    tile_color_matrix = []

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

    # generate list of dimensions
    for j in range(rows):
        tile_color_matrix.append([])
        
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        for i in range(cols):
 
            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
   
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