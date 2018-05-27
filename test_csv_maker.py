from logger import logger
import os

import random
from random import randint
import string
from prompt_toolkit.key_binding.bindings.vi import ascii_lowercase
   
full_path = os.path.realpath(__file__)
csvPath =  os.path.dirname(full_path) + '\\ds_final_test.csv'

BLANK = ""


def rand_header_name(size=6):
    return ''.join(random.choice(string.ascii_uppercase + ascii_lowercase) for _ in range(size))

def rand_bribe_str(num_bribe_digits = 3):
    return ' (' +  ''.join(random.choice(string.digits) for _ in range(num_bribe_digits)) + ')'


def rand_header_dict(size=6, num_bribe_digits = 3):
    header_dict = {}
    header_dict['currency_name'] = rand_header_name(size)
    header_dict['bribe_str'] = rand_bribe_str(num_bribe_digits)
    return header_dict






def rand_header_list(num_headers, currency_name_length, num_bribe_digits):
    header_dict_list = []
    for i in range(num_headers):
        new_header_found = False
#         print('about to endter while loop') #````````````````````````````````````````````````````````````````````````
        while(new_header_found == False):
            new_header_dict = rand_header_dict(currency_name_length, num_bribe_digits)
            
            #make sure header name isnt already in header_dict_list
            new_header_found = True
            for header_dict in header_dict_list:
                if header_dict['currency_name'] == new_header_dict['currency_name']:
                    new_header_found = False
        header_dict_list.append(new_header_dict)
        
#     print('about to make header list')#`````````````````````````````````````````````````````````````````````````````````
    #make header_list
    header_list = []
    for header_dict in header_dict_list:
#         print(header_dict)#``````````````````````````````````````````````````````````````````````````````````````````
        header_str = header_dict['currency_name'] + header_dict['bribe_str']
        header_list.append(header_str)
#         header_list.append(rand_header(currency_name_length, num_bribe_digits))
    return header_list


def print_log_list(log_list):
    for log_dict in log_list:
        print(log_dict)
    print('done printing log list')


def make_csv_data(num_verticies, currency_name_length, num_bribe_digits, min_exchange_cost, max_exchange_cost):
    header_list = rand_header_list(num_verticies, currency_name_length, num_bribe_digits)
#     print(header_list)#`````````````````````````````````````````````````````````````````````````````````````
    
    log_list = []
    
    for i in range(num_verticies):
        line_dict = {BLANK: header_list[i]}
        
        for header_num in range(num_verticies):
            line_dict[header_list[header_num]] = randint(min_exchange_cost, max_exchange_cost)
#             print(line_dict)#```````````````````````````````````````````````````````````````````````````````````````````````````````````
#         print(line_dict)#```````````````````````````````````````````````````````````````````````````````````````    
        log_list.append(line_dict)
#         print_log_list(log_list)//`````````````````````````````````````````````````````````````````
#         print(log_list)#```````````````````````````````````````````````````````````````````````
#         logger.logList(dataDictList, csvPath, wantBackup = True)
    logger.logList(log_list, csvPath, False)
        
    
    
NUM_VERTICIES = 100
CURRENCY_NAME_LENGTH = 3
NUM_BRIBE_DIGITS = 3
MIN_EXCHANGE_COST = 100
MAX_EXCHANGE_COST = 10000
    

make_csv_data(NUM_VERTICIES, CURRENCY_NAME_LENGTH, NUM_BRIBE_DIGITS, MIN_EXCHANGE_COST, MAX_EXCHANGE_COST)
print("Done!")


