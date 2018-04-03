import PIL.ImageFont
from PIL import Image, ImageDraw
from tkinter import font


def load_font(font_path = None, size = 40):
    try:
        font = PIL.ImageFont.truetype(font_path, size)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')
    return font


def get_aspect_ratio(font):
    #the font dimensions you get from this should be the same for any single character as long as you are using a mono-spaced font
    font_dims = font.getsize("a")
    font_width = font_dims[0]
    font_height = font_dims[1]
    aspect_ratio = font_width / font_height
    return aspect_ratio

# 
# def get_font_size(font_path = None):
#     # choose a font (you can see more detail in my library on github)
# #     font_path = None #removed for testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     large_font = 40#works with 40  # get better resolution with larger size
# #     font_path = font_path or 'HelveticaBold.ttf'#'cour.ttf' ## # Courier New. works in windows. linux may need more explicit path
# #     font_path = font_path or 'cour.ttf'# ## # Courier New. works in windows. linux may need more explicit path
#     try:
#         font = PIL.ImageFont.truetype(font_path, size=large_font)
#     except IOError:
#         font = PIL.ImageFont.load_default()
#         print('Could not use chosen font. Using default.')
#     
#     # make the background image based on the combination of font and lines
#     pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
#     
# #     longest_line = tools.find_longest_line(lines)
# #     max_line_width = pt2px(font.getsize(longest_line)[0])
#     
#     
# 
# #     max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
#     # max height is adjusted down because it's too large visually for spacing
#     test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     max_height = pt2px(font.getsize(test_string)[1])
#     
# #     print ('in test_image, font size: ' , font.getsize(test_string))#`````````````````````````````````````````````````````````````
#     return(font.getsize("a"))#return(font.getsize(test_string))


