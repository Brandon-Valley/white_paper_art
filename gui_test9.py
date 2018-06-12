from queue import Queue
from threading import Thread
import time

def producer(out_q):
#     time.sleep(5)
    out_q.put('hello')
    out_q.put('hello2')

def consumer(in_q):
    h = in_q.get()
    print(h + ' world!')
    in_q.task_done()
    print(in_q.get())

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))

t1.start()
t2.start()

q.join()
print('q joined!')