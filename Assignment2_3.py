# write a program which accept one number from user and return it's factorial
print("Enter the number")
no = int(input())

Fact = 1
for i in range(no):
    Fact = Fact * no
    no = no - 1

    #return Fact
print("The Factorial of given number is : ",Fact) 

