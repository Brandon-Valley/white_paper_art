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


