import PIL.ImageFont
from PIL import Image, ImageDraw
from tkinter import font

import tools
import global_constants


def load_font(font_path = None, size = 40):
    try:
        font = PIL.ImageFont.truetype(font_path, size)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')
    return font


def get_aspect_ratio(font_pth):
    dummy_font = load_font(font_pth)
    
    #the font dimensions you get from this should be the same for any single character as long as you are using a mono-spaced font
    font_dims       = dummy_font.getsize("a")
    font_width      = font_dims[0]
    font_height     = font_dims[1]
    aspect_ratio    = font_width / font_height
    return aspect_ratio


    # to get bigger final images, start looking here, in text_image, the final image is made by making 2 images of equal size, so 
    #you have to do the same here, if you can find a way to not need to make both huge images, you can double the size of your final img!!!!!!!!!!!!!!!!!!!!!!
def font_size_valid(font, txt_lines):
    try:
        image_dims  = tools.calc_img_dims(txt_lines, font)
        scrap_image_1 = Image.new("RGB", image_dims, 'white')
        scrap_image_2 = Image.new("RGB", image_dims, 'white')
        
        #not sure if these 2 lines do anything   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        scrap_image_1.close()
        scrap_image_2.close()
        return True
    except:
        return False


def largest_possable_font(font_path, font_size, txt_lines):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ;', txt_lines)#111111111111111111111111111111111111111111111111111111111111111
    
    #need??????????????????????????????????????????????????????????????????????????????????????????????????????????????
    num_lines = len(txt_lines)
    longest_txt_line = tools.find_longest_line(txt_lines)
    longest_line_len = len(longest_txt_line)
#     print('here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')#````````````````````````````````````````````````````````````````

    cur_font = load_font(font_path, global_constants.MAX_FONT_SIZE)

    print('cur_font size: ', cur_font.size)#`````````````````````````````````````````````````````````````````````````````````````````````
    
    #find right order of magnitude
    while(font_size_valid(cur_font, txt_lines) == False):
        new_font_size = int(cur_font.size / 10)
        cur_font = load_font(font_path, new_font_size)
        
    print('right order of mag: ', cur_font.size)#``````````````````````````````````````````````````````````````````````````````````
    
    small_font_size = cur_font.size
    large_font_size = cur_font.size * 10
    diff = large_font_size - small_font_size
    
    # find the largest possible size
    while(diff > 1):
        print('cur_font.size: %s   diff: %s   small_font_size: %s   large_font_size: %s' %(cur_font.size, diff, small_font_size, large_font_size)) #`````````````````````````````````````````````````````````````````````````````````````````````
        #raise font size by half diff until you hit a size thats too big
        while(font_size_valid(cur_font, txt_lines) == True):
            print('    cur_font.size: %s   diff: %s   small_font_size: %s   large_font_size: %s' %(cur_font.size, diff, small_font_size, large_font_size)) #`````````````````````````````````````````````````````````````````````````````````````````````
            small_font_size = cur_font.size
            diff = large_font_size - small_font_size
            
            new_font_size = small_font_size + int(diff / 2)
            cur_font = load_font(font_path, new_font_size)
        
        #reduce font size by half diff until you hit a size thats too small    
        while(font_size_valid(cur_font, txt_lines) == False and diff > 1):
            print('        cur_font.size: %s   diff: %s   small_font_size: %s   large_font_size: %s' %(cur_font.size, diff, small_font_size, large_font_size)) #`````````````````````````````````````````````````````````````````````````````````````````````
            large_font_size = cur_font.size
            diff = large_font_size - small_font_size
            
            new_font_size = large_font_size - int(diff / 2)
            cur_font = load_font(font_path, new_font_size)
    
    print('perfect font size: ', cur_font.size)#`````````````````````````````````````````````````````````````````````````````````````````
    
#     return cur_font    
    return load_font(font_path, cur_font.size - 0)#```````````````````````````````````````````````````````````````````````````````````


def make_font(font_path, font_size, text_lines):
    if font_size == global_constants.MAX_FONT_SIZE_STR:
        return largest_possable_font(font_path, font_size, text_lines)
#         font_size = 80#```````````````````````````````````````````````````````````````````````````````````````````````````````````
        
    
    return load_font(font_path, font_size)
    





import GUI
if __name__ == '__main__':
    GUI.main()   
