# makes a txt file that looks like:

import tools

# 0  1  2  3  4  5  6  7  8  9 10 11
#
#
# 1 
#
#  |                    
# 2  
#
#                     
# 3   |                    
# 4   |                     
# 5                        
# 6                        
# 7                       
# 8                            
# 9                         
# 10                         
# 11                        

size = 100
output_filename = 'test_grid.txt'


num = 3.75
print( num % 1)
print (round(num))



tools.write_text_file(output_filename, line_list)