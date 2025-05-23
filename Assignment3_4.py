# Write a program which accepts N numbers from user and store it into the list accept one another number from user and return frequency
# of that number from list.

size = (int(input("Enter the size of numbers")))

Data = list()

print("The values are : ")
for i in range(size):
    no = int(input())
    Data.append(no)

print("which element you need to search :")
search_Data = int(input())

value = Data.count(search_Data)
print("The number is : ",value)