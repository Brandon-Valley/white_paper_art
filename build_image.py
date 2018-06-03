import tools
import text_image
import color_cords
import offset
import font_tools

import GUI #just for testing



TEST = {'test': 3,
        'tesT': '234'}

def build_img_test(kwargs = TEST):
    print('making img...')
    print('kargs: ')
    
#     print(args)
    for key, value in kwargs.items():
        print('  %s : %s' %(key, value))
    
    print('done!')
    
    
    
    




#TIPS:

#get better resolution with larger font size

# kwargs['output_image_dim_ratio']
    #2/3:
    # a a a
    # a a a
    

def build_final_image(kwargs):
#     print(kwargs)#````````````````````````````````````````````````````````````````````````````````````````````````````````
    print('kwargs: ')
    
#     print(args)
#```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
    for key, value in kwargs.items():
        print('  %s : %s' %(key, value))
    print(' ')
    
    #IF IMAGE STARTS LOOKING WEIRD, LOOK INTO WHY SOMETIMES IN COLOR_CORDS, 
    #THERE ARE 2 OF THE SAME CORD IN ONE COLOR'S LIST, COULD HAVE TO DO WITH ROUNDING? NOT SURE IF IT EFFECTS OTHER THINGS
     
    #MUST USE MONO-SPACED FONTS
    #high resolution images will give better results
     
    #might also be helpful for making big images: https://stackoverflow.com/questions/3397157/how-to-read-a-raw-image-using-pil?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    #reading raw data: http://effbot.org/zone/pil-large-images.htm
     
    # why is there a space in front of every line?
     
     


     

    # make this work for filtering    dont clean this up until filtering works !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #set this to None for no background color separation #there is a reason for this!  this trims the whitespace so that image size can be more consistent!!!!!!!!!!!!
    input_image_background_color = kwargs['input_image_background_color'] #(255, 255, 255) #gui not done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     
    #background 
    #replace this bull shit with something to  deal with whitespace
    default_colors = {'background_image':        (255,255,255),#white
                      'final_image_background':  kwargs['final_image_background_color'],
                      'default_text':            kwargs['background_text_color']}

    
    save_image = True
    if len(kwargs['output_image_file_path']) == 0:
        save_image = False
        
    

#     print('font_size:', kwargs['font_size'])#``````````````````````````````````````````````````````````````````````````
     
     
     
     
     
     
     
     
      
      
    print('getting font aspect ratio...')
    font_aspect_ratio = font_tools.get_aspect_ratio(kwargs['font_path'])
     
     
    #read in the text that will be colored to show a picture
    print('reading in data text file...') 
    data = tools.read_text_file(kwargs['input_text_file_path'])
     
    #turn list of lines of data into one big string, use that to get number of chars in data, then split it into words
    print('formatting data into word list...')
    data_str  = tools.format_data(data)
    num_chars = len(data_str)
    word_list = data_str.split(' ')
     
     
    #turn true_dimension_ratio into max number of lines and max chars per line
    print('calculating ideal text image dimensions...')
    #find correct image dimensions by adjusting desired ratio for the difference between width and height of a char
    true_dimension_ratio = kwargs['output_image_dim_ratio'] * font_aspect_ratio
    ideal_dimentions = tools.calc_ideal_dimentions(true_dimension_ratio, num_chars)
     
    #make list of lines to be output in final image
    print('creating text lines...')
    lines = tools.make_correct_lines(ideal_dimentions['num_lines'], ideal_dimentions['line_length'], word_list)
    # print("number of lines:", len(lines))
     
    print('building color_cords from input image...')
    color_cord_dict = color_cords.get_color_cords(kwargs['input_image_file_path'], kwargs['image_size'], font_aspect_ratio, input_image_background_color)
#     print('color_cords: ', color_cord_dict)#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````
     
    print('calculating and adding user defined offset to adjusted_color_cords...')
    offset_color_cords = offset.offset_color_cords(color_cord_dict, kwargs['image_position_cords'], lines)
      
      
      
    print('making font...')
    font = font_tools.make_font(kwargs['font_path'], kwargs['font_size'], lines)#font_tools.load_font(kwargs['font_path'], kwargs['font_size']) 1111111111111111111111111111  
      
    import time #```````````````````````````````````````````````````````````````````````````````````````````````````````````````````VVVVVVVVV`````````````````
    print('sleeping')#````````````````````````````````````````````````````````````````````````````````````````````````````````````
#     time.sleep(100)   # delays for 5 seconds. You can Also Use Float Value.
    print('done sleeping')#`````````````````````````````````````````````````````````````````````````````````````````````````````````
      
    #put it all together and what have you got?  Bippity Boppity BOO!
    print('creating final image...')
    image = text_image.text_image(lines, offset_color_cords, default_colors, font)#offset_adjusted_
      
    if save_image == True:
        # image.save('test_output.jpg', format='JPEG', subsampling=0,quality = 100)
        print('saving high-resolution image...')
        image.save(kwargs['output_image_file_path'], subsampling = 0, quality = 100)
      
    print('showing low-resolution image...')
    image.show()
      
    print('done!')
    

    build_final_image(kwargs)
      


if __name__ == '__main__':
    GUI.main()   