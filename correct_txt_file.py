import tools
from fontTools.ttLib import TTFont



def correct_txt_file(input_txt_file_path, output_txt_file_path, corrected_chars_csv_path, font_path):
    input_lines_t = tools.read_text_file(input_txt_file_path)
    corrected_lines_l = []
    font = TTFont(font_path)
    
    for input_line in input_lines_t:
        new_corrected_line = ''
        for char in input_line:
            if tools.char_in_font(char, font) == False:
                pass #`````````````````````````````````````````````````````````````````````````````````````````````````!!!!!!!!!!!!!!!!!!!!!
            else:
                new_corrected_line += char
        corrected_lines_l.append(new_corrected_line)
        
    tools.write_text_file(output_txt_file_path, corrected_lines_l)
    
    
    
input_text_file = 'aaaaa_cardano_whitepaper.txt'
output_text_file = 'corrected_' + input_text_file
corrected_chars_csv_path = 'correct_chars.csv'
test_font_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\fonts\\cour.ttf"  
    
correct_txt_file(input_text_file, output_text_file, corrected_chars_csv_path, test_font_path)
print('done')


