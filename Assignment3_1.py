# Write a program which accept N number from the user and store it into the list.Return addition of all elements from that list.

print("How many nymbers are you want to enter? : ")
size = int(input())

Data = list()


print("Number of values")
for i in range(size):
    no = int(input())
    Data.append(no)

print("the values are : ",Data)

sum = 0
for value in Data:
    sum = sum + value 
print("Addition is : ",sum)


