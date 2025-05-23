# Write a program which accepts N numbers from user and store it into the list return addition of all prime numbers from that list. Main 
# python file accepts N numbers from user and pass each number to Chkprime() function which is a part of our user defined moduole named as
# MarvellousNum. Name of the function from main python file should be ListPrime().

def ChkPrime(Data):
    #no = Data
    for i in Data:
        if i % Data == 0:
            return False
        else:
            return True

    print("Enter the numbers : ")
    size = int(input())


    Data = list()

    for i in range(size):
        no = int(input("Enter the values"))
        Data.append(no)

ChkPrime()