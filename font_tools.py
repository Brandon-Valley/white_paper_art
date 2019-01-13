import PIL.ImageFont
from PIL import Image, ImageDraw
from tkinter import font

from fontTools.ttLib import TTFont

import tools
import global_constants


FONTS_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\fonts"


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
        
#         import gc
#         gc.collect()#``````````````````````````` get rid of this ^^^^^^^^^^^^^^^^^```````````````````````````````````````````````````````
#         
        return True
    except:
        return False


def largest_possable_font(font_path, font_size, txt_lines):
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ;', txt_lines)#111111111111111111111111111111111111111111111111111111111111111
    
    #need?????????????????????????????????????????????????????????????????????????????????????????????????????????????? VVVVVVV !????????????????
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

#REALLY need to redo / rename / clean up this func~~~~~~~~~~~~`````````````````````````````````````````````````````````````````````````````````
def make_font(font_path, font_size, text_lines):

    
    if font_size == global_constants.MAX_FONT_SIZE_STR:
        return largest_possable_font(font_path, font_size, text_lines)
#         font_size = 80#```````````````````````````````````````````````````````````````````````````````````````````````````````````
         
     
    return load_font(font_path, font_size)
    






def find_max_font_size(font_path, text_file_path, output_dim_ratio):
    
#     return 23#```````````````````````````````````````````````````````````````````````````````````````````````````
    
    print('getting font aspect ratio...')
    font_aspect_ratio = get_aspect_ratio(font_path)
     
    #read in the text that will be colored to show a picture
    print('reading in data text file...') 
    data = tools.read_text_file(text_file_path)
     
    #turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
    print('formatting data into word list...')
    data_str  = tools.format_data(data)
    num_chars = len(data_str)
    word_list = data_str.split(' ')
     
    #turn true_dimension_ratio into max number of lines and max chars per line
    print('calculating ideal text image dimensions...')
    #find correct image dimensions by adjusting desired ratio for the difference between width and height of a char
    true_dimension_ratio = output_dim_ratio * font_aspect_ratio
    ideal_dimentions = tools.calc_ideal_dimentions(true_dimension_ratio, num_chars)
     
#     return 22#``````````````````````````````````````````````````````````````````````````````````````````````
     
    #make list of lines to be output in final image
    print('creating text lines...')
    lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)

#     return 23#``````````````````````````````````````````````````````````````````````````````````````````````


    dummy_font_size = global_constants.MAX_FONT_SIZE_STR  #this whole section needs a lot of cleaning!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     return 24#``````````````````````````````````````````````````````````````````````````````````````````````
    font = make_font(font_path, dummy_font_size, lines)
    print('returning perfect font size')#``````````````````````````````````````````````````````````````````````````````````````
    return font.size
#     return 24#``````````````````````````````````````````````````````````````````````````````````````````````





#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def char_in_font(unicode_char, font):
    
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
            
#     if unicode_char == '\u2208': #end of txt file
#         return True
    
    return False

#    ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def build_unknown_char_list(lines, font_path):
    unknown_char_list = []
    
    font = TTFont(font_path)
    
    
#     line_num = 1#```````````````````````````````````````````````````````````````````````````````````````````````
    for line in lines:
#         print('checking line: ', line_num)
#         line_num+=1
        
        for char in line:
            if (char_in_font(char, font) == False) and (char not in unknown_char_list):
                print('unknown found')#````````````````````````````````````````````````````````````````````````````````````````
                unknown_char_list.append(char)
    return unknown_char_list
                




import GUI
if __name__ == '__main__':
    GUI.main()   
