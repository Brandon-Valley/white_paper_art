from fontTools.ttLib import TTFont

import tools
import logger



def build_unknown_char_equiv_d(corrected_chars_dl):
    unknown_char_equiv_d = {}
    
    for d in corrected_chars_dl:
        unknown_char_equiv_d[d['unknown_char_unicode']] = d['correct_char']
    return unknown_char_equiv_d 



def correct_txt_file(input_txt_file_path, output_txt_file_path, corrected_chars_csv_path, font_path):
    input_lines_t = tools.read_text_file(input_txt_file_path)
    corrected_lines_l = []
    font = TTFont(font_path)
    
    corrected_chars_dl = logger.readCSV(corrected_chars_csv_path)
    unknown_char_equiv_d = build_unknown_char_equiv_d(corrected_chars_dl)
    
    for input_line in input_lines_t:
        new_corrected_line = ''
        for char in input_line:
            if tools.char_in_font(char, font) == False:
                try:
                    unkown_char_unicode = tools.char_2_unicode(char)
                    corrected_char = unknown_char_equiv_d[unkown_char_unicode]
                    new_corrected_line += corrected_char
                except Exception as e:
                    raise TypeError('''ERROR:  The input text file contains a char that is not recognized by char_in_font(), most likely this is because
                                               you have not loaded the correct and/or completed unkown_chars.csv, the unkown char unicode is:  ''' + str(e))
            else:
                new_corrected_line += char
        corrected_lines_l.append(new_corrected_line)
        
    tools.write_text_file(output_txt_file_path, corrected_lines_l)
    
    
    
input_text_file = 'aaaaa_cardano_whitepaper.txt'
output_text_file = 'corrected_' + input_text_file
corrected_chars_csv_path = 'corrected_chars.csv'
test_font_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\fonts\\cour.ttf"  
    
correct_txt_file(input_text_file, output_text_file, corrected_chars_csv_path, test_font_path)
print('done')


