import PIL.ImageFont
from PIL import Image, ImageDraw

import gc

import tools


def text_image(lines, color_cords, default_colors, font):           
    img_dims = tools.calc_img_dims(lines, font)
    
    gc.collect()

    image = Image.new("RGB", img_dims, default_colors['final_image_background']) # scrap image
    draw = ImageDraw.Draw(image)

     
    x = 0
    letter_w, letter_h = draw.textsize("A", font)
    
    Image.MAX_IMAGE_PIXELS = 1000000000   #need this here
    
    line_num = 0
    for line_num in range(len(lines)):
        line = lines[line_num]
        x_draw = 0
        
        for letter_num in range(len(line)):
            letter = line[letter_num]
            
            letter_cords = [line_num, letter_num]

            char_color = color_cords[line_num][letter_num]
    
            draw.text((x_draw, letter_h * line_num), letter, char_color, font)#font = font

            x_draw += letter_w
        line_num += 1
        

    return image







import GUI
if __name__ == '__main__':
    GUI.main()