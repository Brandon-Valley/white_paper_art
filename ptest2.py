





def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
example_string = 'ZUi there' #u'\u063a\u064a\u0646\u064a'

# for c in example_string:
#     print (repr(c), c)


for c in example_string:
    print(ord(c), hex(ord(c)), c.encode('utf-8'))
    print ()