# makes a txt file that looks like:

import tools

# lst = [1,2,3]
# lst2 = [5,6,7]
# print(lst+lst2)

#return key whose value is highest
def high_key(d):
    high_val = 0
    high_key = 0
    for key, val in d.items():
        if val > high_val:
            high_key = key
            high_val = val
    return high_key




test_d = {'hi': 5,
          1: 23,
          'list': 3,
          (2,4,5): 166
}
print(high_key(test_d))

if (2,4,5) in test_d:
    print('yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay')

print (test_d)






#returns true if every char in test_str is within container_list
def all_within(test_str, container_list):
    contained = True
    for test_char in test_str:
        if test_char not in container_list:
            contained = False
    return contained



import collections
s = "sssddd"
print(collections.Counter(s).most_common(1)[0][0])






t_str = '. ....     .....    '
t_list = [1, ' ', '.']

print(all_within(t_str, t_list))



print(len('                                    .---------------------------------------:        -------.       :---------------------------------------------------------------.                                   '))
num1 = 1

def pbr_test(num):
    num += 5

pbr_test(num1)
print(num1)


test_dict = {"sf": 1,
             'sdfsf': 2,
             'sfgssd': [4,5]}


print( 4 in test_dict.values())

    
        

size = 100
output_filename = 'test_grid.txt'
name = 'bob'
raise NameError ('hi there %s' %(name))

num = 3.75
print( num % 1)
print (round(num))



tools.write_text_file(output_filename, line_list)