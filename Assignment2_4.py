# write a program which accept one number from user and return addition of it's factors.

print("Enter a number")
no = int(input())

#i = 1 
sum = 0
for i in range(1,no):
    if no % i == 0:
        print(i)
        sum = sum + i

print("Addition is :",sum)    


