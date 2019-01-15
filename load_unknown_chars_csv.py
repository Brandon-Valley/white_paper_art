import logger
import os


WANT_BACKUP = True

def char_already_corrected(unknown_char_unicode, corrected_chars_dl):
    if corrected_chars_dl == []:
        return False
    
    for corrected_chars_d in corrected_chars_dl:
        if corrected_chars_d['unknown_char_unicode'] == unknown_char_unicode:
            return True
        
    return False 
    

def find_new_corrected_chars(corrected_chars_dl, unknown_chars_dl):
    new_corrected_chars_dl = []
    
    for unknown_char_d in unknown_chars_dl:
        if char_already_corrected(unknown_char_d['unknown_char_unicode'], corrected_chars_dl) == False:
            unknown_char_d.pop('#_occurrences')
            new_corrected_chars_dl.append(unknown_char_d)
    return new_corrected_chars_dl


# def add_corrected_chars(corrected_chars_dl, unknown_chars_dl):
#     for unknown_char_d in unknown_chars_dl:
#         if char_already_corrected(unknown_char_d['unknown_char_unicode'], corrected_chars_dl) == False:
#             unknown_char_d.pop('#_occurrences')
#             corrected_chars_dl.append(unknown_char_d)
#     return corrected_chars_dl
    


def all_correct_chars_entered(unknown_chars_dl):
    for dict in unknown_chars_dl:
        if dict['correct_char'] == '':
            return False
    return True
    

def load_unknown_chars_csv(unknown_chars_csv_path, corrected_chars_csv_path):
    unknown_chars_dl = logger.readCSV(unknown_chars_csv_path)
    
    #make sure unknown_chars csv has had all correct_chars added
    if all_correct_chars_entered(unknown_chars_dl) == False:
        raise TypeError('ERROR:  You must enter all values for "correct_char" in unknown_chars')
    
    #read original corrected chars csv if it exists
    if os.path.isfile(corrected_chars_csv_path) == True:
        og_corrected_chars_dl = logger.readCSV(corrected_chars_csv_path)
    else:
        og_corrected_chars_dl = []
        
#     final_corrected_chars_dl = add_corrected_chars(og_corrected_chars_dl, unknown_chars_dl) #```````````````````````````````````````````
    new_corrected_chars_dl = find_new_corrected_chars(og_corrected_chars_dl, unknown_chars_dl)
#     print(new_corrected_chars_dl)#```````````````````````````````````````````````````````````````````````````````````````````````````
    
    header_order_list = ['correct_char', 'unknown_char_unicode', 'example']
    
    if new_corrected_chars_dl != []:
        logger.logList(new_corrected_chars_dl, corrected_chars_csv_path, WANT_BACKUP, header_order_list, 'append')




CORRECTED_CHARS_CSV_FILENAME = 'corrected_chars.csv'
UNKNOWN_CHAR_CSV_FILENAME = 'unkown_chars.csv'


load_unknown_chars_csv(UNKNOWN_CHAR_CSV_FILENAME, CORRECTED_CHARS_CSV_FILENAME)
print('done!')

