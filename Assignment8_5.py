import threading

def thread1():
    print("Threading id for T1 is : ", threading.get_ident())
    print("thread name of T1 is : ",threading.current_thread().name)
    for i in range(1,51,1):
        print(i)

def thread2():
    print("Threading id for T2 is : ", threading.get_ident())
    print("thread name of T2 is : ",threading.current_thread().name)
    for i in range(50,0,-1):
        print(i)

def main():

    T1 = threading.Thread(target = thread1, name = "thread-one")
    #print("Threading id for T1 is : ", threading.get_ident())
    
    T2 = threading.Thread(target = thread2, name = "thread-two")
    #print("Threading id for T2 is : ", threading.get_ident())

    T1.start()
    T1.join()

    print("Interval")

    T2.start()
    T2.join()


if __name__ == "__main__":
    main()