import threading

def small(msg):
    for i in msg:
        if int('a' <= i <= 'z'):
            print(i, end = " ")
def capital(msg):
    for i in msg:
        if int('A' <= i <= 'Z'):
            print(i, end = " ")

def digits(msg):
    for i in msg:
        if int(i >= 0):
            print(i, end = " ")
def main():

    str = ("A","B",23,"c","d","E","f",7,45)

    T1 = threading.Thread(target = small, args = (str,))

    T2 = threading.Thread(target = capital, args = (str,))

    T3 = threading.Thread(target = digits, args = (str,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()