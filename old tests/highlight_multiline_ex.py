from PIL import Image, ImageDraw
from random import randint
make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))

WHITE = (254,254,254)
BLACK = (0,0,0)
YELLOW = (222, 224, 68)

lines = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
         'cccccccccccccccccccccccccccccccccccccc']



highlight_cords = [    [0,3],
                       [0,4],
                       [0,7],
                       [1,3],
                       [1,9] ]


backround_color = BLACK
default_text_color = WHITE
highlight_color = YELLOW


image = Image.new("RGB", (1200,400), backround_color) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (1200, 200), (0,0,0)) # final image


fill = " o "
x = 0
w_fill, y = draw.textsize(fill)



line_num = 0
for line_num in range(len(lines)):
    line = lines[line_num]
    x_draw, x_paste = 0, 0
    
    for letter_num in range(len(line)):
        letter = line[letter_num]
        w_full = draw.textsize(fill + letter)[0]
        w = w_full - w_fill     # the width of the character on its own
        
        letter_cords = [line_num, letter_num]
        if letter_cords in highlight_cords:
            color = highlight_color
        else:
            color = default_text_color
        draw.text((x_draw, y * line_num), fill + letter, color)
    
        iletter = image.crop((x_draw + w_fill, 0, x_draw + w_full, y * len(lines)))
        image2.paste(iletter, (x_paste, 0))
        x_draw += w_full
        x_paste += w
    line_num += 1
image2.show()