 # 2. Write a program which contains one function named as ChkNum() which accepts one paramenter as number.If number is even then it should display
 # display "Even number" otherwise display "Odd number" on console.

def ChkNum(num):
    if (num % 2) == 0:
        print("Even Number")
    else:
        print("Odd Number")

print("Enter a number")
no = int(input())

result = ChkNum(no)

print("zop ata")