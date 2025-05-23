from functools import reduce
size = int(input("Enter the number : "))

Data = []

print("the numbers are : ")
for i in range(size):
    no = int(input())
    Data.append(no)

print("Input Data : ",Data)

FData = list(filter(lambda No : No % 2 == 0,Data))
print("filter is : ",FData)

MData = list(map(lambda No : No ** 2,FData))
print("map is : ",MData)

RData = int(reduce(lambda No1,No2 : No1 + No2,MData))
print("Reduce is : ",RData)
