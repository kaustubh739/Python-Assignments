import threading

def evenfactor(no):
    sum = 0
    for i in range(1,no + 1):
        if no % i == 0 and i % 2 == 0:
            #print(i, end = " ")
            sum = sum + i
    print("sum is : ",sum)

def Oddfactor(no):
    sum = 0
    for i in range(1,no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end = " ")
            sum = sum + i
    print("sum is : ",sum)

def main():

    T1 = threading.Thread(target = evenfactor, args = (10,))
    T2 = threading.Thread(target = Oddfactor, args = (10,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")


if __name__ == "__main__":
    main()