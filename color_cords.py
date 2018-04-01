from PIL import Image

import tools



def get_color_cords(fileName, cols, scale, background_color):   
    color_cords = {} 

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
    
    half_pixles_per_tile = ( tile_w * tile_h ) / 2
    
    # compute number of rows
    rows = int(H / tile_h)
    
#     print("cols: %d, rows: %d" % (cols, rows))
#     print("tile dims: %d x %d" % (tile_w, tile_h))

    # check if image size is too small
    if cols > W or rows > H:
        raise Exception("ERROR:    Image too small for specified cols!")
#         print("Image too small for specified cols!")
#         exit(0)

    # generate list of dimensions
    for j in range(rows):
        y_pos = j * tile_h
         
        for i in range(cols):   #for every tile:
            x_pos = i * tile_w
             
            potential_tile_colors = {}
            
            x = 0
            while(x < int( tile_w ) and x_pos + x <= x_max):
                
                y = 0
                while(y < int( tile_h ) and y_pos + y <= y_max and majority_color_found(potential_tile_colors, half_pixles_per_tile) == False):
                    r, g, b = color_image.getpixel(( x_pos + x , y_pos + y ))
                    #check if this color has been seen before, if not, add to list, if so, increase count
                    if (r, g, b) in potential_tile_colors:
                        potential_tile_colors[(r, g, b)] += 1
                    else:
                        potential_tile_colors[(r, g, b)] = 1
                    y += 1
              
                x += 1
                         
            #add most common color in tile to color_cords
            tile_color = high_key(potential_tile_colors)
            tile_cord = [j, i] 
            
            if tile_color != background_color:
                if tile_color in color_cords:
                    color_cords[tile_color].append(tile_cord)
                else:
                    color_cords[tile_color] = [tile_cord]

    return trim(color_cords)


#trims back color_cords so that the minimum x and y positions 
def trim(c_cords):
    #find x and y min
    x_min = None
    y_min = None
    
    for color, cord_list in c_cords.items():
        for cord in cord_list:
            x = cord[1]
            y = cord[0]
            if x_min == None and y_min == None:
                x_min = x
                y_min = y
            else:
                if x_min > x:
                    x_min = x
                if y_min > y:
                    y_min = y
                    
    offset_dict = {'x_offset': -1 * x_min,
                   'y_offset': -1 * y_min}
    
    print('in color_cords, un-trimmed color_cords: ', c_cords)#```````````````````````````````````````````````````````````````````````````
    print("in color_cords, offset_dict = " , offset_dict)#`````````````````````````````````````````````````````````````````````````````````
    return tools.apply_offset(c_cords, offset_dict)
    

#return key whose value is highest
def high_key(d):
    high_val = 0
    high_key = 0
    for key, val in d.items():
        if val > high_val:
            high_key = key
            high_val = val
    return high_key

def majority_color_found(t_colors, half):
    result = False
    
    for t_color, c_count in t_colors.items():
        if c_count > half:
            result = True
            
    return result
    
    
    
    
    