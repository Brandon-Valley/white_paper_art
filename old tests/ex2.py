


# file=raw_input('what is the name of the file?')
# print file
# 
# f = open(file)
# for s in f:
#     s = s.strip("\n")
# f.close
# print len (s)

s= 'hi there \n'

    
# creates a 50x50 pixel black box with hello world written in white, 8 point Arial text
from PIL import Image, ImageDraw, ImageFont

i = Image.new("RGB", (25,25))
d = ImageDraw.Draw(i)
f = ImageFont.truetype("Arial.ttf", 12)
d.text((0,0), s, font=f)
i.save(open("helloworld.png", "wb"), "PNG")