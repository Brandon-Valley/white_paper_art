import tools#could very easily remove if you take out the write_text_file in edit_text_image!!!

#removes and blends
def edit_text_image_lines(old_lines, cld):
    new_lines = []
    for old_line_num in range( len(old_lines) ):
        old_line = old_lines[old_line_num]
        new_line = ''
        old_char_num = 0
        while old_char_num < len(old_line):
            old_char = old_line[old_char_num]
            
            if old_char in cld['remove']:
                new_line += ' '
                old_char_num += 1
                print('removed (kinda):', old_char)#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
            elif old_char in cld['blend']:
                print('blended from  old_line_num: %s  old_char_num: %s  old_char: %s  ...' %(old_line_num, old_char_num, old_char))#```````````````````````````````````````
                blended_str = blend(old_lines, old_line_num, old_char_num, cld) #blend also increase old_char_num (pass-by-ref) still true????????
                new_line += blended_str
                old_char_num += len (blended_str) 
                print(blended_str)#````````````````````````````````````````````````````````````````````````````````````````````````````````
#                 print('old_char_num:', old_char_num)#    ``````````````````````````````````````````````````````````````````````````````````````````
                print('to  old_char_num - 1: %s  old_char: %s  ...' %(old_char_num - 1, old_line[old_char_num - 1]))#```````````````````````````````````` 
            else:
                new_line += old_char
                old_char_num += 1
        new_lines.append(new_line)
        
    tools.write_text_file(output_filename, new_lines)
    
    print('done!')

#returns blended string to be added to new_line and increases old_char_num (pass-by-ref) still????????????????????
def blend(old_lines, old_line_num, old_char_num, cld):
    blend_char = old_lines[old_line_num][old_char_num]
    
    if old_char_num > 0:
        lh_char = old_lines[old_line_num][old_char_num - 1]
    else:
        lh_char = None
    
    count = 0
    rh_char = blend_char
    
    while(rh_char in cld['blend']):
        count += 1
        #if you arn't about to go over the edge of the image
        if old_char_num + count < len(old_lines[old_line_num]): 
            rh_char = old_lines[old_line_num][old_char_num + count]
        else:
            rh_char = None
#         print('in loop trying to find non-blend, count = %s  rh_char = %s' %(count, rh_char))#``````````````````````````````````````````````````````````
        
            
    #once you know what is on either side, decide what/if to change the blend_chars into
    overwrite_char = ''
    possable_char_list = cld['remove'] + cld['blend'] + cld['color'] + cld['whitespace']
    possable_char_list.append(None)
    
    if lh_char not in possable_char_list and rh_char not in possable_char_list: 
        raise NameError('Encountered char that was not in possable_char_list:  lh_char = %s  rh_char = %s' %(lh_char, rh_char))
    else:
        if lh_char in cld['color'] or rh_char in cld['color']:
            print('one of the chars is in color', (lh_char, rh_char))#``````````````````````````````````````````````````````````````````````````
            if lh_char == rh_char:#if surrounded by 2 of the same color chars
                overwrite_char = lh_char
            elif lh_char in cld['color'] and rh_char in cld['color']:#if surrounded by 2 different color chars
                overwrite_char = None
            else:#if color char on one side and whitespace or the end of the image on the other side
                if lh_char in cld['remove'] or lh_char in cld['whitespace'] or lh_char == None:
                    print('color char on one side!!!!!!!!')#`````````````````````````````````````````````````````````````````````````````````````
                    overwrite_char = rh_char
                else:
                    print('color char on one side222!!!!!!!!')#`````````````````````````````````````````````````````````````````````````````````````
                    overwrite_char = lh_char
        else:#if blend chars surrounded on lh and rh side by whitespace or the edge of the image
            overwrite_char = find_isolated_blend_char(old_lines, old_line_num, old_char_num, cld, count) #make a func to set these if it's like the top or bottom of a circle!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print('should make a cap func!!!!!!!!!!!!!!')#!`````````````````````````````````````````````````````````````````````
        
        print('overwrite_char:' , overwrite_char)#`1``````````````````````````````````````````````````````````````````````````````
        blend_str = ''
        if overwrite_char != None:
            for c in range(count):
               blend_str += overwrite_char
        else:#doing it like this so that if there are multiple blend chars, they all stay the same instead of being overwritten by just one
            for c in range(count):
               blend_str += old_lines[old_line_num][old_char_num + c]
               
#         old_char_num += count - 1 # -1 b/c rh_char might need to be removed
        return blend_str
                  
#returns char to use for blending when you have a line of blend chars surrounded on the lh and rh by whitespace by looking up and down,
#will return color char most prevelent either above or below it as long as it is oly bounded by color chars on one side ie: if it has
#color chars on the top and bottom, it will return None
def find_isolated_blend_char(old_lines, old_line_num, old_char_num, cld, rh_char_pos):    
    print('old_lines:', old_lines)#````````````````````````````````````````````````````````````````````````````````````````````````````
    #get above line
    above_line = ''
    if old_line_num == 0 or old_lines[old_line_num - 1] == '':#if on top edge
        above_line += ( ' ' * (rh_char_pos - 1) ) 
    else:
        for above_char_num in range(rh_char_pos):
            above_line += old_lines[old_line_num - 1][old_char_num + above_char_num]
            
    #get below line
    below_line = ''
    if old_line_num == ( len(old_lines) - 1 ) or old_lines[old_line_num + 1] == '':#if on bottom edge
        print('on bottom!!!')#`````````````````````````````````````````````````````````````````````````````````````
        below_line += ( ' ' * (rh_char_pos - 1) ) 
    else:
        print('not on bottom!!')#````````````````````````````````````````````````````````````````````````````````````````
        for below_char_num in range(rh_char_pos):
            print('adding this to below line:', old_lines[old_line_num + 1][old_char_num + below_char_num] )#``````````````````````````````````````
            below_line += old_lines[old_line_num + 1][old_char_num + below_char_num]
            
    print('above_line, below_line:', (above_line, below_line))
        
        
    return None
        
        
text_image_filename = 'data_dash.txt'
output_filename = 'EDITED_' + text_image_filename


char_lists_dict = {'remove'      : ['.'],
                   'blend'       : [':'],
                   'color'       : ['-', '='],
                   'whitespace'  : [' ']}

# cld['remove'] = ['.']
# cld['blend'] = [':']
# cld['color'] = ['-', '=']
# cld['whitespace'] = [' ']

#get lines from original text image
original_text_image_lines = tools.read_text_file(text_image_filename)       

edit_text_image_lines(original_text_image_lines, char_lists_dict)    
            
        
        
        
        
        
        
    
        