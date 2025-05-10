# 7. Write a program which contains one function that accepts one number from user and returns true if number is divisible by 5 othervise return false.

def main(num):
    if (num % 5) == 0:
        print("True")
    else:
        print("False")

print("Enter a number")
no = int(input())

result = main(no)

#print("")
