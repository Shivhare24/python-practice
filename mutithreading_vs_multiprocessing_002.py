from threading import Thread
from multiprocessing import Process
from os import cpu_count
from time import time
from math import sqrt

def calc():
    for i in range (0, 4000000):
        sqrt(i)

if __name__=='__main__':
    
    # using multithreading ..!
    threads = []
    for i in range(cpu_count()):
        print(f'registering thread {i}')
        threads.append(Thread(target=calc))
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    
    # using multiprocessing ..!
    processes = []
    for i in range(cpu_count()):
        print(f'registering process {i}')
        processes.append(Process(target=calc))
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
