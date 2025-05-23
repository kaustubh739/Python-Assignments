# write a program which accept one number from user and check wether the number is prime or not

print("Enter a number : ")
no = int(input())


for i in range(2,no):
    if no % i == 0:
        print("Not prime")
        break
else:
    print("it's a prime number")
    #break
