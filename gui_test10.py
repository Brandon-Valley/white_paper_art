import threading
from threading import Thread

def func1(a):
    print ('Working1', a)

def func2(b):
    print ('Working2', b)

if __name__ == '__main__':
    Thread(target = lambda: func1('AAA')).start()
#     Thread(target = func2).start()