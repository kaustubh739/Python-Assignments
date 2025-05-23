# write a python program using multiprocessing.process to square a list of numbers using multiple processes.
import multiprocessing

def square(no):
    for i in no:
        no1 = i ** 2
        print(no1)



def main():

    numbers = [2,3,4,5,6,7]

    P1 = multiprocessing.Process(target = square, args = (numbers,))

    P1.start()
    P1.join()

if __name__ == "__main__":
    main()
