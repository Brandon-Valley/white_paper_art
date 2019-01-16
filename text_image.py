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
        x_draw, x_paste = 0, 0
        
        for letter_num in range(len(line)):
            letter = line[letter_num]
            
            letter_cords = [line_num, letter_num]
            cur_char = lines[line_num][letter_num]
            
            for color, cord_list in color_cords.items():
                if letter_cords in color_cords[color]:
                    char_color = color
                    break

                else: #this was tabbed one to the left forever and nothing bad happened so it probably does nothing
                    char_color = default_colors['default_text']
    
            draw.text((x_draw, letter_h * line_num), letter, char_color, font)#font = font

            x_draw += letter_w
            x_paste += letter_w
        line_num += 1
        

    return image







import GUI
if __name__ == '__main__':
    GUI.main()