import itertools

# 7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Oy8tLW4sri/tPG1tKKytL+1uL
# +28bKwv7W4tbCltKLxo7S3tKOjtLXs7Ozs7Ozs7Ozs7Ozs7Ozs
# 7Ozs7A

def xor(key, buf):
    for a,b in zip(itertools.cycle(key), buf):
        print (a , b)
        print (type(a) , type(b))
        
    return bytes(a**b for a,b in zip(itertools.cycle(key), buf))

# p1 = int('7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Oy8tLW4sri')
p2 = '7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Oy8tLW4sri'
buff = '7O'


print (xor(p2, buff))