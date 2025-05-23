# Write a program which accept number from user and return addition of digits in that number.

no = int(input("enter a number"))

sum = 0 

while no > 0:
    sum = no % 10
    print(sum)