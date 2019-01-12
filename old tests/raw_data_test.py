import PIL.ImageFont
from PIL import Image, ImageDraw

import sys



input_image_filename = 'test_pics/puppy.jpg'




i = Image.open(input_image_filename)
imgSize = i.size
rawData = i.tobytes()
img = Image.frombytes('L', imgSize, rawData)
img.save('zzz_lmode.png')
img = Image.frombytes('RGB', imgSize, rawData)
img.save('zzz_rgbmode.png')
# img = Image.fromstring('RGBX', imgSize, rawData)
# img.save('rgbxmode.jfif')
# img = Image.fromstring('RGBA', imgSize, rawData)
# img.save('rgbamode.png')
# img = Image.fromstring('CMYK', imgSize, rawData)
# img.save('rgbamode.tiff')

img.convert('L').save('ZZZ_L.png')
img.convert('RGB').save('ZZZ_RGB.png')


print('done!')