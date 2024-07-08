from threading import Thread
from multiprocessing import Process
from time import time

def fibonaci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonaci(number -1) + fibonaci(number-2)

if __name__ == '__main__':
    number = 34

    # using multithreading ..!
    t1 = Thread(target=fibonaci, args=(number,))
    t2 = Thread(target=fibonaci, args=(number,))
    start = time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'total time using multithreading is {start-end} sec')

    # using multiprocessing ..!
    p1 = Process(target=fibonaci, args=(number,))
    p2 = Process(target=fibonaci, args=(number,))
    start = time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'total time using multiprocessing is {start-end} sec')
