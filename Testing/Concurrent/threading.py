# Do tasks simultaneously

import threading
import time

start = time.time()


def compute():
    sums = 0
    for i in range(10000):
        sums += 5
    print(sums)


def compute2():
    sums = 1
    for i in range(10000):
        sums *= 5
    print(sums)


def all_in():
    sums = 0
    for _ in range(10000):
        sums += 5
    for _ in range(10000):
        sums *= 5
    print(sums)


t1 = threading.Thread(target=compute)
t2 = threading.Thread(target=compute2)

t1.start()
t2.start()

all_in()

print(time.time() - start)
