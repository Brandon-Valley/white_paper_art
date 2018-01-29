from PIL import Image, ImageDraw
from random import randint
make_color = lambda : (randint(50, 255), randint(50, 255), randint(50,255))

image = Image.new("RGB", (1200,20), (0,0,0)) # scrap image
draw = ImageDraw.Draw(image)
image2 = Image.new("RGB", (1200, 20), (0,0,0)) # final image

fill = " o "
x = 0
w_fill, y = draw.textsize(fill)
x_draw, x_paste = 0, 0
for c in "The quick brown fox jumps over the lazy dog.":
    w_full = draw.textsize(fill+c)[0]
    w = w_full - w_fill     # the width of the character on its own
    draw.text((x_draw,0), fill+c, make_color())
    iletter = image.crop((x_draw+w_fill, 0, x_draw+w_full, y))
    image2.paste(iletter, (x_paste, 0))
    x_draw += w_full
    x_paste += w
image2.show()