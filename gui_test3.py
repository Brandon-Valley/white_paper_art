# from qtconsole.mainwindow import background



input = (255,255,0)


def highest_contrast_label_color(background_color):
    r, g, b = background_color
    
    for c in r,g,b:
        c = c / 255.0
        if c <= 0.03928:
            c = c/12.92 
        else:
            c = ((c+0.055)/1.055) ** 2.4
    L = 0.2126 * r + 0.7152 * g + 0.0722 * b
    
    if (255 - L) > L:
        return (255, 255, 255) #white
    else:
        return (0, 0, 0) #black
    
    
print(highest_contrast_label_color(input))
