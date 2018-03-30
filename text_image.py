import PIL.ImageFont
from PIL import Image, ImageDraw
import tools


def text_image(lines, color_cords, default_colors, font_size, font_path = None):
    # choose a font (you can see more detail in my library on github)
#     font_path = None #removed for testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     large_font = 40#works with 40  # get better resolution with larger size
#     font_path = font_path or 'HelveticaBold.ttf'#'cour.ttf' ## # Courier New. works in windows. linux may need more explicit path
#     font_path = font_path or 'cour.ttf'# ## # Courier New. works in windows. linux may need more explicit path
#     font = PIL.ImageFont.truetype("Verdana.ttf",14)
    try:
        font = PIL.ImageFont.truetype(font_path, font_size)
#         font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')
    
    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    
    longest_line = tools.find_longest_line(lines)
    max_line_width = pt2px(font.getsize(longest_line)[0])
    
    

#     max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    
    print ('in test_image, font size: ' , font.getsize(test_string))#`````````````````````````````````````````````````````````````
    
#     max_width = pt2px(font.getsize(max_width_line)[0])#just uncommented!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    height = max_height * len(lines) + 2  # perfect or a little oversized
    
    width = int(round(max_line_width * 3 + 0))  # a little oversized , needs to be exactly this # or cuts off text


    image = Image.new("RGB", (width, height), default_colors['backround_2']) # scrap image
    draw = ImageDraw.Draw(image)
    image2 = Image.new("RGB", (width, height), default_colors['backround_1']) # final image
    
    fill = " o "
    x = 0
    w_fill, y = draw.textsize(fill, font)
    
    line_num = 0
    for line_num in range(len(lines)):
        line = lines[line_num]
#         print(line)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        x_draw, x_paste = 0, 0
        
        for letter_num in range(len(line)):
            letter = line[letter_num]
            w_full = draw.textsize(fill + letter, font)[0]
            w = w_full - w_fill     # the width of the character on its own
            
            letter_cords = [line_num, letter_num]
            cur_char = lines[line_num][letter_num]
            
            for color, cord_list in color_cords.items():
                if letter_cords in color_cords[color]:
                    char_color = color
                    break

            else:
                char_color = default_colors['default_text']
    
            draw.text((x_draw, y * line_num), fill + letter, char_color, font)#font = font
        
            iletter = image.crop((x_draw + w_fill, 0, x_draw + w_full, y * len(lines) ))
            
#             iletter.show()#`````````````````````````````````````````````````````````````````````````````````````````````````
            
    #         iletter.show()
    #         sleep(1)
    
            image2.paste(iletter, (x_paste, 0))
            
#                 image2.show()#````````````````````````````````````````````````````````````````````````````````````````````
#             sleep(2)
#             print('x_paste:', x_paste)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            x_draw += w_full
            x_paste += w
        line_num += 1
    return image2