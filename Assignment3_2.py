# Write a program which accepts N numbers from user and store it into the list return maximum number from that list.

print("Enter the size of the number")
size = int(input())

Data = list()

print("the values are")
for i in range(size):
    no =  int(input())
    Data.append(no)

print("The values are : ", Data)

for value in Data:
    no = max(Data)
print("maximum value is : ",no)