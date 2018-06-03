import PIL.ImageFont
from PIL import Image, ImageDraw
import tools


def text_image(lines, color_cords, default_colors, font):    
#     # make the background image based on the combination of font and lines
#     pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
#     
#     longest_line = tools.find_longest_line(lines)
#     max_line_width = pt2px(font.getsize(longest_line)[0])
#     
#     
# 
# #     max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
#     # max height is adjusted down because it's too large visually for spacing
#     test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     max_height = pt2px(font.getsize(test_string)[1])
#         
# #     max_width = pt2px(font.getsize(max_width_line)[0])#just uncommented!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     height = max_height * len(lines) + 2  # perfect or a little oversized
#     
#     width = int(round(max_line_width * 3 + 0))  # a little oversized , needs to be exactly this # or cuts off text
    
    
    img_dims = tools.calc_img_dims(lines, font)

    # to get bigger final images, start looking here, by making both image and image2, you cut the max size of the final image in half!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print('here 0 ,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! font size: ', font.size)#`````````````````````````````````````````````````````````````
    image = Image.new("RGB", img_dims, default_colors['final_image_background']) # scrap image
    print('here 1 ,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! font size: ', font.size)#`````````````````````````````````````````````````````````````
    draw = ImageDraw.Draw(image)
    print('here 2 ,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! font size: ', font.size)#`````````````````````````````````````````````````````````````
    image2 = Image.new("RGB", img_dims, default_colors['background_image']) # final image
    print('here 3 ,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! font size: ', font.size)#`````````````````````````````````````````````````````````````
    
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







import GUI
if __name__ == '__main__':
    GUI.main()