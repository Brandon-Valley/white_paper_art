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
        
        scrap_image = Image.new("RGB", image_dims, 'white')  #only making 1 b/c i wanna see what happens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return True
    except:
        return False


def find_max_font_size(font_path, font_size, txt_lines):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ;', txt_lines)#111111111111111111111111111111111111111111111111111111111111111
    num_lines = len(txt_lines)
    
    longest_txt_line = tools.find_longest_line(txt_lines)
    longest_line_len = len(longest_txt_line)





def make_font(font_path, font_size, text_lines):
    if font_size == global_constants.MAX_FONT_SIZE_STR:
        font_size = find_max_font_size(font_path, font_size, text_lines)
    
    return load_font(font_path, font_size)
    





import GUI
if __name__ == '__main__':
    GUI.main()   
