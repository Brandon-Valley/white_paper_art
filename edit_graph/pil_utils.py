from PIL import Image
import PIL.ImageOps 

import numpy as np


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#
# Uses Direct PIL import
#
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def open_img(path):
    return Image.open(path) 

# dims: (left, top, right, bottom)
# dims are the dims needed to make the box to cut out of og img, not how much to trim from each side
def crop_img(img, dims):
    return img.crop(dims)

# dims: (left, top, right, bottom)
# cuts dim amount off of og img from each side
def crop_from_each_side(img, dims):
    width, height = img.size
    return img.crop((dims[0], dims[1], width - dims[2], height - dims[3]))
    

def show_img_from_path(img_path):
    img = open_img(img_path)
    img.show()
    
    
# dims: like (5185, 4000)    
def make_solid_color_img(dims, color, out_file_path):
    img = Image.new('RGB', dims, color)
    img.save(out_file_path)
    
  
def invert_colors(img):
    return PIL.ImageOps.invert(img)
    
def invert_colors_by_path(input_img_path, output_img_path):
    image = Image.open(input_img_path)
    inverted_image = invert_colors(image)
    inverted_image.save(output_img_path)
    


    
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#
# Simple Tools
#
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    
def get_pixel_color_grid_from_path(input_img_path):
    img = open_img(input_img_path)
    return get_pixel_color_grid(img)
    
# returns a list of lists showing the rgb value of every pixel in an image
# not very efficient
def get_pixel_color_grid(input_img):
    in_img_w, in_img_h = input_img.size
    
    pixel_color_grid = []
    for y in range(in_img_h):
        row_l = []
        for x in range(in_img_w):
            rgb = input_img.getpixel((x,y))
            row_l.append(rgb)
        pixel_color_grid.append(row_l)
    return pixel_color_grid


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#
# Pixel Color Grid Tools
#
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def make_img_from_pixel_color_grid(pixel_color_grid):
    w = len(pixel_color_grid)
    h = len(pixel_color_grid[0])
    dims = (w, h)
    img = Image.new('RGB', dims, 'white')
    
    for x in range(w):
        for y in range(h):
            img.putpixel((x,y), pixel_color_grid[y][x])
    return img
    
def show_pixel_color_grid_as_img(pixel_color_grid):
    make_img_from_pixel_color_grid(pixel_color_grid).show()
    


# scans pixel_color_grid from top and returns row num of first row to contain a pixel that 
# is different from dont_care_color color
def get_row_num_of_first_color_diff(pixle_color_grid, dont_care_color):
    for row_num, row_l in enumerate(pixle_color_grid):
        for rgb in row_l:
            if rgb != dont_care_color:
                return row_num
    raise Exception('ERROR:  image is all one color')
        


# degrees must be 90, 180, or 270
def rotate_pixel_color_grid(in_grid, degrees):
    grid_to_rotate = in_grid
    np_grid = np.rot90(grid_to_rotate, k = 4 - (degrees / 90))  
    
    new_pcg = []
    for row_l in np_grid:
        new_pcg_row_l = []
        for rgb in row_l:
            new_pcg_row_l.append(tuple(rgb))
        new_pcg.append(new_pcg_row_l)
    return new_pcg
    
 



# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#
# Complex Tools
#
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


# trims pic inward from each side until at lease one pixel in the row/col is not the same color as the original border
# not very efficient -- because of rotate_pixel_color_grid
def trim_border(input_img_path, output_img_path):
    rgba_in_img = open_img(input_img_path) 
    in_img = rgba_in_img.convert('RGB')
    
    pixel_color_grid = get_pixel_color_grid(in_img)
    border_color = pixel_color_grid[0][0]
    
     

    top_crop     = get_row_num_of_first_color_diff(pixel_color_grid, border_color)
    left_crop    = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 90), border_color)
    bottom_crop  = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 180), border_color)
    right_crop   = get_row_num_of_first_color_diff(rotate_pixel_color_grid(pixel_color_grid , 270), border_color)
     
    cropped_img = crop_from_each_side(in_img, (left_crop, top_crop, right_crop, bottom_crop))
    cropped_img.save(output_img_path)
    
    
    
if __name__ == '__main__':
    print('in pil_utils main...')
#     input_path = "..\\white_paper_graphs\\btc_graph.jpg"#'../example_pics/big_black_a.jpg'
#     output_path = '../example_pics/trimmed_green_triangle.jpg'
#     
#     trim_border(input_path, output_path)
#     show_img_from_path(output_path)

#     pcg = get_pixel_color_grid_from_path(input_path)
#     show_pixel_color_grid_as_img(pcg)
#     
#     pcg2 = rotate_pixel_color_grid(pcg, 90)
#     show_pixel_color_grid_as_img(pcg2)
#     
#     pcg3 = rotate_pixel_color_grid(pcg, 180)
#     show_pixel_color_grid_as_img(pcg3)

    invert_colors_by_path("C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_g.JPG","C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art_big_data\\white_paper_graphs\\btc_graph_inverted.JPG")



#     test_m = [[0,0,0],
#               [1,2,3]]
#     for r in rotate_pixel_color_grid(test_m, 90):
#         print(r)

#     make_solid_color_img((100, 100), 'black', '../example_pics/big_black_a.jpg')


