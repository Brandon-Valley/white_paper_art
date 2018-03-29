# -*- encoding: utf8 -*-
import sys
from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGBA", (1000, 1000), 'white')
draw = ImageDraw.Draw(im)

start_y = 7
text = 'hithere heres some text'#u'\u00d1\u00d3yŻ\u00d4Ćgp\u010c\u0137'
for i in range(28, 46, 2):
    font = ImageFont.truetype('cour.ttf', i)
    width, height = font.getsize(text)
    draw.rectangle((0, start_y, width, height + start_y), outline='blue')
    draw.text((0, start_y), text, font=font, fill='black')
    start_y += height + 7

im.crop((0, 0, width + 1, start_y + 2)).save(sys.argv[1])