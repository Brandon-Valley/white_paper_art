from PIL import Image, ImageDraw
from random import randint
make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))


words = 'hi this is a string with color'
color1 = (222, 224, 68)
color2 = (2, 56, 78)
color_pos = 5


image = Image.new("RGB", (1200,20), (0,0,0)) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (1200, 20), (0,0,0)) # final image

fill = " o "
x = 0
w_fill, y = draw.textsize(fill)
x_draw, x_paste = 0, 0

c_pos = 0
for c in words:
    w_full = draw.textsize(fill+c)[0]
    w = w_full - w_fill     # the width of the character on its own
    
    if c_pos == color_pos:
        color = color1
    else:
        color = color2
    draw.text((x_draw,0), fill+c, color)
    iletter = image.crop((x_draw+w_fill, 0, x_draw+w_full, y))
    image2.paste(iletter, (x_paste, 0))
    x_draw += w_full
    x_paste += w
    
    c_pos += 1
image2.show()