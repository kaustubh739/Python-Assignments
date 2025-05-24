# create a python program that uses multiprocessing.pool to compute a factorial of numbers in a list.
import multiprocessing
import time
import os
def fun(no):
    Fact = 1
    print("PID is : ",os.getpid())
    for i in range(1,no+1):
        Fact = Fact * i 
    return Fact

def main():

    Data = [100,200,300,400,500,600,700,800]

    start_time = time.time()

    P1 = multiprocessing.Pool()
    result = P1.map(fun,Data)

    P1.close()
    P1.join()

    print(result)

    end_time = time.time()

    print("Execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()