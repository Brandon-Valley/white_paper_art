import logger








def load_unknown_chars_csv(unknown_chars_csv_path, corrected_chars_csv_path):
    unknown_chars_dl = logger.readCSV(unknown_chars_csv_path)
    print(len(unknown_chars_dl))
    
    #make sure unknown_chars csv has had all correct_chars added
    




CORRECTED_CHARS_CSV_FILENAME = 'corrected_chars.csv'
UNKNOWN_CHAR_CSV_FILENAME = 'unkown_chars.csv'


load_unknown_chars_csv(UNKNOWN_CHAR_CSV_FILENAME, CORRECTED_CHARS_CSV_FILENAME)