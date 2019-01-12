# makes a txt file that looks like:

import tools


def within_range( tup1, tup2, r):
    in_range = True
    if len(tup1) == len(tup2):
        for i in range(len(tup1)):
            if tup1[i] < tup2[i] - r or tup1[i] > tup2[i] + r:
                in_range = False
    return in_range
    
    
    
    
#     if  t1a >= t2a - r and t1a <= t2a + r and
#         t1b >= t2b - r and t1b <= t2b + r and
#         t1c >= t2c - r and t1c <= t2c + r:
#         return True
#     else:
#         return False
    
t1 = (1,1,1)
t2 = (6,6,10)
t3 = (100, 200, 100)

d1 = {'a': t2,
      'b': t3}
for d in d1.values():
    print(d)



d1_val_list = d1.values()
print(d1_val_list[0])
print(within_range(t1,d1.values(),5))












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
print('teeeeeeeest:', 23 in test_d.values())

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