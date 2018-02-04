from PIL import Image, ImageDraw
from random import randint
make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))


color1 = (222, 224, 68)


line_list = ['aaaaaaaaaaaaaaaaaaaaa','bbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccc', 'DDDDDDDDDDDDDDDDDDDDDDD']

with open('ex_data.txt', 'r') as myfile:
    words=myfile.read().replace('\n', '')


image = Image.new("RGB", (1200,20), (0,0,0)) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (1200, 20), (0,0,0)) # final image

fill = " o "
x = 0
w_fill, y = draw.textsize(fill)
x_draw, x_paste = 0, 0
y_pos = 0

for line in line_list:
    c_pos = 0
    for c in line:
        w_full = draw.textsize(fill+c)[0]
        w = w_full - w_fill     # the width of the character on its own

        draw.text((x_draw, y_pos), fill+c, color1)
        iletter = image.crop((x_draw+w_fill, 0, x_draw+w_full, y))
        image2.paste(iletter, (x_paste, 0))
        x_draw += w_full
        x_paste += w
        
        c_pos += 1
    y_pos += 1
        
image2.show()