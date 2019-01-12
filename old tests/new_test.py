import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

WHITE = 0  # PIL color to use for "on"
BLACK = 255  # PIL color to use for "off"




def main():
    image = text_image('content.txt')
    image.show()
    image.save('content.png')


def text_image(text_path, font_path=None):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    text_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())
 

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=WHITE)
    draw = PIL.ImageDraw.Draw(image)
    
    
    fill = " o "
    x = 0
    w_fill, y = draw.textsize(fill)
    x_draw, x_paste = 0, 0

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        for c in line:
            w_full = draw.textsize(fill+c)[0]
            w = w_full - w_fill     # the width of the character on its own
            draw.text((x_draw,0), fill+c, WHITE)
            iletter = image.crop((x_draw+w_fill, 0, x_draw+w_full, y))
            image.paste(iletter, (x_paste, 0))
            x_draw += w_full
            x_paste += w
            
            
#             draw.text((horizontal_position, vertical_position),
#                       letter, fill=BLACK, font=font) #ON means the letters will be black
#             horizontal_position += font.getsize(letter)
    vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


if __name__ == '__main__':
    main()