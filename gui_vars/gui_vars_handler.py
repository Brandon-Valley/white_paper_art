
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))) # so you can import json_logger when running from gui

import json_logger


# assumes dir sturcture like this:"
# some_dir
#  |
#  |-- white_paper_art
#  |   |-- gui_vars
#  |       |-- gui_vars_handler.py
#  |       |-- gui_vars.json
#  |  
#  |-- white_paper_art_big_data  


GUI_VARS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
WHITE_PAPER_ART_DIR_PATH = os.path.dirname(GUI_VARS_DIR_PATH)
WHITE_PAPER_ART_BIG_DATA_DIR_PATH = os.path.dirname(WHITE_PAPER_ART_DIR_PATH) + '\\white_paper_art_big_data'


VARS_JSON_PATH = GUI_VARS_DIR_PATH + "\\gui_vars.json"
 
STR_REPLACE_D = {'<WHITE_PAPER_ART_BIG_DATA_PATH>' : WHITE_PAPER_ART_BIG_DATA_DIR_PATH}
 
def load_vars_and_apply_replacements():
    project_vars_d = json_logger.read(VARS_JSON_PATH)
    for key, val in project_vars_d.items():
        for str_to_replace, replacement_str in STR_REPLACE_D.items():
            if str_to_replace in val:
                # print('FOUND STR TO REPLACE, val: ', val)#`````````````````````````````````````````````````
                project_vars_d[key] = val.replace(str_to_replace, replacement_str)
                # print('val after replace: ', val, val.replace(str_to_replace, replacement_str))#``````````````````````````````````````````````````
    return project_vars_d
     
 
def get_var(key):
    # project_vars_d = json_logger.read(PROJECT_VARS_JSON_PATH)
    project_vars_d = load_vars_and_apply_replacements()
     
    # print(project_vars_d)#``````````````````````````````````````````````````````````````````````````
    return project_vars_d[key]






if __name__ == '__main__':
    print(get_var("input_txt_files_dir_path"))

