from fontTools.ttLib import TTFont

import logger
import tools


UNKNOWN_CHAR_CSV_FILENAME = 'unkown_chars.csv'
WANT_UNKOWN_CHAR_CSV_BACKUP = False

UNKNOWN_CHAR_EXAMPLE_SPREAD = 20# num chars to either side of the unknown_char to include in the example



def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False
     



# returns true if the given unknown_char has not been seen before,
# if it is already in the given unknown_char_dl, adds 1 to 
# #_occurrences, then returns False
def new_unkown_char(unknown_char_unicode, unknown_char_dl):
    for unknown_char_d in unknown_char_dl:
        if unknown_char_unicode == unknown_char_d['unknown_char_unicode']:
            unknown_char_d['#_occurrences'] += 1
            return False
    return True


def char_2_unicode(char):
    return hex(ord(char))


def char_ex_insert(char_unicode):
    return string('{' + char_unicode + '}')



def build_unknown_char_example(char_num, input_lines_t, font):
#     example = ''
#     
#     example = input_lines_t[line_num][0:char_num]
#     start_line_num = line_num
#     start_char_num = char_num
#     start_char_spread = 0
#     
#     while start_char_spread < UNKNOWN_CHAR_EXAMPLE_SPREAD and line_num > 0:
#         while start_char_num > 0:
#             start_char_num =- 1
#             start_char_spread += 1
    pass


    
    


#builds dict list used to make unknown char csv
def build_unknown_char_dl(input_lines_t, font_path):
    unknown_char_dl = []
    
    font = TTFont(font_path)
    input_str = tools.format_data(input_lines_t)
    print('here')
    
    #add to unknown_char_dl when find a new char that is unknown to the font
    for line_num, line in enumerate( input_lines_t ):
        for char_num, char in line:
            if char_in_font(char, font) == False and new_unkown_char(char_2_unicode(char), unknown_char_dl) == True:
                    
                    unknown_char_dl.append({'correct_char'         : None,
                                            'unknown_char_unicode' : char_2_unicode(char),
                                            '#_occurrences'        : 1,
                                            'example'              : build_unknown_char_example(char_2_unicode(char_num, input_lines_t, font))})
                    print(unknown_char_dl)
                    
    return unknown_char_dl
                    
                
                    

def build_unknown_char_csv(input_txt_file_path, font_path):
    input_lines_t = tools.read_text_file(input_txt_file_path)
#     print(input_lines_t)#```````````````````````````````````````````````````````````````````````````````````````````````````````
    unknown_char_dl = build_unknown_char_dl(input_lines_t, font_path)
#     print('len dl: ', len(unknown_char_dl))#````````````````````````````````````````````````````````````````````````````
    logger.logList(unknown_char_dl, UNKNOWN_CHAR_CSV_FILENAME, WANT_UNKOWN_CHAR_CSV_BACKUP)
    
    

    

test_font_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\fonts\\cour.ttf"  
 

test_txt_file_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\aaaaa_cardano_whitepaper.txt"
etest_txt_file_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\easy_test_paper.txt"
    
    
    
    
    
build_unknown_char_csv(test_txt_file_path, test_font_path)

print('done!')



