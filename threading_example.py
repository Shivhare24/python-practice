from threading import *
import time

# ! ways to intantiate threading object (Without any class -> functional oriented way)
# def child():
#     print('i am executed by ', current_thread().getName())

# def main():
#     print('i am executed by ', current_thread().getName())

# t1 = Thread(target=child)
# t1.start()
# main()

# ! ways to intantiate threading object (by extending thread class -> OOP way)
# class myThread(Thread):
#     def run(self):
#         print('i am executed by ', current_thread().getName())

# def main():
#     print('i am executed by ', current_thread().getName())

# t1 = myThread()
# t1.start()
# main()

# ! ways to intantiate threading object (Without extending thread class -> OOP way)
# class myThread():
#     def child(self):
#         print('i am executed by ', current_thread().getName())

# def main():
#     print('i am executed by ', current_thread().getName())

# obj = myThread()
# t1 = Thread(target=obj.child)
# t1.start()
# main()


# ! multi threadig example-01
# def double(numbers):
#     for i in numbers:
#         time.sleep(1)
#         print(f'double is: {2*i}')

# def square(numbers):
#     for i in numbers:
#         time.sleep(1)
#         print(f'square is: {i*i}')

# numbers = [1,2,3,4,5,6]
# start_time = time.time()
# t1 = Thread(target = double, args=(numbers,))
# t2 = Thread(target=square, args=(numbers,))
# t1.start() 
# t2.start()
# t1.join()
# t2.join()
# end_time = time.time()
# print(f'total execution time is: {start_time - end_time}')