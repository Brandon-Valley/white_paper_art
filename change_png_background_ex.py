#https://stackoverflow.com/questions/39327265/python-pil-how-can-i-set-the-background-of-an-imagepng-to-white

import numpy as np
import PIL
from PIL import Image


basewidth = 200
img = Image.open("test_pics/bitcoin_high_res.png")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
data = np.array(img)

alpha1 = 0 # Original value
r2, g2, b2, alpha2 = 255, 255, 255,255 # Value that we want to replace it with

red, green, blue,alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
mask = (alpha==alpha1)
data[:,:,:4][mask] = [r2, g2, b2, alpha2]


img = Image.fromarray(data)
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('zzz_change_png_background_output.png')
img.save('test_pics/zzz_change_png_background_output.png')
print('done!')