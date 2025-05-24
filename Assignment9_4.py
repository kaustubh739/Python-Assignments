# create a python program that compare the execution time of summing numbers from 1 to 10 million using normal function,threading and multiprocessing.
import threading
import multiprocessing
import time
def Add(no):
    sum = 0
    for i in range(1, no+1):
        sum = sum + i
    print("Addition is normal : ",sum)
    
def sum(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print("Addition is threading:",sum)

def gun(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print("Addition is multiprocessing:",sum)

def main():
    # normal function

    start_time = time.time()

    value = Add(10000000000)
    #print("Addition is normal",value)

    end_time = time.time()
    print("Execution time is : ",end_time - start_time)

    # threading

    start_time = time.time()

    T1 = threading.Thread(target = sum, args = (10000000000,))

    T1.start()
    T1.join()

    end_time = time.time()
    print("Execution time is : ",end_time - start_time)

    # multiprocessing

    start_time = time.time()
    
    P1 = multiprocessing.Process(target = gun, args = (10000000000,))

    P1.start() 
    P1.join()

    end_time = time.time()
    print("Execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()