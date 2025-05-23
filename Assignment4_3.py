from functools import reduce
def Add(No):
    if No >= 70 and No <= 90:
        return True
    
def increase(No):
    No = No + 10
    return No

def product(No1,No2):
    No = No1 * No2
    return No

print("Enter the size of number that you want to take : ")
size = int(input())

Data = list()

print("Enter the numbers")
for i in range(size):
    no = int(input())
    Data.append(no)

print("Input Data : ",Data)

FData = list(filter(Add,Data))
print("Filter is : ",FData)

MData = list(map(increase,FData))
print("Map is : ",MData)

RData = int(reduce(product,MData))
print("Reduce is : ",RData)