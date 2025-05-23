# create a python program that starts 3 threads each printing numbers from 1 to 5 with a delay of 1 second use threading.Thread
import threading
import time
i = 1
def fun(no):
    for i in no:
        print(i)

def gun(no):
    for i in no:
        print(i)

def sun(no):
    for i in no:
        print(i)

def main():

    numbers = [1,2,3,4,5]

    start_time = time.time()

    T1 = threading.Thread(target = fun, args = (numbers,))
    T2 = threading.Thread(target = gun, args = (numbers,))
    T3 = threading.Thread(target = sun, args = (numbers,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    T3.start()
    T3.join()

    end_time = time.time()

    print("The time required for execution is : ",end_time - start_time)

if __name__ == "__main__":
    main()