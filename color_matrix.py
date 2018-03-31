from PIL import Image


import tools


def get_color_tile_matrix(fileName, cols, scale, moreLevels):    
    tile_color_matrix = []

    color_image = Image.open(fileName).convert('RGB')
    
    x_max = color_image.size[0]
    y_max = color_image.size[1]
#     image.show()#```````````````````````````````````````````````````````````````````````````

    # store dimensions
    W, H = color_image.size[0], color_image.size[1]
#     print("input image dims: %d x %d" % (W, H))

    # compute width of tile # used to be w
    tile_w = W/cols

    # compute tile height based on aspect ratio and scale #used to be h
    tile_h = tile_w / scale
    

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
        y_pos = j * tile_h
        
        tcm_row = []
 
        for i in range(cols):
            x_pos = i * tile_w
             
            tile_colors = {}
            
            x = 0
            while(x < int( tile_w ) and x_pos + x <= x_max):
                
                y = 0
                while(y < int( tile_h ) and y_pos + y <= y_max):
                    r, g, b = color_image.getpixel(( x_pos + x , y_pos + y ))
                    #check if this color has been seen before, if not, add to list, if so, increase count
                    if (r, g, b) in tile_colors:
                        tile_colors[(r, g, b)] += 1
                    else:
                        tile_colors[(r, g, b)] = 1
                    y += 1
              
                x += 1
                         
            tcm_row.append(tools.high_key(tile_colors))
        tile_color_matrix.append( tcm_row )


    return tile_color_matrix