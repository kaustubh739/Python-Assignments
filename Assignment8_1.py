# design python application which creats two thread named as even and odd. Even thread will display first 10 even numbers and odd thread 
# will display first 10 odd numbers.
import threading

def Even():
    for i in range(2,11,2):
        print(i)

def Odd():
    for i in range(1,10,2):
        print(i)

def main():

    print("Execution in parallel way")

    T1 = threading.Thread(target = Even)
    T2 = threading.Thread(target = Odd)

    T1.start()
    T1.join()
    
    T2.start()
    T2.join()

    print("End of main")

if __name__ == "__main__":
    main()