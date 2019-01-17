from PIL import Image

import tools

import GUI #just for testing


def get_color_cords(fileName, cols, aspect_ratio, input_img_background_color, background_text_color):   
    color_cords = []

    color_image = Image.open(fileName).convert('RGB')
    
    x_max = color_image.size[0]
    y_max = color_image.size[1]

    # store dimensions
    W, H = color_image.size[0], color_image.size[1]

    # compute width of tile # used to be w
    tile_w = W / cols

    # compute tile height based on aspect ratio and aspect_ratio #used to be h
    tile_h = tile_w / aspect_ratio
    
    
    half_pixles_per_tile = ( tile_w * tile_h ) / 2
    
    # compute number of rows
    rows = int(H / tile_h)

    # check if image size is too small
    if cols > W or rows > H:
        raise Exception("ERROR:    Image too small for specified cols, choose a higher resolution image from google or reduce image size in the GUI")
#         print("Image too small for specified cols!")
#         exit(0)

    # generate list of dimensions
    for j in range(rows):
        line_color_cords = []
        y_pos = j * tile_h
         
        for i in range(cols):   #for every tile:
            x_pos = i * tile_w
             
            potential_tile_colors = {}
            
            #find the most common color in the tile
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
#             tile_cord = [j, i] 
                
            if tile_color == input_img_background_color:
                line_color_cords.append(background_text_color)
            else:
                line_color_cords.append(tile_color)
        color_cords.append(line_color_cords)
    return color_cords

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
    
    
    
    
if __name__ == '__main__':
    GUI.main()   