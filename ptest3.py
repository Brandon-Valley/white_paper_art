

file_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\white_paper_art\\test_chars.txt"

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
txt_data = read_text_file(file_path)
# print(chars)

ex_str = txt_data[0]
# print(ex_str)

     
for c in ex_str:
    print(ord(c), hex(ord(c)))#, c.encode('utf-8'))