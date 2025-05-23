from functools import reduce

def Chkprime(No):
    for i in range(2,No):
        if No % i == 0:
            return False
    else:
        return True
 
def Multi(No):
    No = No * 2
    return No

def Max(No):
    return Max(No)


size = int(input("Enter the size : "))

Data = []

print("Enter the numbers : ")
for i in range(size):
    no = int(input())
    Data.append(no)

print("Input Data : ",Data)

FData = list(filter(Chkprime,Data))
print("filter is : ",FData)

MData = list(map(Multi,FData))
print("map is : ",MData)

RData = int(reduce(max,MData))
print("reduce is : ",RData)
