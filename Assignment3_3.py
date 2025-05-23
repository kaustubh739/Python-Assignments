# Write a program which accepts N numbers from user and store it into the list return minimum number from that list.

print("Enter the size :")
size = int(input())

Data = list()

print("the values are : ")
for i in range(size):
    no = int(input())
    Data.append(no)

print("the values are : ", Data)

for value in Data:
    no = min(Data)
print("the minimun : ",no)


