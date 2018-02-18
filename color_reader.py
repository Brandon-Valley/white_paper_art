#might be useful later, saves image with only N most-frequent colors:  https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image

from PIL import Image



#return key whose value is highest
def high_key(d):
    high_val = 0
    high_key = 0
    for key, val in d.items():
        if val > high_val:
            high_key = key
            high_val = val
    return high_key


#returns single most common color in image
def most_common_color(rgb_image, height, width):
    colors = {}
    for x in range(width):
        for y in range(height):
            r, g, b = rgb_image.getpixel((x, y))
            #check if this color has been seen before, if not, add to list, if so, increase count
            if (r, g, b) in colors:
                colors[(r, g, b)] += 1
            else:
                colors[(r, g, b)] = 1
        
        print('colors:', colors)
        #return the color with the highest count
        return high_key(colors)
                




#example main
def main():
    input_image_filename = 'color_tile1.jpg'
    im = Image.open(input_image_filename)
    rgb_im = im.convert('RGB')#not sure if needed
     
    # store dimensions
    W, H = rgb_im.size[0], rgb_im.size[1]
    print("input image dims: %d x %d" % (W, H))
     
    print(most_common_color(rgb_im, H, W))


# # call main
if __name__ == '__main__':
    main()




